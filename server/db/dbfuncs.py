from db.database import Database
from models.models import User

def get_db(): 
    db = Database()
    try:
        db.create_table(User)
        yield db.get_session()
    finally:
        db.close_session()