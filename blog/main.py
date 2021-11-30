from fastapi import FastAPI

from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(router=blog.router)
app.include_router(router=user.router)
app.include_router(router=authentication.router)
