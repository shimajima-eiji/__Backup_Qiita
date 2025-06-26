# -*- coding: utf-8 -*-
"""
extract_note_articles

Note.com からエクスポートされた XML ファイルを解析し、
各記事を構造化された JSON 形式で抽出するためのスクリプト。

AI との協調開発を念頭に置き、以下の設計原則に基づいています。

- **明確な目的と機能分離**: 各関数は単一の明確な目的を持ち、理解しやすいように設計されています。
- **データ構造の最適化**: 抽出される JSON データは、機械処理と人間による管理の両方に適した形式です。
  - 記事IDに基づくファイル命名規則により、ファイル管理とソートが容易になります。
  - 日付はISO 8601形式で統一され、プログラムでの扱いやすさを向上させます。
  - 本文は行ごとに分割され、テキスト処理の柔軟性を高めます。
  - 画像情報は別途抽出され、コンテンツの欠損を防ぎます。
- **堅牢性とエラーハンドリング**: ファイルの読み込みやディレクトリ作成時のエラーを適切に処理します。
- **自己文書化**: コード内のコメントは、処理の「なぜ」と「どのように」を説明し、
  将来のメンテナンスやAIによる解析を容易にします。
  (参考: https://qiita.com/nomurasan/items/e450cb0135e250022aaf.md)
"""

import xml.etree.ElementTree as ET
import os
import re
from urllib.parse import unquote
import argparse
import json
from bs4 import BeautifulSoup
from datetime import datetime

from article_model import ArticleData, sanitize_filename, save_article_to_json

def get_max_post_id_digits(xml_file_path: str) -> int:
    """
    XMLファイル内のすべての記事のpost_idの最大値から、その桁数を計算します。

    これにより、ファイル名のゼロパディングを動的に調整し、ソート順の問題を解決します。

    :param xml_file_path: 入力XMLファイルのパス。
    :type xml_file_path: str
    :returns: post_idの最大桁数。post_idが見つからない場合やエラー時は1を返します。
    :rtype: int
    """
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error reading or parsing XML for max post ID digits: {e}")
        return 1

    namespaces = {'wp': 'http://wordpress.org/export/1.2/'}
    max_id = 0
    for item in root.findall('.//item'):
        post_id_elem = item.find('wp:post_id', namespaces)
        if post_id_elem is not None and post_id_elem.text and post_id_elem.text.isdigit():
            max_id = max(max_id, int(post_id_elem.text))
    return len(str(max_id)) if max_id > 0 else 1

def extract_articles_from_note_xml(xml_file_path: str, output_directory: str = "note") -> None:
    """
    Note.com の XML バックアップファイルを解析し、各記事を個別の JSON ファイルとして抽出します。

    抽出されるデータ構造は、後続の処理（例: AIによる分析、ウェブサイト生成）に適しています。

    :param xml_file_path: 入力XMLファイルのフルパス。
    :type xml_file_path: str
    :param output_directory: 抽出された記事を保存するディレクトリ。
    :type output_directory: str
    :returns: None
    :rtype: None
    :raises FileNotFoundError: 指定されたXMLファイルが見つからない場合。
    :raises xml.etree.ElementTree.ParseError: XMLファイルのパースに失敗した場合。
    :raises OSError: 出力ディレクトリの作成に失敗した場合。
    :raises IOError: JSONファイルの書き込みに失敗した場合。
    """
    # XML名前空間の定義
    # Note.com のエクスポートファイルで使用される主要な名前空間
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'wp': 'http://wordpress.org/export/1.2/',
    }

    # 出力ディレクトリが存在しない場合は作成
    try:
        os.makedirs(output_directory, exist_ok=True)
        print(f"Output directory '{output_directory}' ensured.")
    except OSError as e:
        print(f"Error creating output directory '{output_directory}': {e}")
        return

    # XMLファイルの解析
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except FileNotFoundError:
        print(f"Error: XML file not found at '{xml_file_path}'")
        return
    except ET.ParseError as e:
        print(f"Error parsing XML file '{xml_file_path}': {e}\n"
              "Please ensure the XML file is well-formed.")
        return

    # すべての 'item' 要素（個々の記事を表す）を検索
    items = root.findall('.//item')
    if not items:
        print("No <item> elements found in the XML file. Check the XML structure.")
        return

    print(f"Found {len(items)} articles to extract.")
    extracted_count = 0

    # ファイル名のゼロパディング桁数を動的に計算
    max_post_id_digits = get_max_post_id_digits(xml_file_path)
    
    # ファイル名全体の目標長（例: 30文字）から、タイトル部分の最大長を計算
    # post_idのパディング長 + アンダースコア1文字 + タイトル長 = 目標長
    # タイトル長 = 目標長 - post_idのパディング長 - 1
    target_filename_total_length = 30
    title_max_length = target_filename_total_length - max_post_id_digits - 1
    if title_max_length < 1:
        title_max_length = 1

    for i, item in enumerate(items):
        # 記事の基本情報を抽出
        # 欠損時のフォールバックも考慮
        title = item.find('title').text or f"Untitled Article {i+1}"
        pub_date_str = item.find('pubDate').text or ""
        content_html = item.find('content:encoded', namespaces).text or ""
        
        # 記事のステータス、post_id、post_typeを抽出
        # これらの情報は、記事の管理やフィルタリングに役立ちます。
        status_elem = item.find('wp:status', namespaces)
        status = status_elem.text if status_elem is not None else "unknown"

        post_id_elem = item.find('wp:post_id', namespaces)
        post_id = post_id_elem.text if post_id_elem is not None else None

        post_type_elem = item.find('wp:post_type', namespaces)
        post_type = post_type_elem.text if post_type_elem is not None else "post"

        # 記事のユニークな識別子 (guid)
        # ファイル名生成のフォールバックとしても使用
        guid = item.find('guid').text or f"unknown_guid_{i}"

        # 公開日をISO 8601形式にフォーマット
        # プログラムでの日付処理を容易にするため
        formatted_pub_date = ""
        try:
            # 例: Thu, 01 Jan 2020 00:00:00 +0900
            dt_object = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %z')
            formatted_pub_date = dt_object.isoformat()
        except ValueError:
            formatted_pub_date = pub_date_str # パース失敗時は元の文字列をフォールバック

        # BeautifulSoup を使用してHTMLコンテンツを解析
        soup = BeautifulSoup(content_html, 'html.parser')
        
        # 画像情報を抽出
        # 記事内の画像への参照を構造化して保存することで、画像管理を容易にします。
        images = []
        for img_tag in soup.find_all('img'):
            img_info = {
                'src': img_tag.get('src'),
                'alt': img_tag.get('alt', ''),
                'width': img_tag.get('width'),
                'height': img_tag.get('height')
            }
            images.append(img_info)

        # HTMLコンテンツからプレーンテキストを抽出し、行ごとに分割
        # コンテンツの行ごとの処理や、トークン化などの前処理を容易にするため
        content_text = soup.get_text(separator='\n', strip=True)
        content_lines = [line.strip() for line in content_text.splitlines() if line.strip()]

        # 記事データをJSON形式で構造化
        article_data = ArticleData(
            id=guid,
            post_id=post_id,
            title=title,
            publish_date=formatted_pub_date,
            status=status,
            post_type=post_type,
            content=content_lines,
            images=images
        )

        # ファイル名を post_id とサニタイズされたタイトルに基づいて生成
        # 人間が読みやすく、ソートしやすいファイル名を提供します。
        filename_prefix = ""
        if post_id and str(post_id).isdigit():
            filename_prefix = str(post_id).zfill(max_post_id_digits)

        saved_filepath = save_article_to_json(article_data, output_directory, filename_prefix)
        if saved_filepath:
            print(f"Successfully extracted: '{title}' to '{saved_filepath}'")
            extracted_count += 1

    print(f"\nExtraction complete. Total {extracted_count} articles extracted to '{output_directory}'.")

if __name__ == "__main__":
    # コマンドライン引数のパーサー設定
    # スクリプトの柔軟性を高め、異なるXMLファイルや出力ディレクトリに対応
    parser = argparse.ArgumentParser(description="Extract articles from a Note.com XML export file.")
    parser.add_argument("xml_file", nargs='?', default="note-nomuragoro-1.xml", 
                        help="Path to the input XML file (default: note-nomuragoro-1.xml)")
    parser.add_argument("-o", "--output", default="note", 
                        help="Directory to save extracted articles (default: note)")
    args = parser.parse_args()

    # 記事抽出関数の実行
    extract_articles_from_note_xml(args.xml_file, args.output)
