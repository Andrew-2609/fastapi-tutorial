from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..repositories import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.get_by_id(user_id, db)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)
