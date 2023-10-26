from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas import BookSchema, Response, RequestBook

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)


@router.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _books = crud.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_books)


@router.get("/{id}")
async def get_book_by_id(id: int, db: Session = Depends(get_db)):
    _books = crud.get_book_by_id(db, book_id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_books)


@router.post("/update")
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(db, book_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=_book)


@router.delete("/{id}")
async def delete_book(id: int,  db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
