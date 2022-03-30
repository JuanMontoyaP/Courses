# Python
import json
from typing import Optional, List
from uuid import UUID
from datetime import date, datetime

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import status, HTTPException
from fastapi import Body, Path

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="Juan19980319*"
    )

class User(UserBase):
    firs_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Juan"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Montoya"
    )
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User, UserLogin):
    pass

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

# Path Operations

## Users

### Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Signup
    
    This path operations registers a user in the app

    Parameters:
        - Request body parameter
            - user: UserRegister
    
    Returns a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - firs_name: str
        - last_name: str
        _ birth_date: date
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        json.dump(results, f)
        return user

### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    """
    Show all users

    This path operation shows all users in the app

    Parameters:
        -
    
    Returns a json list with all users in the app, whit the following keys
        - user_id: UUID
        - email: EmailStr
        - firs_name: str
        - last_name: str
        _ birth_date: date
    """

    with open("users.json", "r", encoding="utf-8") as f:
        result = json.load(f)
        return result

### Show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user(
    user_id: UUID = Path(
        ...,
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        title="User ID",
        description="This is the user_id for each person"
        )
    ):
    """
    Show a user

    This path operation shows the user with user_id

    Parameters:
        - user_id: UUID

    Returns a json with the user
        - user_id: UUID
        - email: EmailStr
        - firs_name: str
        - last_name: str
        _ birth_date: date
    """
    with open("users.json", "r", encoding="utf-8") as f:
        result = json.load(f)
        for person in result:
            if str(person["user_id"]) == str(user_id):
                return person

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person does not exist!"
        )

### Delete a user
@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user(
    user_id: UUID = Path(
        ...,
        title="User ID",
        description="This is the user id you want to delete",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa7"
    )
):
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        for i in range(len(results)):
            if str(results[i]["user_id"]) == str(user_id):
                person = results[i]
                results.pop(i)
                f.truncate(0)
                f.seek(0)
                json.dump(results, f)
                return person
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person does not exist!"
        )

### Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass

## Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home():
    """
    This path operation shows all tweets in the app

    Parameters:
        -
    
    Returns a json list with all tweets in the app, whit the following keys
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """

    with open("tweets.json", "r", encoding="utf-8") as f:
        result = json.load(f)
        return result

### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post(tweet: Tweet = Body(...)):
    """
    Post a tweet
    
    This path operations post a tweet in the app

    Parameters:
        - Request body parameter
            - tweet: Tweet
    
    Returns a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        result = json.load(f)
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])

        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])

        result.append(tweet_dict)
        f.seek(0)
        json.dump(result, f)
        return tweet

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass

if __name__ == "__main__":
   import uvicorn
   uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)

# Ret -- Create all the path operations