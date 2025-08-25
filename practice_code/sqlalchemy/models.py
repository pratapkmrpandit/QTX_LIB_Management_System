# purpose only for understanding of sqlalchemy ORM 

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection (MySQL with PyMySQL driver)
Database_URL = "mysql+pymysql://root:Office%409087@localhost:3306/task_db"

# Create engine and base class
engine = create_engine(Database_URL, echo=True)
Base = declarative_base()

# Define Task model (maps to 'task' table)
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(250), nullable=False)
    status = Column(String(50), default="Pending")

# Create tables in the database
Base.metadata.create_all(engine)

# Session factory for database operations
sessionlocal = sessionmaker(bind=engine)

