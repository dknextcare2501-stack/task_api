from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import (
    verify_password,
    create_access_token
)

from app.repositories.user_repository import (
    get_user_by_email
)


def login_user(
    db: Session,
    email: str,
    password: str
):
    user = get_user_by_email(
        db,
        email
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    password_valid = verify_password(
        password,
        user.password_hash
    )

    if not password_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token({
        "sub": str(user.id)
    })

    return token