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
