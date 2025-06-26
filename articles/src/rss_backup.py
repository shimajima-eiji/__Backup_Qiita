import re
import json
from json_object import Article, Articles

def main():
    with open('master/sample.rss', 'r', encoding='utf-8') as f:
        content = f.read()

    articles = Articles()

    # Regex to find each item block
    item_pattern = re.compile(r'<item>(.*?)</item>', re.DOTALL)
    items = item_pattern.findall(content)

    for item_str in items:
        title_match = re.search(r'<title>(.*?)</title>', item_str, re.DOTALL)
        link_match = re.search(r'<link>(.*?)</link>', item_str, re.DOTALL)
        pub_date_match = re.search(r'<pubDate>(.*?)</pubDate>', item_str, re.DOTALL)
        creator_match = re.search(r'<note:creatorName>(.*?)</note:creatorName>', item_str, re.DOTALL)
        guid_match = re.search(r'<guid>(.*?)</guid>', item_str, re.DOTALL)
        description_match = re.search(r'<description>(.*?)</description>', item_str, re.DOTALL)

        title = title_match.group(1) if title_match else ''
        link = link_match.group(1) if link_match else ''
        pub_date = pub_date_match.group(1) if pub_date_match else ''
        creator = creator_match.group(1) if creator_match else ''
        guid = guid_match.group(1) if guid_match else ''
        description = description_match.group(1) if description_match else ''

        article = Article(
            title=title,
            link=link,
            pub_date=pub_date,
            creator=creator,
            guid=guid,
            description=description
        )
        articles.add_article(article)

    with open('output/rss_backup.json', 'w', encoding='utf-8') as f:
        f.write(articles.to_json())

if __name__ == '__main__':
    main()
