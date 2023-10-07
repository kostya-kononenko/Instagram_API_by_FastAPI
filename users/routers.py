from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from database.database import get_db
from users import crud, schemas


router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=schemas.UserDisplay)
def create_new_user(request: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, request=request)
