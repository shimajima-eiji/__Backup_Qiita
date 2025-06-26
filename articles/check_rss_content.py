import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

RSS_FEED_URL = "https://note.com/nomuragoro/rss"

def check_rss_content_length():
    namespaces = {'content': 'http://purl.org/rss/1.0/modules/content/'}

    try:
        response = requests.get(RSS_FEED_URL)
        response.raise_for_status()
        rss_content = response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return

    try:
        root = ET.fromstring(rss_content)
    except ET.ParseError as e:
        print(f"Error parsing RSS feed: {e}")
        return

    items = root.findall('.//item')
    print(f'Found {len(items)} items in RSS feed.')

    for i, item in enumerate(items[:5]): # Check first 5 articles
        title_elem = item.find('title')
        title = title_elem.text if title_elem is not None else f"Untitled Article {i+1}"

        content_html_elem = item.find('content:encoded', namespaces)
        content_html = content_html_elem.text if content_html_elem is not None else ''

        soup = BeautifulSoup(content_html, 'html.parser')
        content_text = soup.get_text(separator='\n', strip=True)

        print(f'Article {i+1} (Title: {title}): Content length = {len(content_text)}')

if __name__ == "__main__":
    check_rss_content_length()
