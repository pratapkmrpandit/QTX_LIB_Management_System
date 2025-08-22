from sqlalcehmy import Column, Integer, String, ForeignKey,Date,func
from sqlalchemy.orm import relationship,declarative_base

Base=declarative_base()

class Library(Base):
    __tablename__="Libraries"
    library_id=Column(Integer,primary_key=True)
    name =Column(String(100),nullable=False)
    campus_location=Column(String(100))
    contact_email=Column(String(100),nullable=False,unique=True)
    phone_number=Column(String(15))
    created_at=Column(DateTime,default=func.now())
    updated_at=Column(DateTime,default=func.now(),onupdate=func.now())
    books = relationship("Book", back_populates="library")

class Book(Base):
    __tablename__="Books"
    book_id=Column(Integer,primary_key=True)
    title=Column(String(50),nullable=False)
    isbn=Column(String(30),unique=True , nullable=False)
    publication_date=Column(DateTime)
    total_copies=Column(Integer)
    available_copies=Column(Integer)
    library_id = Column(Integer, ForeignKey('libraries.library_id'))
    created_at=Column(DateTime,default=func.now())
    updated_at=Column(DateTimee,default=func.now(),onupdate=func.now())
    
    library = relationship("Library", back_populates="books")


class Member(Base):
    __tablename__="Members"
    member_id=Column(Integer,primary key=True )
    first_name=Column(String(100),nullable=False)
    last_name=Column(String(100),nullable=False)
    email=Column(String(100),nullable=False)
    phone=Column(String(15))
    member_type=Column(String(50))
    registration_date=Column(DateTime)
    created_at=Column(DateTime,default=func.now())
    updated_at=Column(DateTime,default=func.now(),onupdate=func.now())

class Author(Base):
    __tablename__="Authors"
    author_id=Column(Integer,primary_key=True)
    first_name=Column(String(100),nullable=False)
    last_name=Column(String(100),nullable=False)
    birth_date=Column(DateTime)
    nationality=Column(String(100))
    biography=Column(String(500))
    created_at=Column(DateTime,default=func.now())
    updated_at=Column(DateTime,default=func.now(),onupdate=func.now())
    