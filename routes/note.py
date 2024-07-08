from fastapi import FastAPI, Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc.get("title", ""),
            "desc": doc.get("desc", ""),
            "important": doc.get("important", False),
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/", response_class=HTMLResponse)
async def create_item(request: Request, title: str = Form(...), desc: str = Form(...), important: bool = Form(False)):
    note_data = {
        "title": title,
        "desc": desc,
        "important": important,
    }
    conn.notes.notes.insert_one(note_data)
    return await read_item(request)  # Call read_item to render the template with updated notes
