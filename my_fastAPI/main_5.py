from typing import List, Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# Define a submodel
class Image(BaseModel):
    # special types and validation
    url: HttpUrl
    name: str

# List fields
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # tags: List[str] = []
    tags: Set[str] = ()
    # Use the submodel as a type
    image: Optional[Image] = None

'''    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results'''

# List fields with type parameter

# Set types
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results



