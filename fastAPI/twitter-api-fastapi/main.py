# Python
from typing import Optional
from uuid import UUID
from datetime import date, datetime

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    firs_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        max_length=256,
        min_length=1
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

@app.get(path="/")
def home():
    return {"Twitter API": "Working"}

if __name__ == "__main__":
   import uvicorn
   uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)