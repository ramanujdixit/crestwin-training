from sqlalchemy import Column, Integer, String
from db import Base


class User(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    roll_no = Column(Integer)
    email = Column(String)
