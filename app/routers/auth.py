from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)
from app.services.auth_service import login_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    token = login_user(
        db=db,
        email=credentials.email,
        password=credentials.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }