from fastapi import FastAPI

from json_loader import *

app = FastAPI()

@app.get("/")
def index():
    return "Hello, World!"