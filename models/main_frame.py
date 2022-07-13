# coding:utf-8
from models import IntField, StrField, FloatField, DateField, DateTimeField
from models import BaseModel, Choice, ChoiceField


class PrefixSection(BaseModel):
    start_flag: IntField
    head_flag: IntField
    datagram_length: IntField
    protocol_version: IntField
    function_code: IntField
    trans_direction: ChoiceField
    req_or_resp: ChoiceField
    sub_station_number: StrField
    datagram_id: StrField
    encryption_code: StrField
    data_section_length: IntField


class SuffixSection(BaseModel):
    checking_code: StrField
    tail_flag: IntField
    stop_flag: IntField


if __name__ == '__main__':
    c1 = Choice(name='单条上报', value=1)
    cf1 = ChoiceField(name='上报方式', output_data_type='hex', length=1,
                      input_value=c1, output_value='01')
    print(cf1.json())
