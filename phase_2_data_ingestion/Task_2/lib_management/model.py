from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Author(Base):
    __tablename__ = 'author'

    author_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)
    birth_date = Column(Date, nullable=True)
    nationality = Column(String(100), nullable=True)
    biography = Column(String(500), nullable=True)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")    # relationship with Book

    def __repr__(self):
        return f"<Author(name='{self.first_name} {self.last_name}')>"     # representation of the author object

class Book(Base):
    __tablename__ = 'book'

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(225), nullable=False)
    isbn = Column(String(30), nullable=True, unique=True)
    publication_date = Column(Date, nullable=True)
    total_copies = Column(Integer, nullable=True)
    available_copies = Column(Integer, nullable=True)
    author_id = Column(Integer, ForeignKey('author.author_id'), nullable=False)

    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Book(title='{self.title}', isbn='{self.isbn}')>"      # representation of the book object
