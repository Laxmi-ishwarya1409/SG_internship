from fastapi import FastAPI, HTTPException, status
from sqlmodel import SQLModel, Field, Relationship, create_engine, Session, select, selectinload
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column
from enum import Enum
from datetime import date
from sqlalchemy.types import Enum as SqlEnum
from typing import List

class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

# SQLMODELS
class User(SQLModel,table=True):
    id : int = Field(default=None, primary_key=True)
    name : str
    email : EmailStr

    tasks : list["Task"] = Relationship(back_populates="user")

class Task(SQLModel,table=True):
    id : int = Field(default=None, primary_key=True)
    title : str
    description: str
    due_date : date
    status : Status = Field(sa_column=Column(SqlEnum(Status)),nullable=False)

    user_id : int = Field(foreign_key="user.id")

    user: User = Relationship(back_populates="tasks")


# PYDANTIC MODELS
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

class UserCreate(BaseModel):
    name : str
    email : EmailStr

class TaskCreate(BaseModel):
    title : str
    description : str
    due_date : date
    status : Status
    user_id : int

class TaskRead(BaseModel):
    title : str
    description : str
    status : Status
    due_date : date
    user: UserRead



# database setup
engine = create_engine("sqlite:///task_db.db")

# creating database tables and creating fastapi app
app = FastAPI()
def init_db():
    SQLModel.metadata.create_all(engine)

init_db()


# User model CRUD
@app.post("/add_user", response_model=UserRead)
def create_user(user:UserCreate):
    db_user = User(*user.model_dump())   
    with Session(engine) as session:
        session.add(db_user)
        session.commit()
        return db_user
    
@app.get("/get_user",response_model=List[UserRead])
def get_user():
    with Session(engine) as session:
        result = session.exec(select(User))
        return result.all()
    

@app.put("/update_user/{user_id}",response_model=UserRead)
def update_user(user_id : int,user_data: UserCreate):
    with Session(engine) as session:
        modify_user = session.get(User,user_id)

        if not modify_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        for i,j in user_data.model_dump().items():
            setattr(modify_user, i, j)

        session.commit()
        return modify_user
    

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    with Session(engine) as session:
        user_delete = session.get(User, user_id)
        if not user_delete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        session.delete(user_delete)
        session.commit()
        return {"message": "User deleted successfully"}
    




# Task crud
@app.post("/add_task",response_model=TaskRead)
def add_task(create_task: TaskCreate):
    db_task = Task(**create_task.model_dump())
    with Session(engine) as session:
        session.add(db_task)
        session.commit()
        return db_task
    




@app.get("/get_task",response_model=List[TaskRead])
def get_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(Task).options(selectinload(Task.user))).all()
        return tasks

    

@app.put("/update_task/{task_id}",response_model=TaskRead)
def update_task(task_id : int,task_data: TaskCreate):
    with Session(engine) as session:
        modify_task = session.get(Task,task_id)

        if not modify_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        
        for i,j in task_data.model_dump().items():
            setattr(modify_task, i, j)

        session.commit()
        return modify_task
    

@app.delete("/delete_task/{task_id}")
def delete_task(task_id: int):
    with Session(engine) as session:
        task_delete = session.get(Task, task_id)
        if not task_delete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
        session.delete(task_delete)
        session.commit()
        return {"message": "Task deleted successfully"}