from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    password: str

class UserUpdate(BaseModel):
    name: str
    email: str
    age: int
    is_active: bool

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }
