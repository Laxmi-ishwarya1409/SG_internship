from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlmodel import SQLModel, Relationship, create_engine, Session, select
from sqlalchemy import Field
from pydantic import EmailStr
from datetime import date
from typing import List
from enum import Enum

class LeaveStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class User(SQLModel, table=True):
    id : int = Field(primary_key=True)
    name : str
    email : EmailStr
    role : str
    leave_balance : int = Field(default=20)

    leaves : list["Leave"] = Relationship(back_populates="user")

class Leave(SQLModel, table=True):
    id : int = Field(primary_key=True)
    start_date : date
    end_date : date
    reason : str
    status: LeaveStatus = Field(default=LeaveStatus.pending)

    user_id : int = Field(foreign_key="user.id")
    user : User = Relationship(back_populates="leaves")



class UserCreate(BaseModel):
    name : str
    email : EmailStr
    role : str


class UserRead(BaseModel):
    id : int
    name : str
    email : EmailStr
    role : str
    leave_balance : int

class LeaveCreate(BaseModel):
    start_date : date
    end_date : date
    reason : str
    user_id : int

class LeaveRead(BaseModel):
    id: int
    start_date: date
    end_date: date
    reason: str
    status: LeaveStatus
    user_id: int


engine = create_engine("sqlite:///leave_db.db")

app = FastAPI()

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()


@app.post("/create_user",response_model=UserRead)
def create_user(user:UserCreate):
    db_user = User(**user.model_dump())
    with Session(engine) as session:
        session.add(db_user)
        session.commit()
        return db_user
    
@app.get("/get_all_users",response_model=List[UserRead])
def get_users():
    with Session(engine) as session:
        users = session.exec(select(User))
        return users.all()
    

@app.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id:int, user_data:UserCreate):
    with Session(engine) as session:
        user = session.get(User,user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        for i,j in user_data.model_dump().items():
            setattr(user,i,j)
        session.commit()
        return user


@app.delete("/delete_user/{user_id}")
def delete_user(user_id : int):
    with Session(engine) as session:
        user = session.get(User,user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        session.delete(user)
        session.commit()
        return {"message":f"{user_id} deleted succesfully"}
    



@app.post("/leave/apply",response_model=LeaveRead)
def apply_leave(leave_data:LeaveCreate):
    with Session(engine) as session:
        user = session.get(User, leave_data.user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        leave_days = (leave_data.end_date - leave_data.start_date).days + 1
        if leave_days > user.leave_balance:
            raise HTTPException(status_code=status.HTTP_400_NOT_FOUND, detail="Insufficient leave balance")
        
        db_leave = Leave(**leave_data.model_dump())
        session.add(db_leave)
        session.commit()
        return db_leave
    

@app.get("/leave/", response_model=List[LeaveRead])
def get_leaves(user_id: int = None, status: str = None):
    with Session(engine) as session:
        query = select(Leave)
        if user_id:
            query = query.where(Leave.user_id == user_id)
        if status:
            query = query.where(Leave.status == status)
        leaves = session.exec(query).all()
        return leaves


@app.put("/leave/{leave_id}/approve", response_model=LeaveRead)
def approve_leave(leave_id: int):
    with Session(engine) as session:
        leave = session.get(Leave, leave_id)
        if not leave:
            raise HTTPException(status_code=404, detail="Leave not found")
        if leave.status != LeaveStatus.pending:
            raise HTTPException(status_code=400, detail="Leave already processed")
        
        user = session.get(User, leave.user_id)
        leave_days = (leave.end_date - leave.start_date).days + 1
        if leave_days > user.leave_balance:
            raise HTTPException(status_code=400, detail="Insufficient leave balance")
        
        leave.status = LeaveStatus.approved

        
        user.leave_balance -= leave_days
        session.commit()
        return leave
    


@app.put("/leave/{leave_id}/reject", response_model=LeaveRead)
def reject_leave(leave_id: int):
    with Session(engine) as session:
        leave = session.get(Leave, leave_id)
        if not leave:
            raise HTTPException(status_code=404, detail="Leave not found")
        if leave.status != "pending":
            raise HTTPException(status_code=400, detail="Leave already processed")
        
        leave.status = LeaveStatus.rejected
        session.commit()
        return leave



@app.get("/leave/{user_id}/balance")
def leave_balance(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user_id": user.id, "leave_balance": user.leave_balance}
