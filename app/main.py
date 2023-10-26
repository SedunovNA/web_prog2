from typing import Union

from fastapi import FastAPI
from app.routes import router
#add import
from app.models import Book
from app.config import engine
# Book.metadata.create_all(bind=engine)


app = FastAPI()
    


#define endpoint
@app.get("/")
def home():
    return "HALLO"



app.include_router(router, prefix="/book", tags=["book"])