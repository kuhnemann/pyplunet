from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        CustomerContactIN,
        CustomerContactResult,
        IntegerArrayResult,
        CustomerContactListResult,
        StringResult
)



class test_set_DataCustomerContact30(BaseModel):
    customer_contact_in: CustomerContactIN
    enable_null_or_empty_values: bool
    partner_id: int
    contact_id: int
    login_name: str
    customer_id: int
    address_id: int
    status: int
    fax: str
    name: str
    external_id: str
    cost_center: str
    e_mail: str
    phone_number: str

def get_test_set() -> test_set_DataCustomerContact30:
    return test_set_DataCustomerContact30(
            customer_contact_in= ,
            enable_null_or_empty_values= ,
            partner_id= ,
            contact_id= ,
            login_name= ,
            customer_id= ,
            address_id= ,
            status= ,
            fax= ,
            name= ,
            external_id= ,
            cost_center= ,
            e_mail= ,
            phone_number= 
    )


def test_DataCustomerContact30_update(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.update(
                customer_contact_in=test_set.customer_contact_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_update was successful.")




def test_DataCustomerContact30_insert(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.insert(
                partner_id=test_set.partner_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerContact30_insert was successful.")




def test_DataCustomerContact30_get_contact_object(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_contact_object(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_contact_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CustomerContactResult
    print(f"test_DataCustomerContact30_get_contact_object was successful.")




def test_DataCustomerContact30_set_supervisor1(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_supervisor1(
                login_name=test_set.login_name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_supervisor1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_supervisor1 was successful.")




def test_DataCustomerContact30_get_supervisor1(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_supervisor1(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_supervisor1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_supervisor1 was successful.")




def test_DataCustomerContact30_set_supervisor2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_supervisor2(
                login_name=test_set.login_name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_supervisor2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_supervisor2 was successful.")




def test_DataCustomerContact30_get_supervisor2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_supervisor2(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_supervisor2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_supervisor2 was successful.")




def test_DataCustomerContact30_get_all_contacts(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_all_contacts(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_all_contacts failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataCustomerContact30_get_all_contacts was successful.")




def test_DataCustomerContact30_set_customer_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_customer_id(
                customer_id=test_set.customer_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_customer_id was successful.")




def test_DataCustomerContact30_set_address_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_address_id(
                address_id=test_set.address_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_address_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_address_id was successful.")




def test_DataCustomerContact30_get_status(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_status(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerContact30_get_status was successful.")




def test_DataCustomerContact30_set_status(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_status(
                status=test_set.status,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_status was successful.")




def test_DataCustomerContact30_get_all_contact_objects(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_all_contact_objects(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_all_contact_objects failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CustomerContactListResult
    print(f"test_DataCustomerContact30_get_all_contact_objects was successful.")




def test_DataCustomerContact30_get_address_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_address_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_address_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerContact30_get_address_id was successful.")




def test_DataCustomerContact30_get_fax(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_fax(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_fax failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_fax was successful.")




def test_DataCustomerContact30_get_name1(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_name1(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_name1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_name1 was successful.")




def test_DataCustomerContact30_set_fax(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_fax(
                fax=test_set.fax,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_fax failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_fax was successful.")




def test_DataCustomerContact30_insert2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.insert2(
                customer_contact_in=test_set.customer_contact_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerContact30_insert2 was successful.")




def test_DataCustomerContact30_get_phone(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_phone(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_phone failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_phone was successful.")




def test_DataCustomerContact30_set_name1(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_name1(
                name=test_set.name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_name1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_name1 was successful.")




def test_DataCustomerContact30_get_mobile_phone(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_mobile_phone(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_mobile_phone failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_mobile_phone was successful.")




def test_DataCustomerContact30_set_external_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_external_id(
                external_id=test_set.external_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_external_id was successful.")




def test_DataCustomerContact30_set_cost_center(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_cost_center(
                cost_center=test_set.cost_center,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_cost_center failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_cost_center was successful.")




def test_DataCustomerContact30_get_user_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_user_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_user_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerContact30_get_user_id was successful.")




def test_DataCustomerContact30_set_name2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_name2(
                name=test_set.name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_name2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_name2 was successful.")




def test_DataCustomerContact30_set_email(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_email(
                e_mail=test_set.e_mail,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_email failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_email was successful.")




def test_DataCustomerContact30_set_phone(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_phone(
                phone_number=test_set.phone_number,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_phone failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_phone was successful.")




def test_DataCustomerContact30_get_email(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_email(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_email failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_email was successful.")




def test_DataCustomerContact30_get_external_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_external_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_external_id was successful.")




def test_DataCustomerContact30_set_mobile_phone(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_mobile_phone(
                phone_number=test_set.phone_number,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_set_mobile_phone failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerContact30_set_mobile_phone was successful.")




def test_DataCustomerContact30_get_name2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_name2(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_name2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_name2 was successful.")




def test_DataCustomerContact30_seek_by_external_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.seek_by_external_id(
                external_id=test_set.external_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_seek_by_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataCustomerContact30_seek_by_external_id was successful.")




def test_DataCustomerContact30_get_cost_center(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_cost_center(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_cost_center failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerContact30_get_cost_center was successful.")




def test_DataCustomerContact30_get_customer_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_customer_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerContact30_get_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerContact30_get_customer_id was successful.")



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
        test_DataCustomerContact30_update(pc, test_set)
        test_DataCustomerContact30_insert(pc, test_set)
        test_DataCustomerContact30_get_contact_object(pc, test_set)
        test_DataCustomerContact30_set_supervisor1(pc, test_set)
        test_DataCustomerContact30_get_supervisor1(pc, test_set)
        test_DataCustomerContact30_set_supervisor2(pc, test_set)
        test_DataCustomerContact30_get_supervisor2(pc, test_set)
        test_DataCustomerContact30_get_all_contacts(pc, test_set)
        test_DataCustomerContact30_set_customer_id(pc, test_set)
        test_DataCustomerContact30_set_address_id(pc, test_set)
        test_DataCustomerContact30_get_status(pc, test_set)
        test_DataCustomerContact30_set_status(pc, test_set)
        test_DataCustomerContact30_get_all_contact_objects(pc, test_set)
        test_DataCustomerContact30_get_address_id(pc, test_set)
        test_DataCustomerContact30_get_fax(pc, test_set)
        test_DataCustomerContact30_get_name1(pc, test_set)
        test_DataCustomerContact30_set_fax(pc, test_set)
        test_DataCustomerContact30_insert2(pc, test_set)
        test_DataCustomerContact30_get_phone(pc, test_set)
        test_DataCustomerContact30_set_name1(pc, test_set)
        test_DataCustomerContact30_get_mobile_phone(pc, test_set)
        test_DataCustomerContact30_set_external_id(pc, test_set)
        test_DataCustomerContact30_set_cost_center(pc, test_set)
        test_DataCustomerContact30_get_user_id(pc, test_set)
        test_DataCustomerContact30_set_name2(pc, test_set)
        test_DataCustomerContact30_set_email(pc, test_set)
        test_DataCustomerContact30_set_phone(pc, test_set)
        test_DataCustomerContact30_get_email(pc, test_set)
        test_DataCustomerContact30_get_external_id(pc, test_set)
        test_DataCustomerContact30_set_mobile_phone(pc, test_set)
        test_DataCustomerContact30_get_name2(pc, test_set)
        test_DataCustomerContact30_seek_by_external_id(pc, test_set)
        test_DataCustomerContact30_get_cost_center(pc, test_set)
        test_DataCustomerContact30_get_customer_id(pc, test_set)