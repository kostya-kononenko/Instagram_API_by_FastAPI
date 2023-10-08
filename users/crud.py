from fastapi import HTTPException, status

from users import models, schemas
from sqlalchemy.orm.session import Session

from users.hashing import Hash


def create_user(db: Session, request: schemas.UserBase):
    new_user = models.DBUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(db: Session, username: str):
    user = db.query(models.DBUser).filter(
        models.DBUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username {username} not found",
        )
    return user
