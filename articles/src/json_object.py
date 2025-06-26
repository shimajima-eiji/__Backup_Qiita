from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Article:
    title: str
    pub_date: str
    guid: str
    content: List[str] = field(default_factory=list)
    status: str

    def to_json(self):
        return {
            "title": self.title,
            "pub_date": self.pub_date,
            "guid": self.guid,
            "content": self.content,
            "status": self.status,
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            title=data["title"],
            pub_date=data["pub_date"],
            guid=data["guid"],
            content=data.get("content", []),
            status=data["status"],
        )
