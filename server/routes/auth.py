from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.dbfuncs import get_db
from models.models import User
from models.schema import UserRegister

router = APIRouter(prefix = "/auth", tags = ["Auth"])

@router.post("/register",status_code=status.HTTP_200_OK)
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")
        else:  
            user_data = user.model_dump()
            new_user = User(**user_data)
            db.add(new_user)
    finally:
        db.commit()
    
    return user_data