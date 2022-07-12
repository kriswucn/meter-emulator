# coding:utf-8
from operator import le
from xml.etree.ElementTree import C14NWriterTarget
from pydantic import BaseModel
from typing import List, Optional


class Choice(BaseModel):
    name: str
    value: int


class Field(BaseModel):
    name: str
    code: str
    data_type: str
    length: int
    actual_value: Optional[str]
    encoded_value: Optional[str]
    choice: Optional[Choice]
    fixed_encoded_value: Optional[str]
    
    def __repr__(self) -> str:
        return "class<Filed> name={} value={}".format(self.name, self.value)


if __name__ == "__main__":
    c1 = Choice(name="主动上报", value=1)
    c2 = Choice(name="定时上报", value=2)
    field = Field(name="起始符",
                  code="start_flag",
                  data_type='hex',
                  length=1,
                  fixed_value='68')
    print(field)
