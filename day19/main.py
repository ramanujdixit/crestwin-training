from fastapi import FastAPI, Depends
from db import Base, engine, get_db
from model import User
from schemas import UserCreate, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

app = FastAPI()


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def home():

    return {"message": "PostgreSQL Connected Successfully"}


@app.post("/users")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@app.get("/users")
async def get_all_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))

    users = result.scalars().all()

    return users
