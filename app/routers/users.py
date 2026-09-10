from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.user_service import (get_users, get_users_greater_than_age, get_user, create_new_user, update_existing_user, delete_existing_user)
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from fastapi import Depends
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_users(db)

@router.get("/filter", response_model=list[UserResponse])
def get_filtered_users(max_age: int):
    return get_users_greater_than_age(max_age)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(db, name=user.name, email=user.email, age=user.age, password=user.password)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_existing_user(db, user_id, user.name, user.email, user.age, user.is_active)
    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not Found"
        )

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    delete_existing_user(db, user_id)