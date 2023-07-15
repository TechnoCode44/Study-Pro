from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from json_loader import *
from audio import save_audio

from os.path import isfile

app = FastAPI()

@app.get("/")
async def index():
    return "Hello, World!"

@app.get("/database/{file}")
async def database(file):
    file_content = load_json(f"Database/{file}.json")
    
    if file_content == None:
        raise HTTPException(404, "File not found")
    return file_content

@app.get("/audio/course/{course}/{question_number}")
async def audio(course: str, question_number: int):
    path = f"Audio/{course}/Q{question_number}.mp3"
    audio_exists = isfile(path)

    if audio_exists:
        return FileResponse(path)
    else:
        raise HTTPException(404, "File not found")
    
@app.get("/audio/word/{word}")
async def word(word: str):
    word = word.lower()
    path = f"Audio/Words/{word}.mp3"
    audio_exists = isfile(path)

    if not audio_exists: # Should be POST request
        save_audio(word, "Words", word)
    
    return FileResponse(path)