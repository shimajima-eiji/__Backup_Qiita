import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

from json_object import Article

def parse_rss_to_articles(rss_file_path):
    tree = ET.parse(rss_file_path)
    root = tree.getroot()

    articles = []

    for item in root.findall('.//item'):
        title = item.find('title').text if item.find('title') is not None else ''
        pub_date_str = item.find('pubDate').text if item.find('pubDate') is not None else ''
        guid_element = item.find('guid')
        guid = guid_element.text.split('/')[-1] if guid_element is not None and guid_element.text else ''

        # RSS feed does not have a direct 'status' field like XML export, default to 'publish'
        status = 'publish'

        description_element = item.find('description')
        content_list = []
        if description_element is not None and description_element.text:
            soup = BeautifulSoup(description_element.text, 'html.parser')
            for p_tag in soup.find_all('p'):
                if p_tag.get_text(strip=True):
                    content_list.append(p_tag.get_text(strip=True))
            for img_tag in soup.find_all('img'):
                if img_tag.get('src'):
                    content_list.append(img_tag['src'])

        # Format pub_date to 'yyyy-MM-dd HH:MM:SS' or 'yyyy-MM-dd HH:MM'
        try:
            # Attempt to parse with seconds first
            dt_object = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %z')
            formatted_pub_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                # If parsing with seconds fails, try without seconds
                dt_object = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M %z')
                formatted_pub_date = dt_object.strftime('%Y-%m-%d %H:%M')
            except ValueError:
                formatted_pub_date = pub_date_str # Fallback if parsing fails

        article = Article(
            title=title,
            pub_date=formatted_pub_date,
            guid=guid,
            content=content_list,
            status=status
        )
        articles.append(article)
    return articles

def save_articles_as_json(articles, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for article in articles:
        file_name = f"rss_{article.guid}.json"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(article.to_json(), f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    rss_file = '/mnt/c/Users/shima/Desktop/学習アプリ開発_GeminiCLIデモ/articles/master/sample.rss'
    output_directory = '/mnt/c/Users/shima/Desktop/学習アプリ開発_GeminiCLIデモ/articles/output'
    
    articles = parse_rss_to_articles(rss_file)
    save_articles_as_json(articles, output_directory)
    print(f"Processed {len(articles)} articles from {rss_file} and saved to {output_directory}")
