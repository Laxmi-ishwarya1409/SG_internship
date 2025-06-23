from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator


app = FastAPI()

# Pydantic model to define the structure and validation of the request body
class Item(BaseModel):
    name: str = Field(min_length=3)  
    price: float  
    quantity: int 

    # Custom validator to ensure price is greater than 0
    @field_validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        return value


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/search/")
def search_item(q: str = None):
    return {"query": q}


@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item received", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}