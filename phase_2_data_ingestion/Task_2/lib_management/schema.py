from pydantic import BaseModel, field_validator
from datetime import date, datetime
from typing import Optional
import re

class AuthorSchema(BaseModel):
    first_name: str
    last_name: str=""
    birth_date: Optional[date] = None
    nationality: Optional[str] = None
    biography: Optional[str] = None

    @field_validator("first_name", "last_name",mode="before")           
    def validate_name(cls, v, info):                           # validate and format names
        if v is None:
            return "" if info.field_name == "last_name" else v  
        return v.strip().title()                            # capitalize each part of the name and remove extra spaces


class BookSchema(BaseModel):
    title: str
    isbn: Optional[str] = None
    publication_date: Optional[date] = None
    total_copies: int
    available_copies: int
    author_id: int

    @field_validator("title")
    def validate_title(cls, v):              # validate title is not empty
        v = v.strip().title()
        if not v:
            raise ValueError("Title cannot be empty")
        return v

    @field_validator("isbn", mode="before")
    def validate_isbn(cls, v):                    # validate isbn format
        if not v:
            return None
        v = v.replace("-", "").strip()
        if not re.match(r"^\d{9}[\dX]$|^\d{13}$", v):
            raise ValueError("Invalid ISBN format")
        return v

    @field_validator("publication_date", mode="before")
    def validate_publication_date(cls, v):              # validate date in multiple formats
        if isinstance(v, str):
            v = v.strip()
            if not v:
                return None
            for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S"):
                try:
                    return datetime.strptime(v, fmt).date()
                except ValueError:
                    continue
            raise ValueError("Invalid date format. Expected YYYY-MM-DD or ISO format.")
        if isinstance(v, datetime):
            return v.date()
        return v

