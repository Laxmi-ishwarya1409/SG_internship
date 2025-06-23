from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True)
    task= Column(String)
    completed = Column(Boolean,default=False)
