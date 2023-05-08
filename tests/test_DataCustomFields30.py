from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        PropertyResult,
        TextmoduleIN,
        TextmoduleResult,
        StringResult,
        IntegerList
)


from src.pyplunet.enums import (
        PropertyUsageArea,
        TextModuleUsageArea
)


class test_set_DataCustomFields30(BaseModel):
    property_name_english: str
    property_usage_area: PropertyUsageArea
    main_id: int
    property_value_list: IntegerList
    property_value_id: int
    language_code: str
    flag: str
    text_module_usage_area: TextModuleUsageArea
    id: int
    textmodule_in: TextmoduleIN

def get_test_set() -> test_set_DataCustomFields30:
    return test_set_DataCustomFields30(
            property_name_english= ,
            property_usage_area= ,
            main_id= ,
            property_value_list= ,
            property_value_id= ,
            language_code= ,
            flag= ,
            text_module_usage_area= ,
            id= ,
            textmodule_in= 
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
        print(f"test_DataCustomFields30_get_property failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PropertyResult
    print(f"test_DataCustomFields30_get_property was successful.")




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
        print(f"test_DataCustomFields30_set_property_value_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomFields30_set_property_value_list was successful.")




def test_DataCustomFields30_get_property_value_text(pc: PlunetClient, test_set: test_set_DataCustomFields30):
    try:
        resp = pc.custom_fields.get_property_value_text(
                property_name_english=test_set.property_name_english,
                property_value_id=test_set.property_value_id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomFields30_get_property_value_text failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomFields30_get_property_value_text was successful.")




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
        print(f"test_DataCustomFields30_get_textmodule failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == TextmoduleResult
    print(f"test_DataCustomFields30_get_textmodule was successful.")




def test_DataCustomFields30_set_textmodule(pc: PlunetClient, test_set: test_set_DataCustomFields30):
    try:
        resp = pc.custom_fields.set_textmodule(
                textmodule_in=test_set.textmodule_in,
                id=test_set.id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomFields30_set_textmodule failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomFields30_set_textmodule was successful.")




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
        print(f"test_DataCustomFields30_set_property_value failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomFields30_set_property_value was successful.")



if __name__ == '__main__':
    test_clients = [
        test_client_factory.get_test_client,
        test_client_factory.get_test_client_inmemory_cache,
        test_client_factory.get_test_configured_sql_cache,
        test_client_factory.get_test_client_no_caching,
        test_client_factory.get_test_retrying_client,
        test_client_factory.get_test_retrying_client_inmemory_cache,
        test_client_factory.get_test_retrying_configured_sql_cache,
        test_client_factory.get_test_retrying_client_no_caching,
    ]
    test_set = get_test_set()
    for client in test_clients:
        print(client.__name__)
        pc = client()
        test_DataCustomFields30_get_property(pc, test_set)
        test_DataCustomFields30_set_property_value_list(pc, test_set)
        test_DataCustomFields30_get_property_value_text(pc, test_set)
        test_DataCustomFields30_get_textmodule(pc, test_set)
        test_DataCustomFields30_set_textmodule(pc, test_set)
        test_DataCustomFields30_set_property_value(pc, test_set)