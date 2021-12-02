from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database, oauth2
from ..database import get_db
from ..repositories import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)


# noinspection PyUnusedLocal
@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db),
                  current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_by_id(blog_id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id: int, request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(blog_id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(blog_id, db)
