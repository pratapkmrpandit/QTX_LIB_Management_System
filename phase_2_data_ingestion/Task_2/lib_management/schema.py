from pydantic import BaseModel, field_validator
from datetime import date, datetime
from typing import Optional
import re

class AuthorSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
    nationality: Optional[str] = None
    biography: Optional[str] = None

    @field_validator("first_name", "last_name")
    def validate_name(cls, v):
        return v.strip().title()


class BookSchema(BaseModel):
    title: str
    isbn: Optional[str] = None
    publication_date: Optional[date] = None
    total_copies: int
    available_copies: int
    author_id: int

    @field_validator("title")
    def validate_title(cls, v):
        return v.strip().title()

    @field_validator("isbn", mode="before")
    def validate_isbn(cls, v):
        if not v:  # Allow None
            return None
        v = v.replace("-", "").strip()
        if not re.match(r"^\d{10}(\d{3})?$", v):
            raise ValueError("Invalid ISBN format")
        return v

    @field_validator("publication_date", mode="before")
    def validate_publication_date(cls, v):
        if not v:
            return None
        try:
            if isinstance(v, str):
                return datetime.datetime.strptime("%Y-%m-%d")
            datetime.datetime.strptime(v, "%Y-%m-%d")  
            return v
        except ValueError:
            raise ValueError("Invalid date format, expected YYYY-MM-DD")
        return None
