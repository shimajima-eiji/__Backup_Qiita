import json
from json_object import Article, Articles
from datetime import datetime

def main():
    xml_articles = Articles()
    rss_articles = Articles()

    try:
        with open('output/xml_backup.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data.get('articles', []):
                # Safely get all fields, providing None for missing optional fields
                article = Article(
                    post_id=item.get('post_id'),
                    title=item.get('title'),
                    link=item.get('link'),
                    pub_date=item.get('pub_date'),
                    creator=item.get('creator'),
                    guid=item.get('guid'),
                    content=item.get('content'),
                    post_date=item.get('post_date'),
                    status=item.get('status'),
                    description=item.get('description') # description might be missing in xml_backup
                )
                xml_articles.add_article(article)
    except FileNotFoundError:
        print("xml_backup.json not found. Skipping XML data loading.")

    try:
        with open('output/rss_backup.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data.get('articles', []):
                # Safely get all fields, providing None for missing optional fields
                article = Article(
                    post_id=item.get('post_id'),
                    title=item.get('title'),
                    link=item.get('link'),
                    pub_date=item.get('pub_date'),
                    creator=item.get('creator'),
                    guid=item.get('guid'),
                    content=item.get('content'),
                    post_date=item.get('post_date'),
                    status=item.get('status'),
                    description=item.get('description')
                )
                rss_articles.add_article(article)
    except FileNotFoundError:
        print("rss_backup.json not found. Skipping RSS data loading.")

    verified_articles = Articles()
    post_id_counter = 1

    # Process XML articles first
    for article in xml_articles.articles:
        verified_articles.add_article(article)

    # Process RSS articles
    for rss_article in rss_articles.articles:
        # Auto-generate post_id if empty or None
        if rss_article.post_id is None or rss_article.post_id == 0:
            rss_article.post_id = post_id_counter
            post_id_counter += 1

        # Check for existing article with same guid
        found = False
        for existing_article in verified_articles.articles:
            if existing_article.guid == rss_article.guid:
                found = True
                # Compare publish_date and update if newer
                # Ensure pub_date is not None before parsing
                if rss_article.pub_date and existing_article.pub_date:
                    try:
                        rss_pub_date = datetime.strptime(rss_article.pub_date, '%a, %d %b %Y %H:%M:%S %z')
                        existing_pub_date = datetime.strptime(existing_article.pub_date, '%a, %d %b %Y %H:%M:%S %z')
                        if rss_pub_date > existing_pub_date:
                            # Update existing article with RSS data
                            existing_article.title = rss_article.title
                            existing_article.link = rss_article.link
                            existing_article.pub_date = rss_article.pub_date
                            existing_article.creator = rss_article.creator
                            existing_article.description = rss_article.description
                    except ValueError as e:
                        print(f"Error parsing date for GUID {rss_article.guid}: {e}")
                break
        if not found:
            verified_articles.add_article(rss_article)

    with open('output/verified_articles.json', 'w', encoding='utf-8') as f:
        f.write(verified_articles.to_json())

if __name__ == '__main__':
    main()