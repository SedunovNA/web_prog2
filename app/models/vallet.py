
#from pydantic import BaseModel
from app.config.database import Base



from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship




class Vallet(Base):
    __tablename__ = "vallets"

    id = Column(Integer, primary_key=True, index=True)
    #currency = Column(String)
    amount = Column(Float)
    currency_id = Column(Integer, ForeignKey("currencies.id"))

    # items = relationship("Item", back_populates="owner")


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)

    source = Column(Integer, ForeignKey("vallets.id"))
    target = Column(Integer, ForeignKey("vallets.id"))
    symma = Column(Float)
    rate = Column(Float)
    date = Column(String)

class Purchase(Base):
    __tablename__="purchases"
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    wallet_id = Column(Integer, ForeignKey("vallets.id"))
    symma = Column(Float)
    date = Column(String)
