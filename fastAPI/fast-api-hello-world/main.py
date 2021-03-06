# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="Facundo"
        )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="Torres"
        )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=22
    )
    email: EmailStr = Field(..., example="fac@gmail.com")
    hair_color: Optional[HairColor] = Field(default=None, example="black")
    is_married: Optional[bool] = Field(default=None, example=False)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Facundo",
    #             "last_name": "Garcia",
    #             "age": 21,
    #             "email": "fac@gmail.com",
    #             "hail_color": "blonde",
    #             "is_married": False
    #         }
    #     }

class Location(BaseModel):
    city: str = Field(
        ...,
        max_length=50,
        min_length=1,
        example="Medellin"
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Antioquia"
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Colombia"
    )

@app.get("/")
def home():
    return {"Hello": "World"}

# Request and Response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

# Validations: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name. It is between 1 and 50 chars",
        example="Juan"
        ),
    age: int = Query(
        ...,
        title="Person Age",
        description="This is the person age. It is required",
        example=22
        )
):
    return {name: age}

# Validations: Path parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person ID",
        description="This is the person ID",
        example=223
        )
):
    return {person_id: "It exist!"}

# Validations: Request body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0,
        example=123
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    # person.dict() & location.dict()
    return results