from pydantic import BaseModel, EmailStr, UUID4
from typing import Optional, List
import datetime

# Pydantic schema for User
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_privileged: Optional[bool] = False

class User(BaseModel):
    id: UUID4
    first_name: str
    last_name: str
    email: EmailStr
    is_privileged: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_login: Optional[datetime.datetime]
    passwords: List['Password'] = []

    class Config:
        from_attributes = True

# Pydantic schema for Password
class PasswordCreate(BaseModel):
    content: str
    user_id: UUID4
    title: str
    username: Optional[str] = None
    url: Optional[str] = None

class Password(BaseModel):
    id: UUID4
    content: str
    user_id: UUID4
    title: str
    username: Optional[str] = None
    url: Optional[str] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user: User

    class Config:
        from_attributes = True
