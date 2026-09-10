from sqlalchemy.orm import Session
from app.repositories.user_repository import get_all_users, get_filtered_under_age, get_user_by_id, create_user, update_user, delete_user
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def get_users(db: Session):
    return get_all_users(db)

def get_users_greater_than_age(db: Session, max_age:int):
    return get_filtered_under_age(db, max_age)

def get_user(db: Session, user_id: int):
    return get_user_by_id(db, user_id)

def create_new_user(db: Session, name: str, email: str, age: int, password: str):
    try:
        user = create_user(db, name, email, age, password)
        return user
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Email already exist"
        )

def update_existing_user(db: Session, user_id: int, name: str, email: str, age: int, is_active: bool):
    user = get_user_by_id(db, user_id)
    return update_user(db, user, name, email, age, is_active)

def delete_existing_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    return delete_user(db, user)