from pydantic import BaseModel, Field


class UserInput(BaseModel):
    id: int
    title: str = Field(..., description="title of the note")
    author_name: str = Field(..., description="give author name")
    notes: str = Field(..., description="body of note")
