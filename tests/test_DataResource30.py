from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        PricelistListResult,
        SearchFilter_Resource,
        IntegerArrayResult,
        PaymentInfoResult,
        AccountResult,
        ResourceIN,
        ResourceResult,
        PaymentInfo,
        ResourceListResult,
        IntegerResult,
        IntegerList,
        StringResult
)


from src.pyplunet.enums import (
        ResourceType,
        EventType
)


class test_set_DataResource30(BaseModel):
    resource_in: ResourceIN
    enable_null_or_empty_values: bool
    resource_id: int
    working_status: int
    search_filter_resource: SearchFilter_Resource
    currency_iso_code: str
    status: int
    saml_external_id: str
    working_status_list: IntegerList
    status_list: IntegerList
    server_authentication_string: str
    server_address: str
    event_type: EventType
    payment_method_id: int
    system_language_code: str
    payment_info: PaymentInfo
    name: str
    external_id: str
    phone_number: str
    academic_title: str
    website: str
    fax: str
    form_of_address: int
    e_mail: str
    skype_id: str
    opening: str
    cost_center: str
    login_name: str
    resource_type: ResourceType
    sourcelanguage: str
    targetlanguage: str
    account_id: int

def get_test_set() -> test_set_DataResource30:
    return test_set_DataResource30(
            resource_in= ,
            enable_null_or_empty_values= ,
            resource_id= ,
            working_status= ,
            search_filter_resource= ,
            currency_iso_code= ,
            status= ,
            saml_external_id= ,
            working_status_list= ,
            status_list= ,
            server_authentication_string= ,
            server_address= ,
            event_type= ,
            payment_method_id= ,
            system_language_code= ,
            payment_info= ,
            name= ,
            external_id= ,
            phone_number= ,
            academic_title= ,
            website= ,
            fax= ,
            form_of_address= ,
            e_mail= ,
            skype_id= ,
            opening= ,
            cost_center= ,
            login_name= ,
            resource_type= ,
            sourcelanguage= ,
            targetlanguage= ,
            account_id= 
    )
def test_DataResource30_update(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.update(
                resource_in=test_set.resource_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_delete(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.delete(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_insert(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.insert(
                working_status=test_set.working_status
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResource30_search(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.search(
                search_filter_resource=test_set.search_filter_resource
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult


def test_DataResource30_get_currency(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_currency(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_currency(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_currency(
                resource_id=test_set.resource_id,
                currency_iso_code=test_set.currency_iso_code
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_full_name(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_full_name(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_get_status(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_status(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResource30_set_status(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_status(
                status=test_set.status,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_saml_external_id(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_saml_external_id(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_saml_external_id(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_saml_external_id(
                resource_id=test_set.resource_id,
                saml_external_id=test_set.saml_external_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_resource_object(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_resource_object(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == ResourceResult


def test_DataResource30_get_all_resource_objects2(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_all_resource_objects2(
                working_status_list=test_set.working_status_list,
                status_list=test_set.status_list
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == ResourceListResult


def test_DataResource30_get_all_resource_objects(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_all_resource_objects(
                working_status=test_set.working_status,
                status=test_set.status
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == ResourceListResult


def test_DataResource30_deregister_callback_observer(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.deregister_callback_observer(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_available_account_id_list(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_available_account_id_list(
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult


def test_DataResource30_register_callback_notify(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.register_callback_notify(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_payment_method_description(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_payment_method_description(
                payment_method_id=test_set.payment_method_id,
                system_language_code=test_set.system_language_code
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_get_payment_information(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_payment_information(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == PaymentInfoResult


def test_DataResource30_set_payment_information(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_payment_information(
                resource_id=test_set.resource_id,
                payment_info=test_set.payment_info
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_available_payment_method_list(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_available_payment_method_list(
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult


def test_DataResource30_deregister_callback_notify(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.deregister_callback_notify(
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_register_callback_observer(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.register_callback_observer(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_name1(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_name1(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_name2(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_name2(
                name=test_set.name,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_set_name1(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_name1(
                name=test_set.name,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_set_external_id(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_external_id(
                external_id=test_set.external_id,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_external_id(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_external_id(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_phone(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_phone(
                phone_number=test_set.phone_number,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_phone(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_phone(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_get_name2(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_name2(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_get_skype_id(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_skype_id(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_academic_title(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_academic_title(
                academic_title=test_set.academic_title,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_mobile_phone(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_mobile_phone(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_website(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_website(
                website=test_set.website,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_email(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_email(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_fax(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_fax(
                fax=test_set.fax,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_fax(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_fax(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_form_of_address(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_form_of_address(
                form_of_address=test_set.form_of_address,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_form_of_address(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_form_of_address(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResource30_set_email(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_email(
                e_mail=test_set.e_mail,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_set_mobile_phone(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_mobile_phone(
                phone_number=test_set.phone_number,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_website(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_website(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_skype_id(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_skype_id(
                skype_id=test_set.skype_id,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_user_id(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_user_id(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResource30_set_opening(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_opening(
                opening=test_set.opening,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_academic_title(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_academic_title(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_seek_by_external_id(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.seek_by_external_id(
                external_id=test_set.external_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResource30_get_opening(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_opening(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_get_cost_center(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_cost_center(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_cost_center(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_cost_center(
                cost_center=test_set.cost_center,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_resource_type(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_resource_type(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResource30_set_supervisor2(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_supervisor2(
                login_name=test_set.login_name,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_working_status(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_working_status(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResource30_get_supervisor2(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_supervisor2(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_working_status(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_working_status(
                working_status=test_set.working_status,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_supervisor1(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_supervisor1(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResource30_set_supervisor1(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_supervisor1(
                login_name=test_set.login_name,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_set_resource_type(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.set_resource_type(
                resource_type=test_set.resource_type,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResource30_get_pricelists(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_pricelists(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == PricelistListResult


def test_DataResource30_get_pricelists2(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_pricelists2(
                sourcelanguage=test_set.sourcelanguage,
                targetlanguage=test_set.targetlanguage,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == PricelistListResult


def test_DataResource30_get_account(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.get_account(
                account_id=test_set.account_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == AccountResult


def test_DataResource30_insert_object(pc: PlunetClient, test_set: test_set_DataResource30):
    try:
        resp = pc.resource.insert_object(
                resource_in=test_set.resource_in
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()
    test_DataResource30_update(pc, test_set)
    test_DataResource30_delete(pc, test_set)
    test_DataResource30_insert(pc, test_set)
    test_DataResource30_search(pc, test_set)
    test_DataResource30_get_currency(pc, test_set)
    test_DataResource30_set_currency(pc, test_set)
    test_DataResource30_get_full_name(pc, test_set)
    test_DataResource30_get_status(pc, test_set)
    test_DataResource30_set_status(pc, test_set)
    test_DataResource30_get_saml_external_id(pc, test_set)
    test_DataResource30_set_saml_external_id(pc, test_set)
    test_DataResource30_get_resource_object(pc, test_set)
    test_DataResource30_get_all_resource_objects2(pc, test_set)
    test_DataResource30_get_all_resource_objects(pc, test_set)
    test_DataResource30_deregister_callback_observer(pc, test_set)
    test_DataResource30_get_available_account_id_list(pc, test_set)
    test_DataResource30_register_callback_notify(pc, test_set)
    test_DataResource30_get_payment_method_description(pc, test_set)
    test_DataResource30_get_payment_information(pc, test_set)
    test_DataResource30_set_payment_information(pc, test_set)
    test_DataResource30_get_available_payment_method_list(pc, test_set)
    test_DataResource30_deregister_callback_notify(pc, test_set)
    test_DataResource30_register_callback_observer(pc, test_set)
    test_DataResource30_get_name1(pc, test_set)
    test_DataResource30_set_name2(pc, test_set)
    test_DataResource30_set_name1(pc, test_set)
    test_DataResource30_set_external_id(pc, test_set)
    test_DataResource30_get_external_id(pc, test_set)
    test_DataResource30_set_phone(pc, test_set)
    test_DataResource30_get_phone(pc, test_set)
    test_DataResource30_get_name2(pc, test_set)
    test_DataResource30_get_skype_id(pc, test_set)
    test_DataResource30_set_academic_title(pc, test_set)
    test_DataResource30_get_mobile_phone(pc, test_set)
    test_DataResource30_set_website(pc, test_set)
    test_DataResource30_get_email(pc, test_set)
    test_DataResource30_set_fax(pc, test_set)
    test_DataResource30_get_fax(pc, test_set)
    test_DataResource30_set_form_of_address(pc, test_set)
    test_DataResource30_get_form_of_address(pc, test_set)
    test_DataResource30_set_email(pc, test_set)
    test_DataResource30_set_mobile_phone(pc, test_set)
    test_DataResource30_get_website(pc, test_set)
    test_DataResource30_set_skype_id(pc, test_set)
    test_DataResource30_get_user_id(pc, test_set)
    test_DataResource30_set_opening(pc, test_set)
    test_DataResource30_get_academic_title(pc, test_set)
    test_DataResource30_seek_by_external_id(pc, test_set)
    test_DataResource30_get_opening(pc, test_set)
    test_DataResource30_get_cost_center(pc, test_set)
    test_DataResource30_set_cost_center(pc, test_set)
    test_DataResource30_get_resource_type(pc, test_set)
    test_DataResource30_set_supervisor2(pc, test_set)
    test_DataResource30_get_working_status(pc, test_set)
    test_DataResource30_get_supervisor2(pc, test_set)
    test_DataResource30_set_working_status(pc, test_set)
    test_DataResource30_get_supervisor1(pc, test_set)
    test_DataResource30_set_supervisor1(pc, test_set)
    test_DataResource30_set_resource_type(pc, test_set)
    test_DataResource30_get_pricelists(pc, test_set)
    test_DataResource30_get_pricelists2(pc, test_set)
    test_DataResource30_get_account(pc, test_set)
    test_DataResource30_insert_object(pc, test_set)