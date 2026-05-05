from pydantic import BaseModel


class StudentCreate(BaseModel):
    id: int
    name: str
    roll_no: int


class StudentUpdate(BaseModel):
    name: str
    roll_no: int
