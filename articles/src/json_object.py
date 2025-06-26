from dataclasses import dataclass, asdict, field
from datetime import datetime
import json
from typing import List, Dict, Any

@dataclass
class Article:
    post_id: int
    title: str
    link: str
    pub_date: str
    creator: str
    guid: str
    content: str
    post_date: str
    status: str

@dataclass
class Articles:
    articles: List[Article] = field(default_factory=list)

    def to_json(self):
        return json.dumps(asdict(self), indent=2, ensure_ascii=False)

    def add_article(self, article: Article):
        self.articles.append(article)
