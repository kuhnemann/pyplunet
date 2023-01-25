from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        CallbackListResult,
        StringArrayResult,
        LanguageListResult,
        CurrencyList,
        CountryListResult,
        CompanyCodeListResult,
        ServiceListResult,
        StringResult
)



class test_set_DataAdmin30(BaseModel):
    language_code: str

def get_test_set() -> test_set_DataAdmin30:
    return test_set_DataAdmin30(
            language_code="EN"
    )
def test_DataAdmin30_get_system_currencies(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_system_currencies(
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == CurrencyList


def test_DataAdmin30_get_available_document_templates(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_available_document_templates(
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringArrayResult


def test_DataAdmin30_get_company_code_list(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_company_code_list(
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == CompanyCodeListResult


def test_DataAdmin30_get_domestic_currency(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_domestic_currency(
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataAdmin30_get_available_services(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_available_services(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == ServiceListResult


def test_DataAdmin30_get_available_countries(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_available_countries(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == CountryListResult


def test_DataAdmin30_get_available_languages(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_available_languages(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == LanguageListResult


def test_DataAdmin30_get_list_of_registered_callbacks(pc: PlunetClient, test_set: test_set_DataAdmin30):
    try:
        resp = pc.admin.get_list_of_registered_callbacks(
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == CallbackListResult



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()
    test_DataAdmin30_get_system_currencies(pc, test_set)
    test_DataAdmin30_get_available_document_templates(pc, test_set)
    test_DataAdmin30_get_company_code_list(pc, test_set)
    test_DataAdmin30_get_domestic_currency(pc, test_set)
    test_DataAdmin30_get_available_services(pc, test_set)
    test_DataAdmin30_get_available_countries(pc, test_set)
    test_DataAdmin30_get_available_languages(pc, test_set)
    test_DataAdmin30_get_list_of_registered_callbacks(pc, test_set)