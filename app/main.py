from pydantic import BaseModel
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request,Query
from app.pinecone_search import pineconeSearch
from app.Document import Document
from typing import List

@asynccontextmanager
async def lifespan(application: FastAPI):
    global searchengine
    searchengine = pineconeSearch()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/search")
async def search(query: str = Query(..., min_length=1)) -> List[Document]:
    if searchengine is None:
        raise ValueError("Search engine not initialized")
    else:
        print("find searchengine")
        return searchengine.search(query)
    

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
async def root(request: Request):
    return {"message": "this is the root"}
    # return {"secret": request.app.state.super_secret}


@app.get("/hello/{name}")
async def read_item(name):
    return {"message": f"Hello {name}, how are you?"}

@app.post("/items/")
async def create_item(item:Item):
    return {"message": f"{item.name} is priced at £{item.price}"}