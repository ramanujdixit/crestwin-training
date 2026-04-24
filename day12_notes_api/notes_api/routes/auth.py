from fastapi import APIRouter, Depends
from models.user_model import UserInput
from utils.file_handling import load_file, save_data

router = APIRouter()


@router.post("/create")
def create_notes(note: UserInput, data=Depends(load_file)):
    # data = load_file()
    new_note = {
        "id": note.id,
        "title": note.title,
        "author_name": note.author_name,
        "notes": note.notes,
    }
    data.append(new_note)
    save_data(data)

    return {"message": "note added", "note": new_note}
