from pydantic import BaseModel, field_validator, EmailStr
from typing import Optional
from datetime import datetime
import re

# ---------- Library Schema ----------
class LibrarySchema(BaseModel):
    library_id: int
    name: str
    campus_location: str
    contact_email: EmailStr
    phone_number: str

    # Normalize text fields
    @field_validator("name", "campus_location")
    def normalize_text(cls, v):
        return v.strip().title()

    # Validate and format phone number
    @field_validator("phone_number")
    def validate_phone(cls, v):
        digits = re.sub(r"\D", "", v)
        if len(digits) < 10:
            raise ValueError("Invalid phone number")
        return f"+1-{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:]}"


# ---------- Book Schema ----------
class BookSchema(BaseModel):
    book_id: int
    title: str
    isbn: str
    publication_date: str  # Will validate format
    total_copies: int
    available_copies: int
    library_id: int

    # Normalize title
    @field_validator("title")
    def normalize_title(cls, v):
        return v.strip().title()

    # Validate ISBN
    @field_validator("isbn")
    def validate_isbn(cls, v):
        if not re.match(r"^\d{10}(\d{3})?$", v.replace("-", "")):
            raise ValueError("Invalid ISBN format")
        return v

    # Validate and format date (YYYY-MM-DD)
    @field_validator("publication_date")
    def validate_pub_date(cls, v):
        try:
            # If input is already a date object, convert to string
            if isinstance(v, datetime):
                return v.strftime("%Y-%m-%d")
            datetime.strptime(v, "%Y-%m-%d")
            return v
        except ValueError:
            raise ValueError("Invalid date format, expected YYYY-MM-DD")


# ---------- Author Schema ----------
class AuthorSchema(BaseModel):
    author_id: int
    first_name: str
    last_name: str
    birth_date: str  # Will validate format
    nationality: str
    biography: Optional[str] = None

    # Normalize name fields
    @field_validator("first_name", "last_name", "nationality")
    def normalize_text(cls, v):
        return v.strip().title()

    # Validate birth date
    @field_validator("birth_date")
    def validate_birth_date(cls, v):
        try:
            if isinstance(v, datetime):
                return v.strftime("%Y-%m-%d")
            datetime.strptime(v, "%Y-%m-%d")
            return v
        except ValueError:
            raise ValueError("Invalid date format, expected YYYY-MM-DD")


# ---------- Member Schema ----------
class MemberSchema(BaseModel):
    member_id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    member_type: str  # student or faculty
    registration_date: str  # Will validate format

    # Normalize name
    @field_validator("first_name", "last_name")
    def normalize_name(cls, v):
        return v.strip().title()

    # Validate member type
    @field_validator("member_type")
    def validate_member_type(cls, v):
        if v.lower() not in ["student", "faculty"]:
            raise ValueError("member_type must be 'student' or 'faculty'")
        return v.lower()

    # Validate phone number
    @field_validator("phone")
    def validate_phone(cls, v):
        digits = re.sub(r"\D", "", v)
        if len(digits) < 10:
            raise ValueError("Invalid phone number")
        return f"+1-{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:]}"

    # Validate registration date
    @field_validator("registration_date")
    def validate_registration_date(cls, v):
        try:
            if isinstance(v, datetime):
                return v.strftime("%Y-%m-%d")
            datetime.strptime(v, "%Y-%m-%d")
            return v
        except ValueError:
            raise ValueError("Invalid date format, expected YYYY-MM-DD")
