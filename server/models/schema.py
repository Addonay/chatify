from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserLogin(BaseModel):
    email: EmailStr = Field(unique = True)
    
class UserRegister(UserLogin):
    username: Optional[str]
    password: Optional[str]
    profile_image: str