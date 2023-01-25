from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        ResourceContactResult,
        IntegerArrayResult,
        ResourceContactIN,
        ResourceContactListResult,
        IntegerResult,
        StringResult
)



class test_set_DataResourceContact30(BaseModel):
    resource_contact_in: ResourceContactIN
    enable_null_or_empty_values: bool
    contact_id: int
    status: int
    resource_id: int
    saml_external_id: str
    name: str
    external_id: str
    phone_number: str
    academic_title: str
    fax: str
    form_of_address: int
    e_mail: str
    skype_id: str
    opening: str
    address_id: int

def get_test_set() -> test_set_DataResourceContact30:
    return test_set_DataResourceContact30(
            resource_contact_in= ,
            enable_null_or_empty_values= ,
            contact_id= ,
            status= ,
            resource_id= ,
            saml_external_id= ,
            name= ,
            external_id= ,
            phone_number= ,
            academic_title= ,
            fax= ,
            form_of_address= ,
            e_mail= ,
            skype_id= ,
            opening= ,
            address_id= 
    )
def test_DataResourceContact30_update(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.update(
                resource_contact_in=test_set.resource_contact_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_insert(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.insert(
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResourceContact30_get_status(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_status(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResourceContact30_set_status(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_status(
                status=test_set.status,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_all_contact_objects(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_all_contact_objects(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == ResourceContactListResult


def test_DataResourceContact30_get_saml_external_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_saml_external_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_set_saml_external_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_saml_external_id(
                contact_id=test_set.contact_id,
                saml_external_id=test_set.saml_external_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_name1(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_name1(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_set_name2(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_name2(
                name=test_set.name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_insert2(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.insert2(
                resource_contact_in=test_set.resource_contact_in
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResourceContact30_set_name1(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_name1(
                name=test_set.name,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_set_external_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_external_id(
                external_id=test_set.external_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_external_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_external_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_set_phone(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_phone(
                phone_number=test_set.phone_number,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_phone(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_phone(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_get_name2(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_name2(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_get_skype_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_skype_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_set_academic_title(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_academic_title(
                academic_title=test_set.academic_title,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_mobile_phone(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_mobile_phone(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_get_email(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_email(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_set_fax(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_fax(
                fax=test_set.fax,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_fax(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_fax(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_set_form_of_address(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_form_of_address(
                form_of_address=test_set.form_of_address,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_form_of_address(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_form_of_address(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResourceContact30_set_email(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_email(
                e_mail=test_set.e_mail,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_set_mobile_phone(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_mobile_phone(
                phone_number=test_set.phone_number,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_set_skype_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_skype_id(
                skype_id=test_set.skype_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_set_opening(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_opening(
                opening=test_set.opening,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_academic_title(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_academic_title(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_seek_by_external_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.seek_by_external_id(
                external_id=test_set.external_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult


def test_DataResourceContact30_get_opening(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_opening(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == StringResult


def test_DataResourceContact30_get_address_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_address_id(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerResult


def test_DataResourceContact30_set_address_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_address_id(
                address_id=test_set.address_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_contact_object(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_contact_object(
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == ResourceContactResult


def test_DataResourceContact30_get_all_contacts(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_all_contacts(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult


def test_DataResourceContact30_set_resource_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.set_resource_id(
                resource_id=test_set.resource_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        input(type(e))
        return
    assert type(resp) == Result


def test_DataResourceContact30_get_resource_id(pc: PlunetClient, test_set: test_set_DataResourceContact30):
    try:
        resp = pc.resource_contact.get_resource_id(
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
    test_DataResourceContact30_update(pc, test_set)
    test_DataResourceContact30_insert(pc, test_set)
    test_DataResourceContact30_get_status(pc, test_set)
    test_DataResourceContact30_set_status(pc, test_set)
    test_DataResourceContact30_get_all_contact_objects(pc, test_set)
    test_DataResourceContact30_get_saml_external_id(pc, test_set)
    test_DataResourceContact30_set_saml_external_id(pc, test_set)
    test_DataResourceContact30_get_name1(pc, test_set)
    test_DataResourceContact30_set_name2(pc, test_set)
    test_DataResourceContact30_insert2(pc, test_set)
    test_DataResourceContact30_set_name1(pc, test_set)
    test_DataResourceContact30_set_external_id(pc, test_set)
    test_DataResourceContact30_get_external_id(pc, test_set)
    test_DataResourceContact30_set_phone(pc, test_set)
    test_DataResourceContact30_get_phone(pc, test_set)
    test_DataResourceContact30_get_name2(pc, test_set)
    test_DataResourceContact30_get_skype_id(pc, test_set)
    test_DataResourceContact30_set_academic_title(pc, test_set)
    test_DataResourceContact30_get_mobile_phone(pc, test_set)
    test_DataResourceContact30_get_email(pc, test_set)
    test_DataResourceContact30_set_fax(pc, test_set)
    test_DataResourceContact30_get_fax(pc, test_set)
    test_DataResourceContact30_set_form_of_address(pc, test_set)
    test_DataResourceContact30_get_form_of_address(pc, test_set)
    test_DataResourceContact30_set_email(pc, test_set)
    test_DataResourceContact30_set_mobile_phone(pc, test_set)
    test_DataResourceContact30_set_skype_id(pc, test_set)
    test_DataResourceContact30_set_opening(pc, test_set)
    test_DataResourceContact30_get_academic_title(pc, test_set)
    test_DataResourceContact30_seek_by_external_id(pc, test_set)
    test_DataResourceContact30_get_opening(pc, test_set)
    test_DataResourceContact30_get_address_id(pc, test_set)
    test_DataResourceContact30_set_address_id(pc, test_set)
    test_DataResourceContact30_get_contact_object(pc, test_set)
    test_DataResourceContact30_get_all_contacts(pc, test_set)
    test_DataResourceContact30_set_resource_id(pc, test_set)
    test_DataResourceContact30_get_resource_id(pc, test_set)