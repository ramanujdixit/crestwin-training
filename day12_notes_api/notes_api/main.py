from fastapi import FastAPI, Depends, HTTPException, Query
from utils.file_handling import load_file, save_data
from routes import auth, user

import json


app = FastAPI(title="Notes API")


@app.get("/")
def home():
    return {"message": "Welcome to Notes API"}


@app.get("/all-notes")
def all_notes(data=Depends(load_file)):
    return data


@app.get("/notes/{note_id}")
def get_note(note_id: int, data=Depends(load_file)):
    for note in data:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="note not found")


@app.get("/notes")
def search_notes(
    author_name: str = Query(..., description="give author name to find note"),
    data=Depends(load_file),
):
    collected_notes = []
    for note in data:
        if note["author_name"] == author_name:
            collected_notes.append(note)

    if not collected_notes:
        raise HTTPException(status_code=404, detail="Author not found")

    return collected_notes


app.include_router(auth.router)
app.include_router(user.router)
