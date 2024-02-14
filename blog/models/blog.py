from sqlmodel import SQLModel, Field
from typing import Optional, List


class Post(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(unique=True)
    content: str
