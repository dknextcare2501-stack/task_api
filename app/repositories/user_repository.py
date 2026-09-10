from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.core.security import hash_password


def get_all_users(db: Session):
    return db.query(User).all()

def get_filtered_under_age(db:Session, max_age: int):
    return db.query(User).filter(
        User.age > max_age
    )

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(
        User.id == user_id
    ).first()


def create_user(
    db: Session,
    name: str,
    email: str,
    age: int,
    password: str
):
    user = User(
        name=name,
        email=email,
        age=age,
        password_hash=hash_password(password),
        is_active=True
    )
    try:
        db.add(user)    
        db.commit()
        db.refresh(user)

        return user
    except IntegrityError:
        db.rollback()
        raise

def update_user(
    db: Session,
    user: User,
    name: str,
    email: str,
    age: int,
    is_active: bool
):
    user.name = name
    user.email = email
    user.age = age
    user.is_active = is_active

    try:
        db.commit()
        db.refresh(user)

        return user
    except IntegrityError:
        db.rollback()
        raise

def delete_user(
    db: Session,
    user: User
):
    db.delete(user)
    db.commit()

def get_user_by_email(
    db: Session,
    email: str
):
    return db.query(User).filter(
        User.email == email
    ).first()