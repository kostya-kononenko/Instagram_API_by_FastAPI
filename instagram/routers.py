from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from instagram import schemas, crud
from database.database import get_db


router = APIRouter(prefix="/post", tags=["post"])

image_url_types = ['absolute', 'relative']


@router.post("", response_model=schemas.PostDisplay)
def create(
    request: schemas.PostBase,
    db: Session = Depends(get_db),
):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.",
        )
    return crud.create_post(db, request)


@router.get('/all', response_model=List[schemas.PostDisplay])
def posts(db: Session = Depends(get_db)):
    return crud.get_all_posts(db)
