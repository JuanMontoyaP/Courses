# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import status, UploadFile
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, File

app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class PersonBase(BaseModel):
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

class Person(PersonBase):
    password: str = Field(..., min_length=8, example="123456789")

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

class PersonOut(PersonBase):
    pass

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

class LoginOut(BaseModel):
    username: str = Field(..., max_length=20, example="jp2021")
    message: str = Field(default='Successful Login in!')

@app.get(
    path="/",
    status_code=status.HTTP_200_OK
    )
def home(): 
    return {"Hello": "World"}

# Request and Response body
@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED
    )
def create_person(person: Person = Body(...)):
    return person

# Validations: Query Parameters
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK
    )
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
persons = [1, 2, 3, 4, 5]

@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK
    )
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person ID",
        description="This is the person ID",
        example=223
        )
):
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person does not exist!"
        )
    return {person_id: "It exist!"}

# Validations: Request body
@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_202_ACCEPTED
    )
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

# Forms
@app.post(
    path="/loging",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)

# Cookies and Headers
@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK
)
def contact(
    fits_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent

# Files
@app.post(
    path="/post_image"
)
def post_image(
    image: UploadFile = File(...)
):
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    }