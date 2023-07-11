from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from json_loader import *

from os.path import isfile

app = FastAPI()
app.mount("/audio", StaticFiles(directory="Audio"), name="Audio")

@app.get("/")
def index():
    return "Hello, World!"

@app.get("/database/")
def database(file):
    file_content = load_json(f"Database/{file}")
    
    if file_content == None:
        raise HTTPException(404, "File not found")
    return file_content

@app.get("/audio")
def audio(course: str, question_number: int):
    path = f"Audio/{course}/Q{question_number}.mp3"
    audio_exists = isfile(path)

    if audio_exists:
        request_path = f"/audio/{course}/Q{question_number}.mp3" # Single letter change then "path" variable
        return request_path
    else:
        raise HTTPException(404, "File not found")