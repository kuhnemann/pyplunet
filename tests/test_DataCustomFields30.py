from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        TextmoduleResult,
        PropertyResult,
        TextmoduleIN,
        IntegerList,
        StringResult
)



class test_set_DataCustomFields30(BaseModel):
    property_name_english: str
    property_usage_area: int
    main_id: int
    property_value_id: int
    language_code: str
    property_value_list: IntegerList
    textmodule_in: TextmoduleIN
    id: int
    flag: str
    text_module_usage_area: int

def get_test_set() -> test_set_DataCustomFields30:
    return test_set_DataCustomFields30(
            property_name_english= ,
            property_usage_area= ,
            main_id= ,
            property_value_id= ,
            language_code= ,
            property_value_list= ,
            textmodule_in= ,
            id= ,
            flag= ,
            text_module_usage_area= 
    )
def test_DataCustomFields30_get_property(pc: PlunetClient, test_set: test_set_DataCustomFields30):
    try:
        resp = pc.custom_fields.get_property(
                property_name_english=test_set.property_name_english,
                property_usage_area=test_set.property_usage_area,
                main_id=test_set.main_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == PropertyResult


def test_DataCustomFields30_get_property_value_text(pc: PlunetClient, test_set: test_set_DataCustomFields30):
    try:
        resp = pc.custom_fields.get_property_value_text(
                property_name_english=test_set.property_name_english,
                property_value_id=test_set.property_value_id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomFields30_set_property_value_list(pc: PlunetClient, test_set: test_set_DataCustomFields30):
    try:
        resp = pc.custom_fields.set_property_value_list(
                property_name_english=test_set.property_name_english,
                property_usage_area=test_set.property_usage_area,
                property_value_list=test_set.property_value_list,
                main_id=test_set.main_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomFields30_set_property_value(pc: PlunetClient, test_set: test_set_DataCustomFields30):
    try:
        resp = pc.custom_fields.set_property_value(
                property_name_english=test_set.property_name_english,
                property_usage_area=test_set.property_usage_area,
                property_value_id=test_set.property_value_id,
                main_id=test_set.main_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomFields30_set_textmodule(pc: PlunetClient, test_set: test_set_DataCustomFields30):
    try:
        resp = pc.custom_fields.set_textmodule(
                textmodule_in=test_set.textmodule_in,
                id=test_set.id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomFields30_get_textmodule(pc: PlunetClient, test_set: test_set_DataCustomFields30):
    try:
        resp = pc.custom_fields.get_textmodule(
                flag=test_set.flag,
                text_module_usage_area=test_set.text_module_usage_area,
                id=test_set.id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == TextmoduleResult



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()
    test_DataCustomFields30_get_property(pc, test_set)
    test_DataCustomFields30_get_property_value_text(pc, test_set)
    test_DataCustomFields30_set_property_value_list(pc, test_set)
    test_DataCustomFields30_set_property_value(pc, test_set)
    test_DataCustomFields30_set_textmodule(pc, test_set)
    test_DataCustomFields30_get_textmodule(pc, test_set)