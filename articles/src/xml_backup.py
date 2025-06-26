import xml.etree.ElementTree as ET
from json_object import Article, Articles
import json

def main():
    tree = ET.parse('master/note-nomuragoro-1.xml')
    root = tree.getroot()

    for item in root.findall('.//item'):
        # Safely get all fields, providing None for missing optional fields
        post_id_element = item.find('{http://wordpress.org/export/1.2/}post_id')
        title_element = item.find('title')
        link_element = item.find('link')
        pub_date_element = item.find('pubDate')
        creator_element = item.find('{http://purl.org/dc/elements/1.1/}creator')
        guid_element = item.find('guid')
        content_element = item.find('{http://purl.org/rss/1.0/modules/content/}encoded')
        post_date_element = item.find('{http://wordpress.org/export/1.2/}post_date')
        status_element = item.find('{http://wordpress.org/export/1.2/}status')
        description_element = item.find('description') # description might be missing in xml_backup

        article = Article(
            post_id=int(post_id_element.text) if post_id_element is not None else None,
            title=title_element.text if title_element is not None else None,
            link=link_element.text if link_element is not None else None,
            pub_date=pub_date_element.text if pub_date_element is not None else None,
            creator=creator_element.text if creator_element is not None else None,
            guid=guid_element.text if guid_element is not None else None,
            content=content_element.text if content_element is not None else None,
            post_date=post_date_element.text if post_date_element is not None else None,
            status=status_element.text if status_element is not None else None,
            description=description_element.text if description_element is not None else None,
            source='xml' # Set source to 'xml'
        )
        
        # Save each article as a separate JSON file named by its GUID
        filename = f"output/{article.guid}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(article.__dict__, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
