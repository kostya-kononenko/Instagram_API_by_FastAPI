from datetime import datetime
from sqlalchemy.orm import Session
from comments import models, schemas


def create(db: Session, request: schemas.CommentBase):
    new_comment = models.DBComment(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
        timestamp=datetime.now(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db: Session, post_id: int):
    return db.query(models.DBComment).filter(
        models.DBComment.post_id == post_id).all()
