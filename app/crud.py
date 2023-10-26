from sqlalchemy.orm import Session
from app.models import Book
from app.schemas import BookSchema


# Get all book data
def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

# Get By Id book  data
def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

# Create book  data
def create_book(db: Session, book: BookSchema):
    _book = Book(title=book.title, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book

# Remove book data
def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()

# Update book data
def update_book(db: Session, book_id: int, title: str, description: str):
    _book = get_book_by_id(db=db, book_id=book_id)
    _book.title = title
    _book.description = description
    db.commit()
    db.refresh(_book)
    return _book
