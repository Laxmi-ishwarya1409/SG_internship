from fastapi import APIRouter, HTTPException, status, Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas import AddTodo, UpdateTodo, TodoResponse
from models import Todo
from typing import List

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message":"Welcome to todo router"}


@router.post("/add_todo", response_model=TodoResponse)
async def add_todo(todo : AddTodo, db : Session = Depends(get_db)):
    # new_todo = Todo(task=todo.task,completed = todo.completed)
    new_todo = Todo(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    return new_todo


@router.get("/todos",response_model=List[TodoResponse])
async def get_todos(db : Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos


@router.get("/get_single_todo/{id}",response_model=TodoResponse)
async def get_single_todo(id: int, db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="Todo not Found")
    return todo


@router.patch("/update_todo/{id}",response_model=TodoResponse)
async def get_single_todo(id: int,updatedtodo: UpdateTodo, db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="Todo not Found")
    todo.task = updatedtodo.task
    db.commit()
    return todo

@router.delete("/todos/{id}")
async def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": f"Todo with id {id} deleted"}