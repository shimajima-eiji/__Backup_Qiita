import json
import os
from datetime import datetime
from json_object import Article

def merge_articles(output_dir):
    articles_map = {}

    # Load existing articles (fix, xml, rss)
    for filename in os.listdir(output_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    article = Article.from_json(data)

                    prefix, guid = filename.split('_', 1)
                    guid = guid.replace('.json', '')

                    if guid not in articles_map:
                        articles_map[guid] = {'fix': None, 'xml': None, 'rss': None}

                    if prefix == 'fix':
                        articles_map[guid]['fix'] = article
                    elif prefix == 'xml':
                        articles_map[guid]['xml'] = article
                    elif prefix == 'rss':
                        articles_map[guid]['rss'] = article
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {filename}. Skipping.")
                    continue

    # Process and merge articles
    for guid, versions in articles_map.items():
        best_article = None
        best_pub_date = None

        # Determine the best article based on pub_date and priority
        for source in ['fix', 'xml', 'rss']:
            article = versions[source]
            if article:
                try:
                    current_pub_date = datetime.strptime(article.pub_date, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    current_pub_date = datetime.strptime(article.pub_date, '%Y-%m-%d %H:%M')

                if best_article is None or current_pub_date > best_pub_date:
                    best_article = article
                    best_pub_date = current_pub_date
                elif current_pub_date == best_pub_date:
                    # Apply priority if pub_date is the same
                    if source == 'fix' and versions['fix']:
                        best_article = versions['fix']
                    elif source == 'xml' and versions['xml'] and best_article != versions['fix']:
                        best_article = versions['xml']
                    elif source == 'rss' and versions['rss'] and best_article not in [versions['fix'], versions['xml']]:
                        best_article = versions['rss']

        if best_article:
            # Save the best article as fix_GUID.json
            output_file_path = os.path.join(output_dir, f"fix_{best_article.guid}.json")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                json.dump(best_article.to_json(), f, ensure_ascii=False, indent=2)

            # Delete xml_ and rss_ versions
            for source_prefix in ['xml_', 'rss_']:
                file_to_delete = os.path.join(output_dir, f"{source_prefix}{guid}.json")
                if os.path.exists(file_to_delete):
                    os.remove(file_to_delete)
                    print(f"Deleted {file_to_delete}")

if __name__ == '__main__':
    output_directory = '/mnt/c/Users/shima/Desktop/学習アプリ開発_GeminiCLIデモ/articles/output'
    merge_articles(output_directory)
    print(f"Merge process completed for articles in {output_directory}")
