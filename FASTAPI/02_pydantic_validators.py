
# # Basic Validation

# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int


# user1 = User(name="Alice", age=30)
# user2 = User(name="Bob", age="not a number")






# # Add Field Constraints

# from pydantic import BaseModel, Field

# class Product(BaseModel):
#     name: str = Field(..., min_length=2)
#     price: float = Field(..., gt=0)

# product = Product(name="Book", price=9.99)
# product = Product(name="A", price=0)





class PriceMustBeGreaterThanZero(Exception):
    pass

from pydantic import BaseModel , Field, field_validator
class Item(BaseModel):
    name : str = Field(min_length=2)
    price : int
    quantity : int

    @field_validator("price")
    @classmethod
    def check_price(cls,value):
        if value <= 0:
            raise PriceMustBeGreaterThanZero("Price must be greater than zero")
        else:
            return value

item1 = Item(name="Laptop",price=0,quantity = 5)





from fastapi import FastAPI
from pydantic import BaseModel, model_validator
from datetime import date

app = FastAPI()

class Event(BaseModel):
    title: str
    start_date: date
    end_date: date
    @model_validator(mode='after')
    def validate_dates(self) -> "Event":
        if self.start_date >= self.end_date:
            raise ValueError("start_date must be before end_date")
        return self
    
@app.post("/events/")
def create_event(event: Event):
    return {"message": "Event created successfully!", "event": event}







from pydantic import BaseModel, model_validator

class Pair(BaseModel):
    a: int
    b: int

    @model_validator(mode='before')
    @classmethod
    def swap_if_needed(cls, values):
        a = values.get('a')
        b = values.get('b')
        if a is not None and b is not None and a > b:
            # Swap a and b to maintain a < b
            values['a'], values['b'] = b, a
        return values
    

p1 = Pair(a=111,b=12)
print(p1)



# def __repr__(self):
#     return f"{self.__class__.__name__}({', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})"
