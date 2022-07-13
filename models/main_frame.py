# coding:utf-8
from unicodedata import name
from models import *

class SuffixSection(BaseModel):
    pass

class PrefixSection(BaseModel):
    starter: IntField = IntField(name='起始符', 
                                output_data_type='hex', 
                                length=1, 
                                output_value='68', 
                                input_value=68)
    head_flag: IntField = IntField(name='头标识', 
                                output_data_type='hex', 
                                length=1, 
                                output_value='F5', 
                                input_value=68)
    datagram_length: IntField = IntField(name='报文长度', 
                                output_data_type='hex', 
                                length=2, 
                                output_value='0000', 
                                input_value=68)
    protocol_version: IntField = IntField(name='协议版本', 
                                output_data_type='hex', 
                                length=2, 
                                output_value='0001', 
                                input_value=1)
    function_code: IntField = IntField(name='功能码',
                                    output_data_type='bcd',
                                    length=2,
                                    )