from fastapi import FastAPI
from utils import information

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello():
    return {"message": "Hello!"}

@app.get("/entries/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/numeric_items/{item_id}")
def read_numeric_item(item_id: int):
    return {"item_id" : item_id}

@app.get("/info")
async def info():
    return information


@app.get("/status")
async def status():
    print(info)
    return {"Alive!, All systems go."}


