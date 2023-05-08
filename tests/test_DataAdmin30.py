from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        LanguageListResult,
        CountryListResult,
        CurrencyList,
        ServiceListResult,
        StringArrayResult,
        CompanyCodeListResult,
        CallbackListResult,
        StringResult
)



class test_set_DataAdmin30(BaseModel):
    language_code: str

def get_test_set() -> test_set_DataAdmin30:
    return test_set_DataAdmin30(
            language_code="EN"
    )


def test_DataAdmin30_get_domestic_currency(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_domestic_currency(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataAdmin30_get_domestic_currency failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataAdmin30_get_domestic_currency was successful.")




def test_DataAdmin30_get_available_document_templates(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_available_document_templates(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataAdmin30_get_available_document_templates failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataAdmin30_get_available_document_templates was successful.")




def test_DataAdmin30_get_list_of_registered_callbacks(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_list_of_registered_callbacks(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataAdmin30_get_list_of_registered_callbacks failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CallbackListResult
    print(f"test_DataAdmin30_get_list_of_registered_callbacks was successful.")




def test_DataAdmin30_get_company_code_list(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_company_code_list(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataAdmin30_get_company_code_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CompanyCodeListResult
    print(f"test_DataAdmin30_get_company_code_list was successful.")




def test_DataAdmin30_get_available_services(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_available_services(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataAdmin30_get_available_services failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ServiceListResult
    print(f"test_DataAdmin30_get_available_services was successful.")




def test_DataAdmin30_get_available_countries(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_available_countries(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataAdmin30_get_available_countries failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CountryListResult
    print(f"test_DataAdmin30_get_available_countries was successful.")




def test_DataAdmin30_get_system_currencies(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_system_currencies(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataAdmin30_get_system_currencies failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CurrencyList
    print(f"test_DataAdmin30_get_system_currencies was successful.")




def test_DataAdmin30_get_available_languages(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_available_languages(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataAdmin30_get_available_languages failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == LanguageListResult
    print(f"test_DataAdmin30_get_available_languages was successful.")



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
        test_DataAdmin30_get_domestic_currency(pc, test_set)
        test_DataAdmin30_get_available_document_templates(pc, test_set)
        test_DataAdmin30_get_list_of_registered_callbacks(pc, test_set)
        test_DataAdmin30_get_company_code_list(pc, test_set)
        test_DataAdmin30_get_available_services(pc, test_set)
        test_DataAdmin30_get_available_countries(pc, test_set)
        test_DataAdmin30_get_system_currencies(pc, test_set)
        test_DataAdmin30_get_available_languages(pc, test_set)