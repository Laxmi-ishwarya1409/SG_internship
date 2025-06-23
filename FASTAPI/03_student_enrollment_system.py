from sqlmodel import Field
from pydantic import EmailStr,BaseModel

class Student(BaseModel):
    name : str
    email : EmailStr
    age : int = Field(gt=0,lt=7)

class Courses(BaseModel):
    title : str
    code : str
    credits : int = Field(gt=0,lt=7)

class Enrollments(BaseModel):
    pass

# Enrollment

# Links Student and Course

# Optional: Grade