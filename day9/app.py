from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated
import json


app = FastAPI(title="Login Page")


class UserInput(BaseModel):
    email: Annotated[str, Field(..., description="enter your mail id")]
    password: Annotated[str, Field(..., description="enter your password")]


def load_file():
    with open("login_details.json", "r") as f:
        return json.load(f)


def save_data(data):
    with open("login_details.json", "w") as f:
        json.dump(data, f)


@app.get("/")
def home():
    return {"message": "Welcome to Login Page"}


@app.post("/login")
def login(user: UserInput):
    data = load_file()

    for u in data:
        if u["email"] == user.email and u["password"] == user.password:
            return {"message": "Login Successfull"}

    raise HTTPException(status_code=401, detail="Bad Credentials")


@app.post("/signup")
def sign_up(user: UserInput):
    data = load_file()

    new_user = {"email": user.email, "password": user.password}

    for u in data:
        if u["email"] == user.email:
            raise HTTPException(
                status_code=400, detail="User already exists. Please login"
            )
    data.append(new_user)
    save_data(data)
    return JSONResponse(
        status_code=201, content={"message": "user registered successfully"}
    )


@app.put("/update_password/{email}")
def update_password(email: str, update_user: UserInput):
    data = load_file()

    for user in data:
        if user["email"] == email:
            user["email"] = update_user.email
            user["password"] = update_user.password

            save_data(data)
            return JSONResponse(status_code=201, content={"message": "User Updated"})

    raise HTTPException(status_code=404, detail="user not found")


@app.delete("/delete/{email}")
def delete_user(email: str):
    data = load_file()

    for i, user in enumerate(data):
        if user["email"] == email:
            deleted_user = data.pop(i)
            save_data(data)
            return {"message": "user deleted", "user": deleted_user}

    raise HTTPException(status_code=404, content={"message": "user not found"})
