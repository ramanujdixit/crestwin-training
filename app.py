from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import engine, SessionLocal
import model

model.base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = model.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(model.User).all()
