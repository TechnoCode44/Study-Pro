from fastapi import FastAPI, HTTPException

from json_loader import *

app = FastAPI()

@app.get("/")
def index():
    return "Hello, World!"

@app.get("/database/")
def database(file):
    file_content = load_json(f"Database/{file}")
    
    if file_content == None:
        raise HTTPException(404, "File not found")
    return file_content