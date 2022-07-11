from fastapi import APIRouter, HTTPException, status

from app.models import Note

router = APIRouter(tags=["notes"])
notes = dict()

@router.get("/notes/{note_id}")
async def get_note(note_id):
    if note := notes.get(note_id):
        return {"message": "success", "text": note, "id": note_id}
    else:
        raise HTTPException(status_code=404, detail="Note does not exist")

@router.post("/notes", status_code=status.HTTP_201_CREATED)
async def post_note(note: Note):
    if not note.id in notes:
        notes[note.id] = note.text
        return {"message": "success"}
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Note already exists")

@router.delete("/notes", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note: Note):
    if note.id in notes:
        del notes[note.id]
        return {"message": "success"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note does not exist")

@router.put("/notes")
async def update_note(note: Note):
    if note.id in notes:
        notes[note.id] = note.text
        return {"message": "success"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note does not exist")