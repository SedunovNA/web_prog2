
#from pydantic import BaseModel
from app.config.database import Base



from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship




class Vallet(Base):
    __tablename__ = "vallets"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)
    amount = Column(Float)

    # items = relationship("Item", back_populates="owner")