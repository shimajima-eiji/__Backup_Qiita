import requests
import xml.etree.ElementTree as ET
import os
import re
from urllib.parse import unquote
import argparse
import json
from bs4 import BeautifulSoup
from datetime import datetime

from article_model import ArticleData, sanitize_filename, save_article_to_json

# RSSフィードのURL
RSS_FEED_URL = "https://note.com/nomuragoro/rss"

def get_max_post_id_from_existing_json(output_directory: str) -> int:
    """
    既存のJSONファイルからpost_idの最大値を取得します。
    """
    max_id = 0
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            if filename.endswith(".json"):
                filepath = os.path.join(output_directory, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if 'post_id' in data and data['post_id'] is not None:
                            try:
                                max_id = max(max_id, int(data['post_id']))
                            except ValueError:
                                pass # post_idが数字でない場合は無視
                except (json.JSONDecodeError, Exception) as e:
                    print(f"Warning: Error reading {filename}: {e}. Skipping.")
    return max_id

def get_max_post_id_digits(max_post_id: int) -> int:
    """
    post_idの最大値から、その桁数を計算します。
    """
    return len(str(max_post_id)) if max_post_id > 0 else 1

def extract_and_update_articles_from_rss(output_directory: str = "note") -> None:
    """
    RSSフィードから記事を抽出し、既存のJSONファイルと比較して更新または追加します。
    """
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
    }

    try:
        os.makedirs(output_directory, exist_ok=True)
        print(f"Output directory '{output_directory}' ensured.")
    except OSError as e:
        print(f"Error creating output directory '{output_directory}': {e}")
        return

    # RSSフィードの取得
    try:
        response = requests.get(RSS_FEED_URL)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
        rss_content = response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return

    # RSSフィードの解析
    try:
        root = ET.fromstring(rss_content)
    except ET.ParseError as e:
        print(f"Error parsing RSS feed: {e}\n" \
              "Please ensure the RSS feed is well-formed XML.")
        return

    items = root.findall('.//item')
    if not items:
        print("No <item> elements found in the RSS feed.")
        return

    print(f"Found {len(items)} articles in RSS feed.")
    updated_count = 0
    added_count = 0

    # 既存の記事データをロード (guidをキーとして)
    existing_articles_by_guid = {}
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            if filename.endswith(".json"):
                filepath = os.path.join(output_directory, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if 'id' in data: # 'id'はguid
                            existing_articles_by_guid[data['id']] = data
                except (json.JSONDecodeError, Exception) as e:
                    print(f"Warning: Error reading {filename}: {e}. Skipping.")

    # post_idの最大値と桁数を取得
    max_existing_post_id = get_max_post_id_from_existing_json(output_directory)
    max_post_id_digits = get_max_post_id_digits(max_existing_post_id + len(items)) # RSSで追加される可能性のある記事数も考慮
    
    # ファイル名全体の目標長（例: 30文字）
    target_filename_total_length = 30
    # post_idのパディング長 + アンダースコア1文字 + タイトル長 = 30
    title_max_length = target_filename_total_length - max_post_id_digits - 1
    if title_max_length < 1:
        title_max_length = 1

    for i, item in enumerate(items):
        title = item.find('title').text or f"Untitled Article {i+1}"
        pub_date_str = item.find('pubDate').text or ""
        content_html_elem = item.find('content:encoded', namespaces)
        content_html = content_html_elem.text if content_html_elem is not None else ""
        
        # guidをextractスクリプトと同様にサニタイズ
        guid_full = item.find('guid').text or f"unknown_guid_{i}"
        match = re.search(r'/n/([a-zA-Z0-9]+)$', guid_full)
        if match:
            guid = match.group(1)
        else:
            guid = sanitize_filename(guid_full, max_length=10) # guidがURLでない場合のフォールバック

        # RSSフィードにはwp:status, wp:post_id, wp:post_typeがないため、デフォルト値を使用
        status = "publish" 
        post_type = "post" 

        # post_idの割り当てロジック
        current_post_id = None
        if guid in existing_articles_by_guid: # 既存の記事の場合、既存のpost_idを再利用
            current_post_id = existing_articles_by_guid[guid].get('post_id') # .get()でKeyErrorを回避
        
        # 新しい記事、または既存記事だがpost_idがNoneの場合に新しいpost_idを割り当てる
        if current_post_id is None:
            max_existing_post_id += 1 # 新しい記事ごとにインクリメント
            current_post_id = str(max_existing_post_id)

        # 公開日をISO 8601形式にフォーマット
        formatted_pub_date = ""
        try:
            dt_object = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %z')
            formatted_pub_date = dt_object.isoformat()
        except ValueError:
            formatted_pub_date = pub_date_str

        soup = BeautifulSoup(content_html, 'html.parser')
        
        images = []
        for img_tag in soup.find_all('img'):
            img_info = {
                'src': img_tag.get('src'),
                'alt': img_tag.get('alt', ''),
                'width': img_tag.get('width'),
                'height': img_tag.get('height')
            }
            images.append(img_info)

        content_text = soup.get_text(separator='\n', strip=True)
        content_lines = [line.strip() for line in content_text.splitlines() if line.strip()]

        # RSSフィードのcontentが空の場合、既存のcontentを保持
        if not content_lines and guid in existing_articles_by_guid:
            content_lines = existing_articles_by_guid[guid]['content']

        article_data = ArticleData(
            id=guid,
            post_id=current_post_id, # post_idをdataclassに含める
            title=title,
            publish_date=formatted_pub_date,
            status=status,
            post_type=post_type,
            content=content_lines,
            images=images
        )

        # 差分検出と更新/追加
        is_new_article = guid not in existing_articles_by_guid
        is_updated_article = False

        if not is_new_article:
            existing_data = existing_articles_by_guid[guid]
            
            # post_idは動的に割り当てられるため比較から除外
            temp_existing_data = existing_data.copy()
            temp_article_data = article_data.__dict__.copy() # dataclassのdict表現
            temp_existing_data.pop('post_id', None)
            temp_article_data.pop('post_id', None)

            if json.dumps(temp_existing_data, ensure_ascii=False, sort_keys=True) != json.dumps(temp_article_data, ensure_ascii=False, sort_keys=True):
                is_updated_article = True
                # 古いファイルを削除
                # 既存のファイル名を特定し、削除
                for existing_filename in os.listdir(output_directory):
                    filepath_to_check = os.path.join(output_directory, existing_filename)
                    try:
                        with open(filepath_to_check, 'r', encoding='utf-8') as f_check:
                            check_data = json.load(f_check)
                            if 'id' in check_data and check_data['id'] == guid:
                                os.remove(filepath_to_check)
                                print(f"Removed old version of {existing_filename}")
                                break
                    except (json.JSONDecodeError, Exception):
                        continue

        if is_new_article or is_updated_article:
            # ファイル名生成
            padded_post_id = str(current_post_id).zfill(max_post_id_digits)
            filename_prefix = padded_post_id

            saved_filepath = save_article_to_json(article_data, output_directory, filename_prefix)
            if saved_filepath:
                if is_new_article:
                    added_count += 1
                    print(f"Successfully added: '{title}' to '{saved_filepath}'")
                elif is_updated_article:
                    updated_count += 1
                    print(f"Successfully updated: '{title}' to '{saved_filepath}'")

    print(f"\nExtraction and update complete. Total {added_count} articles added, {updated_count} articles updated to '{output_directory}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and update articles from Note.com RSS feed.")
    parser.add_argument("-o", "--output", default="note", 
                        help="Directory to save extracted articles (default: note)")
    args = parser.parse_args()

    extract_and_update_articles_from_rss(args.output)