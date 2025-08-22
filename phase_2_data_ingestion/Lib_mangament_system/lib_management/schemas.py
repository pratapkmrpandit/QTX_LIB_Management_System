# schemas code for validation 
from pydantic import BaseModel, EmailStr , validator
from datetime import datetime
import re

class LibrarySchema(BaseModel):
    name: str
    campus_loaction:str
    contact_email:EmailStr
    phone_number:str

    @validator('name','campus_loaction')    # validating and normalizing text fields
    def normalize_text(cls,v):
        return v.strip().title()
    
    @validator('phone_number')
    def validate_phone(cls,v):
        digits=re.sub(r'\D','',v)     # removing non digit characters
        if len(digits)<10 or len(digits)>15:   # checking length if it is not valid raise error
            raise ValueError("Invalid phone number")
        return f"+1-{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:]}"   # formatting to standard format (us format)


class BookSchema(BaseModel):
    title:str
    isbn:str
    publication_date:str
    total_copies:int
    available_copies:int
    library_id:int

    @validator('isbn')
    def clear_isbn(cls,v):
        return v.replace('-','').strip()   # removing hyphens and spaces

    @validator('publication_date',pre=True)
    def parse_date(cls,v):
        try:
            return datetime.strptime(v,'%Y-%m-%d').date()  # parsing date from string
        except :
            raise ValueError("Invalid formate")

class AuthorSchema(BaseModel):
    first_name:str
    last_name:str
    birth_date:str
    nationality:str
    biography:str

    @validator('birth_date',pre=True)
    def parse_birth_date(cls,v):
        try:
            return datetime.strptime(v,'%Y-%m-%d').date()  # parsing date from string
        except :
            raise ValueError("Invalid date formate")

class MemberSchema(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    phone:str
    member_type:str
    registration_date:str

    @validator('phone')
    def validate_phone(cls,v):
        digits=re.sub(r'\D','',v)
        if len(digits)<10 or len(digits)>15:
            raise ValueError("Invalid phone number")
        return f"+1-{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:]}"
    
    @validator('registration_date',pre=True)
    def parse_registration_date(cls,v):
        return datetime.strptime(v,'%Y-%m-%d').date()  # parsing date from string