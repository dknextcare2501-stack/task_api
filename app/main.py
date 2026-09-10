from fastapi import FastAPI

from app.db.database import engine
from app.models.user import Base
from app.routers import users
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(auth.router)


