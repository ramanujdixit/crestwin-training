from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import json
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

app = FastAPI(title="Login System")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
Exp = 30


class UserInput(BaseModel):
    username: str
    password: str
    email: str
    phone_no: int


class loginSchema(BaseModel):
    username: str
    password: str


def load_data():
    with open("users.json", "r") as f:
        data = json.load(f)
    return data


def save_data(data):
    with open("users.json", "w") as f:
        json.dump(data, f)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


@app.post("/sign-up")
def signup(new_user: UserInput):
    data = load_data()

    for user in data:
        if user["username"] == new_user.username:
            raise HTTPException(status_code=400, detail="Username already exist")
        if user["email"] == new_user.email:
            raise HTTPException(status_code=400, detail="email id already exist")
    hashed_password = pwd_context.hash(new_user.password)
    new_user_dic = new_user.model_dump()
    new_user_dic["password"] = hashed_password
    data.append(new_user_dic)
    save_data(data)
    return {"message": "new user added"}


@app.post("/login")
def login(user: loginSchema):
    data = load_data()

    for u in data:
        if u["username"] == user.username:

            if not verify_password(user.password, u["password"]):
                raise HTTPException(status_code=401, detail="Unauthorized")

            exp_time = datetime.utcnow() + timedelta(minutes=Exp)

            token = jwt.encode(
                {"username": user.username, "exp": exp_time}, SECRET_KEY, ALGORITHM
            )

            return {"message": "Login Successful", "token": token}

    raise HTTPException(status_code=404, detail="Username not found")
