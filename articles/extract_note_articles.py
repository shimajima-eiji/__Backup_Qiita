import xml.etree.ElementTree as ET
import os
import re
from urllib.parse import unquote
import argparse
import json
from bs4 import BeautifulSoup

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

    for i, item in enumerate(items):
        title = item.find('title').text or f"Untitled Article {i+1}"
        link = item.find('link').text or "#"
        creator = item.find('dc:creator', namespaces).text or "Unknown Author"
        pub_date = item.find('pubDate').text or "No Date"
        content_html = item.find('content:encoded', namespaces).text or ""
        post_name = item.find('wp:post_name', namespaces).text

        soup = BeautifulSoup(content_html, 'html.parser')
        content_text = soup.get_text(separator='\n', strip=True)

        filename_base = None
        if post_name:
            decoded_post_name = unquote(post_name)
            filename_base = re.sub(r'[\\/:*?"<>|]', '', decoded_post_name).strip()

        if not filename_base:
            sanitized_title = re.sub(r'[\\/:*?"<>|]', '', title).strip()
            if sanitized_title:
                filename_base = sanitized_title
            else:
                guid = item.find('guid').text or f"unknown_guid_{i}"
                filename_base = f"article_{guid}"

        filename_base = filename_base[:150]
        output_filename = os.path.join(output_directory, f"{filename_base}.json")

        counter = 1
        while os.path.exists(output_filename):
            output_filename = os.path.join(output_directory, f"{filename_base}_{counter}.json")
            counter += 1

        article_data = {
            'title': title,
            'link': link,
            'author': creator,
            'publish_date': pub_date,
            'content': content_text
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