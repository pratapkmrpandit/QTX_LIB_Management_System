from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_engine(db_url: str):                               # create and return a new engine
    return create_engine(db_url, echo=False, future=True)

def get_session(engine):                                        # create and return a new session
    SessionLocal = sessionmaker(bind=engine) 
    return SessionLocal()
