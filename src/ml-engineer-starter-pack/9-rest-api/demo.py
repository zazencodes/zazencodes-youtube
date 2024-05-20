from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    x: float
    y: float


app = FastAPI()


@app.get("/version")
async def version():
    return {"version": "0.1"}


@app.post("/add")
async def add(item: Item):
    return {"result": item.x + item.y}
