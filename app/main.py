from contextlib import asynccontextmanager
from fastapi import FastAPI
# from tortoise import Tortoise


app = FastAPI()

# main_app_lifespan = app.router.lifespan_context

# @asynccontextmanager
# async def lifespan_wrapper(app):
#     print("startup")
#     async with main_app_lifespan(app) as maybe_state:
#         yield maybe_state
#     print("shutdown")

class Item(BaseModel):
    name: str
    price: float



# # Function to be executed during startup
# def startup_event():
#     print("Initializing objects...")
#     # Your initialization code here


# @app.on_event("startup")
# async def startup():
#     startup_event()

# searchengine = pineconeSearch()


@app.get("/search")
async def search(query:str):
    pass
    
    
@app.get("/")
async def read_iteam():
    return {"message": "Welcome to omaai"}

@app.get("/hello/{name}")
async def read_item(name):
    return {"message": f"Hello {name}, how are you?"}

@app.post("/items/")
async def create_item(item:Item):
    return {"message": f"{item.name} is priced at £{item.price}"}