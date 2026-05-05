from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import SessionLocal, engine
import model
from schemas import StudentCreate, StudentUpdate

# model.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Hello! Welcome home"}


@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(model.User).filter(model.User.id == student.id).first()

    if existing:
        raise HTTPException(status_code=400, detail="Student already exists")

    new_student = model.User(id=student.id, name=student.name, roll_no=student.roll_no)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(model.User).all()


@app.get("/students/{student_id}")
def find_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(model.User).filter(model.User.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="student not found"
        )
    return student


@app.put("/students/{student_id}")
def update_student(student_id: int, data: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(model.User).filter(model.User.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="student not found"
        )

    student.name = data.name
    student.roll_no = data.roll_no

    db.commit()
    db.refresh(student)

    return student


@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(model.User).filter(model.User.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="student not found"
        )

    db.delete(student)
    db.commit()
    return {"message": "student deleted successfully"}
