import xml.etree.ElementTree as ET
import os
import re
from urllib.parse import unquote
import argparse
import json
from bs4 import BeautifulSoup
from datetime import datetime

def sanitize_filename(text, max_length=100):
    # Remove invalid characters for filenames
    sanitized = re.sub(r'[\\/:*?"<>|]', '', text)
    # Replace spaces with underscores (optional, but good for consistency)
    sanitized = sanitized.replace(' ', '_')
    # Remove leading/trailing whitespace
    sanitized = sanitized.strip()
    # Truncate to max_length
    return sanitized[:max_length]

def get_max_post_id_digits(xml_file_path: str) -> int:
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except (FileNotFoundError, ET.ParseError):
        return 0

    namespaces = {'wp': 'http://wordpress.org/export/1.2/'}
    max_id = 0
    for item in root.findall('.//item'):
        post_id_elem = item.find('wp:post_id', namespaces)
        if post_id_elem is not None and post_id_elem.text.isdigit():
            max_id = max(max_id, int(post_id_elem.text))
    return len(str(max_id)) if max_id > 0 else 1

def extract_articles_from_note_xml(xml_file_path: str, output_directory: str = "note") -> None:
    """
    Parses a Note.com XML backup file and extracts each article into a separate JSON file.

    Args:
        xml_file_path (str): The full path to the input XML file.
        output_directory (str): The directory where extracted articles will be saved.
    """
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'wp': 'http://wordpress.org/export/1.2/',
    }

    try:
        os.makedirs(output_directory, exist_ok=True)
        print(f"Output directory '{output_directory}' ensured.")
    except OSError as e:
        print(f"Error creating output directory '{output_directory}': {e}")
        return

    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except FileNotFoundError:
        print(f"Error: XML file not found at '{xml_file_path}'")
        return
    except ET.ParseError as e:
        print(f"Error parsing XML file '{xml_file_path}': {e}")
        return

    items = root.findall('.//item')
    if not items:
        print("No <item> elements found in the XML file.")
        return

    print(f"Found {len(items)} articles to extract.")
    extracted_count = 0

    # Calculate max post_id digits for padding
    max_post_id_digits = get_max_post_id_digits(xml_file_path)
    
    # Target total filename length is around 30 characters
    # post_id_padding + underscore + title_length = 30
    # title_length = 30 - post_id_padding - 1
    title_max_length = 30 - max_post_id_digits - 1
    if title_max_length < 1: # Ensure title_max_length is at least 1
        title_max_length = 1

    for i, item in enumerate(items):
        title = item.find('title').text or f"Untitled Article {i+1}"
        pub_date_str = item.find('pubDate').text or ""
        content_html = item.find('content:encoded', namespaces).text or ""
        
        # Extract status, post_id, post_type
        status_elem = item.find('wp:status', namespaces)
        status = status_elem.text if status_elem is not None else "unknown"

        post_id_elem = item.find('wp:post_id', namespaces)
        post_id = post_id_elem.text if post_id_elem is not None else None

        post_type_elem = item.find('wp:post_type', namespaces)
        post_type = post_type_elem.text if post_type_elem is not None else "post"

        guid = item.find('guid').text or f"unknown_guid_{i}"

        # Format publish date to ISO 8601
        formatted_pub_date = ""
        try:
            dt_object = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %z')
            formatted_pub_date = dt_object.isoformat()
        except ValueError:
            formatted_pub_date = pub_date_str # Fallback to original if parsing fails

        soup = BeautifulSoup(content_html, 'html.parser')
        
        # Extract image information
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

        # Generate filename based on post_id and sanitized title
        filename_base = ""
        if post_id and post_id.isdigit():
            # Zero-pad post_id dynamically
            padded_post_id = str(post_id).zfill(max_post_id_digits)
            filename_base = f"{padded_post_id}_{sanitize_filename(title, max_length=title_max_length)}"
        else:
            # Fallback if post_id is not available or not a digit
            filename_base = sanitize_filename(title, max_length=30) # Use 30 for title if no ID
            if not filename_base:
                filename_base = f"article_{i}"

        output_filename = os.path.join(output_directory, f"{filename_base}.json")

        counter = 1
        while os.path.exists(output_filename):
            output_filename = os.path.join(output_directory, f"{filename_base}_{counter}.json")
            counter += 1

        article_data = {
            'id': guid, # Keep the original guid for reference
            'post_id': post_id, # Added
            'title': title,
            'publish_date': formatted_pub_date,
            'status': status, # Added
            'post_type': post_type, # Added
            'content': content_lines,
            'images': images # Added
        }

        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                json.dump(article_data, f, ensure_ascii=False, indent=4)
            print(f"Successfully extracted: '{title}' to '{output_filename}'")
            extracted_count += 1
        except IOError as e:
            print(f"Error writing file '{output_filename}': {e}")

    print(f"\nExtraction complete. Total {extracted_count} articles extracted to '{output_directory}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract articles from a Note.com XML export file.")
    parser.add_argument("xml_file", nargs='?', default="note-nomuragoro-1.xml", help="Path to the input XML file (default: note-nomuragoro-1.xml)")
    parser.add_argument("-o", "--output", default="note", help="Directory to save extracted articles (default: note)")
    args = parser.parse_args()

    extract_articles_from_note_xml(args.xml_file, args.output)
