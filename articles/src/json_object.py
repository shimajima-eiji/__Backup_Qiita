from dataclasses import dataclass, asdict, field
from datetime import datetime
import json
from typing import List, Dict, Any, Optional

@dataclass
class Article:
    title: str
    link: str
    pub_date: str
    creator: str
    guid: str
    description: Optional[str] = None
    post_id: Optional[int] = None
    content: Optional[str] = None
    post_date: Optional[str] = None
    status: Optional[str] = None

@dataclass
class Articles:
    articles: List[Article] = field(default_factory=list)

    def to_json(self):
        return json.dumps(asdict(self), indent=2, ensure_ascii=False)

    def add_article(self, article: Article):
        self.articles.append(article)
