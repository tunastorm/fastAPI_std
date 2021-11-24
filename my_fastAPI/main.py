from typing import Optional
from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


fake_items_db = [{"item_name":"Foo"}, {"item_name":"Bar"}, {"item_name":"Baz"}]

app = FastAPI()

@app.get("/models/{model_name}") # receives HTTP requests
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message":"Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

'''
@app.get("/items/{item_id}") # receives HTTP requests
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
'''

@app.get("/users/{user_id}/items/{item_id}") # receives HTTP requests
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id":user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit":limit}
    return item

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

'''
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_rax": price_with_tax})
    return item_dict
'''

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q":q})
    return result

@app.get("/items/")
async def read_items(q: Optional[str] = Query('item', min_length=3, max_length=50, regex="^item$")):
    results = {"items": [{"item_id":"Foo"}, {"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results


