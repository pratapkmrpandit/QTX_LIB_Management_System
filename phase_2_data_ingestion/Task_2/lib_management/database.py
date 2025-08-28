from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_engine(db_url: str):
    return create_engine(db_url, echo=False, future=True)

def get_session(engine):
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()
