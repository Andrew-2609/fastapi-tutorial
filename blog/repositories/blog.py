from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import models
from .. import schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_by_id(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} is not available")

    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(blog_id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with it {blog_id} is not available")

    blog.update(dict(request))
    db.commit()

    response = {"detail": "updated"}
    response.update(dict(request))

    return response


def delete(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} is not available")

    blog.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
