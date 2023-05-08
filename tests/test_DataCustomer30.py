from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        PaymentInfo,
        CustomerResult,
        WorkflowListResult,
        PaymentInfoResult,
        DateResult,
        AccountResult,
        IntegerArrayResult,
        CustomerListResult,
        SearchFilter_Customer,
        StringResult,
        CustomerIN,
        IntegerList
)


from src.pyplunet.enums import (
        EventType
)


class test_set_DataCustomer30(BaseModel):
    customer_in: CustomerIN
    enable_null_or_empty_values: bool
    customer_id: int
    search_filter: SearchFilter_Customer
    payment_info: PaymentInfo
    resource_id: int
    text: str
    payment_method_id: int
    system_language_code: str
    server_authentication_string: str
    server_address: str
    event_type: EventType
    date_initial_contact: datetime
    status: int
    status_list: IntegerList
    account_id: int
    dossier: str
    form_of_address: int
    website: str
    fax: str
    skype_id: str
    name: str
    external_id: str
    e_mail: str
    academic_title: str
    opening: str
    phone_number: str

def get_test_set() -> test_set_DataCustomer30:
    return test_set_DataCustomer30(
            customer_in= ,
            enable_null_or_empty_values= ,
            customer_id= ,
            search_filter= ,
            payment_info= ,
            resource_id= ,
            text= ,
            payment_method_id= ,
            system_language_code= ,
            server_authentication_string= ,
            server_address= ,
            event_type= ,
            date_initial_contact= ,
            status= ,
            status_list= ,
            account_id= ,
            dossier= ,
            form_of_address= ,
            website= ,
            fax= ,
            skype_id= ,
            name= ,
            external_id= ,
            e_mail= ,
            academic_title= ,
            opening= ,
            phone_number= 
    )


def test_DataCustomer30_update(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.update(
                customer_in=test_set.customer_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_update was successful.")




def test_DataCustomer30_delete(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.delete(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_delete was successful.")




def test_DataCustomer30_insert(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.insert(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomer30_insert was successful.")




def test_DataCustomer30_search(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.search(
                search_filter=test_set.search_filter
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataCustomer30_search was successful.")




def test_DataCustomer30_get_currency(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_currency(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_currency failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_currency was successful.")




def test_DataCustomer30_get_project_manager_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_project_manager_id(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_project_manager_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomer30_get_project_manager_id was successful.")




def test_DataCustomer30_get_created_by_resource_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_created_by_resource_id(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_created_by_resource_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomer30_get_created_by_resource_id was successful.")




def test_DataCustomer30_set_payment_information(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_payment_information(
                customer_id=test_set.customer_id,
                payment_info=test_set.payment_info
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_payment_information failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_payment_information was successful.")




def test_DataCustomer30_get_account_manager_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_account_manager_id(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_account_manager_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomer30_get_account_manager_id was successful.")




def test_DataCustomer30_set_account_manager_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_account_manager_id(
                customer_id=test_set.customer_id,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_account_manager_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_account_manager_id was successful.")




def test_DataCustomer30_set_project_manager_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_project_manager_id(
                customer_id=test_set.customer_id,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_project_manager_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_project_manager_id was successful.")




def test_DataCustomer30_get_available_workflows(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_available_workflows(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_available_workflows failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == WorkflowListResult
    print(f"test_DataCustomer30_get_available_workflows was successful.")




def test_DataCustomer30_get_payment_information(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_payment_information(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_payment_information failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PaymentInfoResult
    print(f"test_DataCustomer30_get_payment_information was successful.")




def test_DataCustomer30_get_available_payment_method_list(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_available_payment_method_list(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_available_payment_method_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataCustomer30_get_available_payment_method_list was successful.")




def test_DataCustomer30_set_source_of_contact(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_source_of_contact(
                customer_id=test_set.customer_id,
                text=test_set.text
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_source_of_contact failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_source_of_contact was successful.")




def test_DataCustomer30_get_date_of_initial_contact(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_date_of_initial_contact(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_date_of_initial_contact failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataCustomer30_get_date_of_initial_contact was successful.")




def test_DataCustomer30_get_payment_method_description(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_payment_method_description(
                payment_method_id=test_set.payment_method_id,
                system_language_code=test_set.system_language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_payment_method_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_payment_method_description was successful.")




def test_DataCustomer30_get_source_of_contact(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_source_of_contact(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_source_of_contact failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_source_of_contact was successful.")




def test_DataCustomer30_deregister_callback_observer(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.deregister_callback_observer(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_deregister_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_deregister_callback_observer was successful.")




def test_DataCustomer30_register_callback_notify(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.register_callback_notify(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_register_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_register_callback_notify was successful.")




def test_DataCustomer30_set_date_of_initial_contact(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_date_of_initial_contact(
                customer_id=test_set.customer_id,
                date_initial_contact=test_set.date_initial_contact
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_date_of_initial_contact failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_date_of_initial_contact was successful.")




def test_DataCustomer30_get_available_account_id_list(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_available_account_id_list(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_available_account_id_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataCustomer30_get_available_account_id_list was successful.")




def test_DataCustomer30_deregister_callback_notify(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.deregister_callback_notify(
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_deregister_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_deregister_callback_notify was successful.")




def test_DataCustomer30_register_callback_observer(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.register_callback_observer(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_register_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_register_callback_observer was successful.")




def test_DataCustomer30_get_full_name(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_full_name(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_full_name failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_full_name was successful.")




def test_DataCustomer30_get_status(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_status(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomer30_get_status was successful.")




def test_DataCustomer30_set_status(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_status(
                status=test_set.status,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_status was successful.")




def test_DataCustomer30_get_all_customer_objects2(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_all_customer_objects2(
                status_list=test_set.status_list
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_all_customer_objects2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CustomerListResult
    print(f"test_DataCustomer30_get_all_customer_objects2 was successful.")




def test_DataCustomer30_get_customer_object(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_customer_object(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_customer_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CustomerResult
    print(f"test_DataCustomer30_get_customer_object was successful.")




def test_DataCustomer30_get_all_customer_objects(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_all_customer_objects(
                status=test_set.status
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_all_customer_objects failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CustomerListResult
    print(f"test_DataCustomer30_get_all_customer_objects was successful.")




def test_DataCustomer30_get_account(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_account(
                account_id=test_set.account_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == AccountResult
    print(f"test_DataCustomer30_get_account was successful.")




def test_DataCustomer30_set_dossier(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_dossier(
                customer_id=test_set.customer_id,
                dossier=test_set.dossier
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_dossier failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_dossier was successful.")




def test_DataCustomer30_get_dossier(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_dossier(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_dossier failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_dossier was successful.")




def test_DataCustomer30_get_fax(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_fax(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_fax failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_fax was successful.")




def test_DataCustomer30_get_name1(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_name1(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_name1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_name1 was successful.")




def test_DataCustomer30_set_form_of_address(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_form_of_address(
                form_of_address=test_set.form_of_address,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_form_of_address failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_form_of_address was successful.")




def test_DataCustomer30_get_form_of_address(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_form_of_address(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_form_of_address failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomer30_get_form_of_address was successful.")




def test_DataCustomer30_set_website(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_website(
                website=test_set.website,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_website failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_website was successful.")




def test_DataCustomer30_set_fax(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_fax(
                fax=test_set.fax,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_fax failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_fax was successful.")




def test_DataCustomer30_set_skype_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_skype_id(
                skype_id=test_set.skype_id,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_skype_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_skype_id was successful.")




def test_DataCustomer30_get_skype_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_skype_id(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_skype_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_skype_id was successful.")




def test_DataCustomer30_get_academic_title(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_academic_title(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_academic_title failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_academic_title was successful.")




def test_DataCustomer30_insert2(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.insert2(
                customer_in=test_set.customer_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomer30_insert2 was successful.")




def test_DataCustomer30_get_phone(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_phone(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_phone failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_phone was successful.")




def test_DataCustomer30_set_name1(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_name1(
                name=test_set.name,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_name1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_name1 was successful.")




def test_DataCustomer30_get_mobile_phone(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_mobile_phone(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_mobile_phone failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_mobile_phone was successful.")




def test_DataCustomer30_get_website(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_website(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_website failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_website was successful.")




def test_DataCustomer30_set_external_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_external_id(
                external_id=test_set.external_id,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_external_id was successful.")




def test_DataCustomer30_set_name2(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_name2(
                name=test_set.name,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_name2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_name2 was successful.")




def test_DataCustomer30_set_email(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_email(
                e_mail=test_set.e_mail,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_email failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_email was successful.")




def test_DataCustomer30_get_opening(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_opening(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_opening failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_opening was successful.")




def test_DataCustomer30_set_academic_title(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_academic_title(
                academic_title=test_set.academic_title,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_academic_title failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_academic_title was successful.")




def test_DataCustomer30_set_opening(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_opening(
                opening=test_set.opening,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_opening failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_opening was successful.")




def test_DataCustomer30_set_phone(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_phone(
                phone_number=test_set.phone_number,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_phone failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_phone was successful.")




def test_DataCustomer30_get_email(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_email(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_email failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_email was successful.")




def test_DataCustomer30_get_external_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_external_id(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_external_id was successful.")




def test_DataCustomer30_set_mobile_phone(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.set_mobile_phone(
                phone_number=test_set.phone_number,
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_set_mobile_phone failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomer30_set_mobile_phone was successful.")




def test_DataCustomer30_get_name2(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.get_name2(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_get_name2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomer30_get_name2 was successful.")




def test_DataCustomer30_seek_by_external_id(pc: PlunetClient, test_set: test_set_DataCustomer30):
    try:
        resp = pc.customer.seek_by_external_id(
                external_id=test_set.external_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomer30_seek_by_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomer30_seek_by_external_id was successful.")



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
        test_DataCustomer30_update(pc, test_set)
        test_DataCustomer30_delete(pc, test_set)
        test_DataCustomer30_insert(pc, test_set)
        test_DataCustomer30_search(pc, test_set)
        test_DataCustomer30_get_currency(pc, test_set)
        test_DataCustomer30_get_project_manager_id(pc, test_set)
        test_DataCustomer30_get_created_by_resource_id(pc, test_set)
        test_DataCustomer30_set_payment_information(pc, test_set)
        test_DataCustomer30_get_account_manager_id(pc, test_set)
        test_DataCustomer30_set_account_manager_id(pc, test_set)
        test_DataCustomer30_set_project_manager_id(pc, test_set)
        test_DataCustomer30_get_available_workflows(pc, test_set)
        test_DataCustomer30_get_payment_information(pc, test_set)
        test_DataCustomer30_get_available_payment_method_list(pc, test_set)
        test_DataCustomer30_set_source_of_contact(pc, test_set)
        test_DataCustomer30_get_date_of_initial_contact(pc, test_set)
        test_DataCustomer30_get_payment_method_description(pc, test_set)
        test_DataCustomer30_get_source_of_contact(pc, test_set)
        test_DataCustomer30_deregister_callback_observer(pc, test_set)
        test_DataCustomer30_register_callback_notify(pc, test_set)
        test_DataCustomer30_set_date_of_initial_contact(pc, test_set)
        test_DataCustomer30_get_available_account_id_list(pc, test_set)
        test_DataCustomer30_deregister_callback_notify(pc, test_set)
        test_DataCustomer30_register_callback_observer(pc, test_set)
        test_DataCustomer30_get_full_name(pc, test_set)
        test_DataCustomer30_get_status(pc, test_set)
        test_DataCustomer30_set_status(pc, test_set)
        test_DataCustomer30_get_all_customer_objects2(pc, test_set)
        test_DataCustomer30_get_customer_object(pc, test_set)
        test_DataCustomer30_get_all_customer_objects(pc, test_set)
        test_DataCustomer30_get_account(pc, test_set)
        test_DataCustomer30_set_dossier(pc, test_set)
        test_DataCustomer30_get_dossier(pc, test_set)
        test_DataCustomer30_get_fax(pc, test_set)
        test_DataCustomer30_get_name1(pc, test_set)
        test_DataCustomer30_set_form_of_address(pc, test_set)
        test_DataCustomer30_get_form_of_address(pc, test_set)
        test_DataCustomer30_set_website(pc, test_set)
        test_DataCustomer30_set_fax(pc, test_set)
        test_DataCustomer30_set_skype_id(pc, test_set)
        test_DataCustomer30_get_skype_id(pc, test_set)
        test_DataCustomer30_get_academic_title(pc, test_set)
        test_DataCustomer30_insert2(pc, test_set)
        test_DataCustomer30_get_phone(pc, test_set)
        test_DataCustomer30_set_name1(pc, test_set)
        test_DataCustomer30_get_mobile_phone(pc, test_set)
        test_DataCustomer30_get_website(pc, test_set)
        test_DataCustomer30_set_external_id(pc, test_set)
        test_DataCustomer30_set_name2(pc, test_set)
        test_DataCustomer30_set_email(pc, test_set)
        test_DataCustomer30_get_opening(pc, test_set)
        test_DataCustomer30_set_academic_title(pc, test_set)
        test_DataCustomer30_set_opening(pc, test_set)
        test_DataCustomer30_set_phone(pc, test_set)
        test_DataCustomer30_get_email(pc, test_set)
        test_DataCustomer30_get_external_id(pc, test_set)
        test_DataCustomer30_set_mobile_phone(pc, test_set)
        test_DataCustomer30_get_name2(pc, test_set)
        test_DataCustomer30_seek_by_external_id(pc, test_set)