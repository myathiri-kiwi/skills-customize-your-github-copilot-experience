# Starter code for FastAPI REST API assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: str = ""

items: List[Item] = []

@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the FastAPI assignment!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# CRUD endpoints for Item
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(items):
        if item.id == item_id:
            items[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, item in enumerate(items):
        if item.id == item_id:
            del items[idx]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

# To run: uvicorn starter-code:app --reload
