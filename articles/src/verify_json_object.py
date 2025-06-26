import json
import os
from datetime import datetime
from json_object import Article

def verify_and_filter_articles(new_articles, existing_articles_dir):
    existing_articles = {}
    for filename in os.listdir(existing_articles_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(existing_articles_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                article = Article.from_json(data)
                existing_articles[article.guid] = article

    filtered_articles = []
    for new_article in new_articles:
        if new_article.guid in existing_articles:
            existing_article = existing_articles[new_article.guid]
            # Compare pub_date. If new article is older or same, skip.
            # Assuming pub_date is in 'yyyy-MM-dd HH:MM:SS' or 'yyyy-MM-dd HH:MM' format
            try:
                new_pub_date = datetime.strptime(new_article.pub_date, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                new_pub_date = datetime.strptime(new_article.pub_date, '%Y-%m-%d %H:%M')
            
            try:
                existing_pub_date = datetime.strptime(existing_article.pub_date, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                existing_pub_date = datetime.strptime(existing_article.pub_date, '%Y-%m-%d %H:%M')

            if new_pub_date <= existing_pub_date:
                print(f"Skipping {new_article.guid}: New article is older or same as existing.")
                continue
        filtered_articles.append(new_article)
    return filtered_articles

if __name__ == '__main__':
    # This is a placeholder for testing. In a real scenario, new_articles would come from rss_backup.py or xml_backup.py
    # And existing_articles_dir would be the output directory.
    # For demonstration, let's create some dummy articles.
    dummy_new_articles = [
        Article(title="New Article 1", pub_date="2025-06-26 10:00:00", guid="n_new_1", content=["Content 1"], status="publish"),
        Article(title="New Article 2", pub_date="2025-06-26 11:00:00", guid="n_existing_1", content=["Content 2"], status="publish"), # This one should update existing_1
        Article(title="New Article 3", pub_date="2025-06-26 09:00:00", guid="n_existing_2", content=["Content 3"], status="publish"), # This one should be skipped
    ]

    # Create dummy existing files in output directory for testing
    output_dir = '/mnt/c/Users/shima/Desktop/学習アプリ開発_GeminiCLIデモ/articles/output'
    os.makedirs(output_dir, exist_ok=True)

    # Existing article 1 (will be updated)
    with open(os.path.join(output_dir, 'xml_n_existing_1.json'), 'w', encoding='utf-8') as f:
        json.dump(Article(title="Existing Article 1", pub_date="2025-06-26 09:30:00", guid="n_existing_1", content=["Old Content 1"], status="publish").to_json(), f, ensure_ascii=False, indent=2)
    
    # Existing article 2 (will be skipped)
    with open(os.path.join(output_dir, 'xml_n_existing_2.json'), 'w', encoding='utf-8') as f:
        json.dump(Article(title="Existing Article 2", pub_date="2025-06-26 10:00:00", guid="n_existing_2", content=["Old Content 2"], status="publish").to_json(), f, ensure_ascii=False, indent=2)

    print("--- Running verification ---")
    filtered = verify_and_filter_articles(dummy_new_articles, output_dir)
    print("Filtered articles GUIDs:", [a.guid for a in filtered])
    print("--- Verification complete ---")
