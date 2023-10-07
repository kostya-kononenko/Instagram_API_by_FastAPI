from instagram import models, schemas
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
