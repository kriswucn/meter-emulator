# coding:utf-8
from pydantic import BaseModel

class Field(BaseModel):
    name: str
    code: str
    data_type: str
    