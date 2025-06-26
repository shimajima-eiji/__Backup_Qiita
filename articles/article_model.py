from dataclasses import dataclass, field
import json
import os
import re

@dataclass
class ArticleData:
    id: str
    title: str
    publish_date: str
    status: str
    post_type: str
    content: list[str]
    images: list[dict]
    post_id: str | None = None # post_idをオプションとして追加

def sanitize_filename(text: str, max_length: int = 100) -> str:
    """
    ファイル名として安全な文字列に変換します。
    """
    sanitized = re.sub(r'[\\/:*?"<>|]', '', text)
    sanitized = sanitized.replace(' ', '_')
    sanitized = sanitized.strip()
    return sanitized[:max_length]

def save_article_to_json(article: ArticleData, output_directory: str, filename_prefix: str = "") -> str:
    """
    記事データをJSONファイルとして保存します。
    ファイル名の衝突を解決し、適切なファイル名を生成します。

    :param article: 保存する記事データ。
    :type article: ArticleData
    :param output_directory: ファイルを保存するディレクトリ。
    :type output_directory: str
    :param filename_prefix: ファイル名に付加するプレフィックス（例: post_id）。
    :type filename_prefix: str
    :returns: 保存されたファイルのフルパス。
    :rtype: str
    """
    # ファイル名生成
    sanitized_title = sanitize_filename(article.title, max_length=30) # ファイル名タイトル部分の最大長を30に固定
    
    if filename_prefix:
        base_filename = f"{filename_prefix}_{sanitized_title}"
    else:
        # guidからID部分を抽出してファイル名に利用
        match = re.search(r'/n/([a-zA-Z0-9]+)$', article.id)
        if match:
            guid_part = match.group(1)
        else:
            guid_part = sanitize_filename(article.id, max_length=10) # guidがURLでない場合のフォールバック
        base_filename = f"{guid_part}_{sanitized_title}"

    output_filepath = os.path.join(output_directory, f"{base_filename}.json")

    # ファイル名衝突時の処理（連番を追加）
    counter = 1
    while os.path.exists(output_filepath):
        output_filepath = os.path.join(output_directory, f"{base_filename}_{counter}.json")
        counter += 1

    try:
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(article.__dict__, f, ensure_ascii=False, indent=4)
        return output_filepath
    except IOError as e:
        print(f"Error writing file '{output_filepath}': {e}")
        return ""
