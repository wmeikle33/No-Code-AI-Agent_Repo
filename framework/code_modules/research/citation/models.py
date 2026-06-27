from pydantic import BaseModel
from typing import Optional


class Citation(BaseModel):
    title: str
    url: Optional[str] = None
    author: Optional[str] = None
    publication_date: Optional[str] = None
    publisher: Optional[str] = None
    access_date: Optional[str] = None


class Source(BaseModel):
    id: str
    title: str
    content: str
    url: Optional[str] = None
