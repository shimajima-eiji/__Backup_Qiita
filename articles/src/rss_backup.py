import re
import json
from json_object import Article, Articles
import os

def main():
    with open('master/sample.rss', 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find each item block
    item_pattern = re.compile(r'<item>(.*?)</item>', re.DOTALL)
    items = item_pattern.findall(content)

    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)

    # Initialize a counter for post_id for RSS articles
    # This assumes that post_ids from XML are already loaded or will be handled by merge_xml_rss.py
    # For now, let's start from a high number to avoid collision with XML post_ids if they are small.
    # A better approach would be to find the max post_id from existing articles.
    # For this task, I will assume post_id generation is handled during the merge process if needed.
    # The design doc says "rss では post_id が空欄のため自動採番したり" which implies it's handled during verification/merge.
    # So, I will not generate post_id here, but rather in merge_xml_rss.py.

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
            description=description,
            source='rss' # Set source to 'rss'
        )
        
        # Sanitize GUID for filename
        sanitized_guid = re.sub(r'[^a-zA-Z0-9_.-]', '_', article.guid)
        filename = f"output/{sanitized_guid}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(article.__dict__, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()