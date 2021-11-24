from typing import Optional

from fastapi import FastAPI

app = FastAPI()


# noinspection PyUnusedLocal
@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the database"}
    else:
        return {"data": f"{limit} blogs from the database"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{blog_id}")
def show(blog_id: int):
    return {"data": blog_id}


@app.post("/blog")
def create_blog():
    return {"data": "Blog was created"}
