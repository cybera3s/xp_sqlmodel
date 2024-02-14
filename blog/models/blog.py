from sqlmodel import SQLModel, Field
from typing import Optional, List


class Post(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(unique=True)
    content: str
    views_count: int | None = Field(default=None)


class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    body: str