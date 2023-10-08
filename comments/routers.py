from comments.schemas import CommentBase
from users.schemas import UserAuth
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from comments import crud
from auth.oauth2 import get_current_user

router = APIRouter(prefix="/comment", tags=["comment"])


@router.get("/all/{post_id}")
def comments(post_id: int, db: Session = Depends(get_db)):
    return crud.get_all(db, post_id)


@router.post("")
def create(
    request: CommentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return crud.create(db, request)
