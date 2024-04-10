import os
from models.models import Base
from utils.config import Settings
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class Database:
    database_url = f"sqlite:///{os.path.join('db', 'db.sqlite3')}"
    # database_url = Settings().db_url
    def __init__(self):
        self.engine = create_engine(self.database_url, echo=True)
        self.connection = self.engine.connect()
        self.SessionLocal = scoped_session(sessionmaker(bind=self.engine, autoflush=False, autocommit=False))
    
    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)
        
    def create_table(self, model):
        metadata = MetaData()
        model.metadata.create_all(bind=self.engine)
        
    def get_session(self):
        return self.SessionLocal
    
    def close_session(self):
        self.SessionLocal.close()
        