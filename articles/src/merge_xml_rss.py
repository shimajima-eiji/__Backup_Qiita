import json
import os
from datetime import datetime
from json_object import Article

def main():
    output_dir = 'output'
    merged_articles = {}

    # Define source priorities for tie-breaking
    source_priority = {
        'fix': 3,
        'xml': 2,
        'rss': 1
    }

    for filename in os.listdir(output_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Determine source: if not present, assume 'fix'
                if 'source' not in data or data['source'] is None:
                    data['source'] = 'fix'
                article = Article(**data)

                if article.guid not in merged_articles:
                    merged_articles[article.guid] = article
                else:
                    existing_article = merged_articles[article.guid]

                    # Convert pub_date to datetime objects for comparison
                    try:
                        existing_pub_date = datetime.strptime(existing_article.pub_date, '%a, %d %b %Y %H:%M:%S %z')
                    except ValueError:
                        existing_pub_date = datetime.min # Fallback for unparseable dates

                    try:
                        new_pub_date = datetime.strptime(article.pub_date, '%a, %d %b %Y %H:%M:%S %z')
                    except ValueError:
                        new_pub_date = datetime.min # Fallback for unparseable dates

                    if new_pub_date > existing_pub_date:
                        merged_articles[article.guid] = article
                    elif new_pub_date == existing_pub_date:
                        # Apply tie-breaking rule based on source priority
                        existing_priority = source_priority.get(existing_article.source, 0)
                        new_priority = source_priority.get(article.source, 0)

                        if new_priority > existing_priority:
                            merged_articles[article.guid] = article

    # Assign post_ids to articles that don't have them
    max_post_id = 0
    for article in merged_articles.values():
        if article.post_id is not None:
            max_post_id = max(max_post_id, article.post_id)

    for article in merged_articles.values():
        if article.post_id is None or article.post_id == 0:
            max_post_id += 1
            article.post_id = max_post_id

    # Write merged articles back to output directory
    for guid, article in merged_articles.items():
        # Sanitize GUID for filename (already done in xml_backup and rss_backup, but good to be safe)
        sanitized_guid = guid.replace('https://note.com/nomuragoro/n/', '').replace('/', '_').replace('.', '_')
        filename = f"output/{sanitized_guid}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(article.__dict__, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()