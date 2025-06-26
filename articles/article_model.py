from dataclasses import dataclass, field
import json
import os
import re
from datetime import datetime # datetimeをインポート

@dataclass
class ArticleData:
    id: str
    title: str
    publish_date: str
    status: str
    post_type: str
    content: list[str]
    images: list[dict]

def sanitize_filename(text: str, max_length: int = 100) -> str:
    """
    ファイル名として安全な文字列に変換します。
    """
    sanitized = re.sub(r'[\\/:*?"<>|]', '', text)
    sanitized = sanitized.replace(' ', '_')
    sanitized = sanitized.strip()
    return sanitized[:max_length]

def save_article_to_json(article: ArticleData, output_directory: str) -> str:
    """
    記事データをJSONファイルとして保存します。
    ファイル名の衝突を解決し、適切なファイル名を生成します。

    :param article: 保存する記事データ。
    :type article: ArticleData
    :param output_directory: ファイルを保存するディレクトリ。
    :type output_directory: str
    :returns: 保存されたファイルのフルパス。
    :rtype: str
    """
    # ファイル名生成: (publish_date=yyyymmdd-HHMM)_(id).json
    # publish_dateをdatetimeオブジェクトに変換してフォーマット
    try:
        dt_object = datetime.fromisoformat(article.publish_date)
        date_part = dt_object.strftime("%Y%m%d-%H%M")
    except ValueError:
        date_part = "unknown_date"

    # idはnxxxx形式であることを想定
    base_filename = f"{date_part}_{article.id}"

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
