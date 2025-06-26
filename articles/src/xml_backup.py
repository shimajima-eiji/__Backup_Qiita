import xml.etree.ElementTree as ET
from json_object import Article, Articles

def main():
    tree = ET.parse('master/note-nomuragoro-1.xml')
    root = tree.getroot()

    articles = Articles()

    for item in root.findall('.//item'):
        article = Article(
            post_id=int(item.find('{http://wordpress.org/export/1.2/}post_id').text),
            title=item.find('title').text,
            link=item.find('link').text,
            pub_date=item.find('pubDate').text,
            creator=item.find('{http://purl.org/dc/elements/1.1/}creator').text,
            guid=item.find('guid').text,
            content=item.find('{http://purl.org/rss/1.0/modules/content/}encoded').text,
            post_date=item.find('{http://wordpress.org/export/1.2/}post_date').text,
            status=item.find('{http://wordpress.org/export/1.2/}status').text
        )
        articles.add_article(article)

    with open('output/xml_backup.json', 'w', encoding='utf-8') as f:
        f.write(articles.to_json())

if __name__ == '__main__':
    main()