
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

    vallet_id_1 = Column(Integer, ForeignKey("vallets.id"))
    vallet_id_2 = Column(Integer, ForeignKey("vallets.id"))
    currency_id = Column(Integer, ForeignKey("currencies.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    symma = Column(Float)

