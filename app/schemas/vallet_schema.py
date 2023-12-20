from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


# class ValletSchema(BaseModel):
#     id: Optional[int] = None
#     currency: Optional[str] = None
#     amount: Optional[float] = None

#     # class Config:
#     #     orm_mode = True


class CreateRequestVallet(BaseModel):
    currency_id: Union[int, None] = None
    amount: Union[float, None] = None
   

class CreateRequestCurrency(BaseModel):
    name: Union[str, None] = None

class CreateRequestCategory(BaseModel):
    name: Union[str, None] = None

class CreateRequestTransaction(BaseModel):

    source: Union[int, None] = None
    target: Union[int, None] = None
    symma: Union[float, None] = None

class CreateRequestPurchase(BaseModel):
    category_id: Union[int, None] = None
    wallet_id: Union[int, None] = None
    symma: Union[float, None] = None
   

class Response(GenericModel, Generic[T]):
    code: int = 200
    # status: str
    message: str = 'Success'
    data: Optional[T]

 

# class Request(GenericModel, Generic[T]):
#     parameter: Optional[T] = Field(...)


# class RequestVallet(BaseModel):
#     parameter: CreateRequestVallet = Field(...)
