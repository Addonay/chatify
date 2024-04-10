from uuid import uuid4
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    # id = Column(String, primary_key=True, default=uuid4())
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    profile_image = Column(String)
    
    def __repr__(self) -> str:
        return f"{self.email}"
    
