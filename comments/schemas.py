from pydantic import BaseModel
from datetime import datetime


class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime

    class Config:
        from_attributes = True


class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int
