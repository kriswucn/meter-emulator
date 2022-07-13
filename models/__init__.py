# coding:utf-8
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class Choice(BaseModel):
    name: str
    value: int


class BaseField(BaseModel):
    name: str
    output_data_type: str
    length: int
    output_value: Optional[str]

class IntField(BaseField):
    input_value: int

class FloatField(BaseField):
    input_value: float

class DateField(BaseField):
    input_value: date

class DateTimeField(BaseField):
    input_value: datetime

class StrField(BaseField):
    input_value: str

class ChoiceField(BaseField):
    input_value: Choice