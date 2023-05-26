from typing import Optional,List
from pydantic import BaseModel

class taskBase(BaseModel):
    title : str
    body : str

class task(taskBase):

    class Config():
        orm_mode = True
