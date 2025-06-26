import requests
import xml.etree.ElementTree as ET
import os
import re
from urllib.parse import unquote
import argparse
import json
from bs4 import BeautifulSoup
from datetime import datetime

# RSSフィードのURL
RSS_FEED_URL = "https://note.com/nomuragoro/rss"

def sanitize_filename(text: str, max_length: int = 100) -> str:
    """
    ファイル名として安全な文字列に変換します。
    """
    sanitized = re.sub(r'[\\/:*?"<>|]', '', text)
    sanitized = sanitized.replace(' ', '_')
    sanitized = sanitized.strip()
    return sanitized[:max_length]

def get_max_post_id_digits_from_existing_json(output_directory: str) -> int:
    """
    既存のJSONファイルからpost_idの最大桁数を計算します。
    """
    max_id = 0
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            if filename.endswith(".json"):
                try:
                    # ファイル名からpost_idを抽出
                    match = re.match(r'^(\d+)_.*\.json$', filename)
                    if match:
                        post_id = int(match.group(1))
                        max_id = max(max_id, post_id)
                except ValueError:
                    continue
    return len(str(max_id)) if max_id > 0 else 1

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

    # 既存のJSONファイルからpost_idの最大桁数を取得
    max_post_id_digits = get_max_post_id_digits_from_existing_json(output_directory)
    
    # ファイル名全体の目標長（例: 30文字）
    target_filename_total_length = 30
    # post_idのパディング長 + アンダースコア1文字 + タイトル長 = 30
    title_max_length = target_filename_total_length - max_post_id_digits - 1
    if title_max_length < 1:
        title_max_length = 1

    # 既存の記事IDをロードして、更新が必要か判断する
    existing_article_ids = set()
    existing_articles_data = {}
    if os.path.exists(output_directory):
        for filename in os.listdir(output_directory):
            if filename.endswith(".json"):
                filepath = os.path.join(output_directory, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if 'id' in data:
                            existing_article_ids.add(data['id'])
                            existing_articles_data[data['id']] = data
                except json.JSONDecodeError:
                    print(f"Warning: Could not decode JSON from {filename}. Skipping.")
                except Exception as e:
                    print(f"Warning: Error reading {filename}: {e}. Skipping.")

    for i, item in enumerate(items):
        title = item.find('title').text or f"Untitled Article {i+1}"
        pub_date_str = item.find('pubDate').text or ""
        content_html_elem = item.find('content:encoded', namespaces)
        content_html = content_html_elem.text if content_html_elem is not None else ""
        guid = item.find('guid').text or f"unknown_guid_{i}"

        # RSSフィードにはwp:status, wp:post_id, wp:post_typeがないため、Noneまたはデフォルト値を使用
        status = "publish" # RSSフィードは通常公開記事のみを含む
        post_id = None # RSSフィードからは直接取得できない
        post_type = "post" # RSSフィードは通常投稿記事のみを含む

        # 既存のpost_idを再利用するか、新しいpost_idを割り当てる
        # Note: RSSフィードにはpost_idがないため、ここではguidをベースに一意性を判断
        # 既存のファイル名からpost_idを抽出するロジックを考慮
        current_post_id = None
        if guid in existing_articles_data and 'post_id' in existing_articles_data[guid] and existing_articles_data[guid]['post_id'] is not None:
            current_post_id = existing_articles_data[guid]['post_id']
        else:
            # 新しい記事の場合、既存のpost_idの最大値+1を割り当てる
            # これは簡易的なもので、より堅牢なID管理が必要な場合は別途検討
            max_existing_post_id = 0
            for existing_filename in os.listdir(output_directory):
                if existing_filename.endswith(".json"):
                    match = re.match(r'^(\d+)_.*\.json$', existing_filename)
                    if match:
                        max_existing_post_id = max(max_existing_post_id, int(match.group(1)))
            current_post_id = str(max_existing_post_id + 1)

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

        # ファイル名を post_id とサニタイズされたタイトルに基づいて生成
        filename_base = ""
        if current_post_id and str(current_post_id).isdigit():
            padded_post_id = str(current_post_id).zfill(max_post_id_digits)
            filename_base = f"{padded_post_id}_{sanitize_filename(title, max_length=title_max_length)}"
        else:
            filename_base = sanitize_filename(title, max_length=target_filename_total_length)
            if not filename_base:
                filename_base = f"article_{i}"

        output_filepath = os.path.join(output_directory, f"{filename_base}.json")

        article_data = {
            'id': guid,
            'post_id': current_post_id,
            'title': title,
            'publish_date': formatted_pub_date,
            'status': status,
            'post_type': post_type,
            'content': content_lines,
            'images': images
        }

        # 差分検出と更新/追加
        is_new_article = guid not in existing_article_ids
        is_updated_article = False

        if not is_new_article:
            # 既存の記事がある場合、内容を比較して更新されたかチェック
            # 簡易的な比較（JSON文字列化して比較）
            existing_data = existing_articles_data[guid]
            # post_idは動的に割り当てられるため比較から除外
            temp_existing_data = existing_data.copy()
            temp_article_data = article_data.copy()
            temp_existing_data.pop('post_id', None)
            temp_article_data.pop('post_id', None)

            if json.dumps(temp_existing_data, ensure_ascii=False, sort_keys=True) != \
               json.dumps(temp_article_data, ensure_ascii=False, sort_keys=True):
                is_updated_article = True
                # 古いファイルを削除して新しいファイルに置き換える
                old_filename_match = re.match(r'^(\d+)_.*\.json$', existing_articles_data[guid]['filename'])
                if old_filename_match:
                    old_filepath = os.path.join(output_directory, existing_articles_data[guid]['filename'])
                    if os.path.exists(old_filepath):
                        os.remove(old_filepath)
                        print(f"Removed old version of {existing_articles_data[guid]['title']}")

        if is_new_article or is_updated_article:
            # ファイル名衝突時の処理（連番を追加）
            final_output_filepath = output_filepath
            counter = 1
            while os.path.exists(final_output_filepath):
                final_output_filepath = os.path.join(output_directory, f"{filename_base}_{counter}.json")
                counter += 1
            
            # 記事データに最終的なファイル名を保存（差分検出のために必要）
            article_data['filename'] = os.path.basename(final_output_filepath)

            try:
                with open(final_output_filepath, 'w', encoding='utf-8') as f:
                    json.dump(article_data, f, ensure_ascii=False, indent=4)
                if is_new_article:
                    added_count += 1
                    print(f"Successfully added: '{title}' to '{final_output_filepath}'")
                elif is_updated_article:
                    updated_count += 1
                    print(f"Successfully updated: '{title}' to '{final_output_filepath}'")
            except IOError as e:
                print(f"Error writing file '{final_output_filepath}': {e}")

    print(f"\nExtraction and update complete. Total {added_count} articles added, {updated_count} articles updated to '{output_directory}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and update articles from Note.com RSS feed.")
    parser.add_argument("-o", "--output", default="note", 
                        help="Directory to save extracted articles (default: note)")
    args = parser.parse_args()

    extract_and_update_articles_from_rss(args.output)
