from pydantic import BaseModel

class AddTodo(BaseModel):
    task : str
    completed  : bool = False

class TodoResponse(BaseModel):
    id : int
    task : str
    completed  : bool = False


class UpdateTodo(BaseModel):
    task : str