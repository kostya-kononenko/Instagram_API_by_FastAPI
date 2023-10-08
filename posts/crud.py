from fastapi import HTTPException, status

from posts import models, schemas
from sqlalchemy.orm.session import Session
import datetime


def create_post(db: Session, request: schemas.PostBase):
    new_post = models.DBPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=request.creator_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db: Session):
    return db.query(models.DBPost).all()


def delete(db: Session, id: int, user_id: int):
    post = db.query(models.DBPost).filter(models.DBPost.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )
    if post.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only post creator can delete post",
        )

    db.delete(post)
    db.commit()
    return "ok"
