from pydantic import BaseModel
from typing import Optional, TypeVar

T = TypeVar("T")


class Book(BaseModel):
    id:str = None
    title:str 
    description : str 


class Response(BaseModel):
    code :str
    status: str
    massage: str
    result :Optional[T] = None

