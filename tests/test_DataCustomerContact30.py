from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerArrayResult,
        CustomerContactIN,
        CustomerContactListResult,
        CustomerContactResult,
        IntegerResult,
        StringResult
)



class test_set_DataCustomerContact30(BaseModel):
    customer_contact_in: CustomerContactIN
    enable_null_or_empty_values: bool
    partner_id: int
    contact_id: int
    status: int
    customer_id: int
    name: str
    external_id: str
    phone_number: str
    fax: str
    e_mail: str
    cost_center: str
    address_id: int
    login_name: str

def get_test_set() -> test_set_DataCustomerContact30:
    return test_set_DataCustomerContact30(
            customer_contact_in= ,
            enable_null_or_empty_values= ,
            partner_id= ,
            contact_id= ,
            status= ,
            customer_id= ,
            name= ,
            external_id= ,
            phone_number= ,
            fax= ,
            e_mail= ,
            cost_center= ,
            address_id= ,
            login_name= 
    )
def test_DataCustomerContact30_update(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.update(
                customer_contact_in=test_set.customer_contact_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_insert(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.insert(
                partner_id=test_set.partner_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataCustomerContact30_get_status(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_status(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataCustomerContact30_set_status(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_status(
                status=test_set.status,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_all_contact_objects(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_all_contact_objects(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == CustomerContactListResult


def test_DataCustomerContact30_get_name1(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_name1(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_set_name2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_name2(
                name=test_set.name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_insert2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.insert2(
                customer_contact_in=test_set.customer_contact_in
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataCustomerContact30_set_name1(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_name1(
                name=test_set.name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_set_external_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_external_id(
                external_id=test_set.external_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_external_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_external_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_set_phone(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_phone(
                phone_number=test_set.phone_number,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_phone(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_phone(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_get_name2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_name2(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_get_mobile_phone(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_mobile_phone(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_get_email(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_email(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_set_fax(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_fax(
                fax=test_set.fax,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_fax(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_fax(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_set_email(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_email(
                e_mail=test_set.e_mail,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_set_mobile_phone(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_mobile_phone(
                phone_number=test_set.phone_number,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_user_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_user_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataCustomerContact30_seek_by_external_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.seek_by_external_id(
                external_id=test_set.external_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult


def test_DataCustomerContact30_get_cost_center(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_cost_center(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_set_cost_center(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_cost_center(
                cost_center=test_set.cost_center,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_address_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_address_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataCustomerContact30_set_address_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_address_id(
                address_id=test_set.address_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_contact_object(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_contact_object(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == CustomerContactResult


def test_DataCustomerContact30_set_customer_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_customer_id(
                customer_id=test_set.customer_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_set_supervisor2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_supervisor2(
                login_name=test_set.login_name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_all_contacts(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_all_contacts(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult


def test_DataCustomerContact30_get_supervisor2(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_supervisor2(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_get_supervisor1(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_supervisor1(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataCustomerContact30_set_supervisor1(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.set_supervisor1(
                login_name=test_set.login_name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataCustomerContact30_get_customer_id(pc: PlunetClient, test_set: test_set_DataCustomerContact30):
    try:
        resp = pc.customer_contact.get_customer_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()
    test_DataCustomerContact30_update(pc, test_set)
    test_DataCustomerContact30_insert(pc, test_set)
    test_DataCustomerContact30_get_status(pc, test_set)
    test_DataCustomerContact30_set_status(pc, test_set)
    test_DataCustomerContact30_get_all_contact_objects(pc, test_set)
    test_DataCustomerContact30_get_name1(pc, test_set)
    test_DataCustomerContact30_set_name2(pc, test_set)
    test_DataCustomerContact30_insert2(pc, test_set)
    test_DataCustomerContact30_set_name1(pc, test_set)
    test_DataCustomerContact30_set_external_id(pc, test_set)
    test_DataCustomerContact30_get_external_id(pc, test_set)
    test_DataCustomerContact30_set_phone(pc, test_set)
    test_DataCustomerContact30_get_phone(pc, test_set)
    test_DataCustomerContact30_get_name2(pc, test_set)
    test_DataCustomerContact30_get_mobile_phone(pc, test_set)
    test_DataCustomerContact30_get_email(pc, test_set)
    test_DataCustomerContact30_set_fax(pc, test_set)
    test_DataCustomerContact30_get_fax(pc, test_set)
    test_DataCustomerContact30_set_email(pc, test_set)
    test_DataCustomerContact30_set_mobile_phone(pc, test_set)
    test_DataCustomerContact30_get_user_id(pc, test_set)
    test_DataCustomerContact30_seek_by_external_id(pc, test_set)
    test_DataCustomerContact30_get_cost_center(pc, test_set)
    test_DataCustomerContact30_set_cost_center(pc, test_set)
    test_DataCustomerContact30_get_address_id(pc, test_set)
    test_DataCustomerContact30_set_address_id(pc, test_set)
    test_DataCustomerContact30_get_contact_object(pc, test_set)
    test_DataCustomerContact30_set_customer_id(pc, test_set)
    test_DataCustomerContact30_set_supervisor2(pc, test_set)
    test_DataCustomerContact30_get_all_contacts(pc, test_set)
    test_DataCustomerContact30_get_supervisor2(pc, test_set)
    test_DataCustomerContact30_get_supervisor1(pc, test_set)
    test_DataCustomerContact30_set_supervisor1(pc, test_set)
    test_DataCustomerContact30_get_customer_id(pc, test_set)