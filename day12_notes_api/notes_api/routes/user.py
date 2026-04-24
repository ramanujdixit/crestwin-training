from fastapi import APIRouter, Depends, HTTPException
from models.user_model import UserInput
from utils.file_handling import load_file, save_data


router = APIRouter()


@router.put("/update_note/{note_id}")
def update_note(note_to_update: UserInput, note_id: int, data=Depends(load_file)):
    for note in data:
        if note["id"] == note_id:
            note["id"] = note_to_update.id
            note["title"] = note_to_update.title
            note["author_name"] = note_to_update.author_name
            note["notes"] = note_to_update.notes

            save_data(data)
            return {"message": "Task updated", "task": note}

    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/delete-note/{note_id}")
def delete_note(note_id: int, data=Depends(load_file)):
    for i, note in enumerate(data):
        if note["id"] == note_id:
            deleted_note = data.pop(i)
            save_data(data)
            return {"message": "Noted deleted Successfully", "note": deleted_note}
    raise HTTPException(status_code=404, detail="Note not found")
