from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        AddressIN,
        IntegerResult,
        StringResult,
        IntegerArrayResult
)


from src.pyplunet.enums import (
        AddressType
)


class test_set_DataCustomerAddress30(BaseModel):
    address_in: AddressIN
    enable_null_or_empty_values: bool
    address_id: int
    partner_id: int
    state: str
    description: str
    language: str
    name: str
    customer_id: int
    cost_center: str
    external_id: str
    street2: str
    zip: str
    street: str
    city: str
    country: str
    address_type: AddressType

def get_test_set() -> test_set_DataCustomerAddress30:
    return test_set_DataCustomerAddress30(
            address_in= ,
            enable_null_or_empty_values= ,
            address_id= ,
            partner_id= ,
            state= ,
            description= ,
            language= ,
            name= ,
            customer_id= ,
            cost_center= ,
            external_id= ,
            street2= ,
            zip= ,
            street= ,
            city= ,
            country= ,
            address_type= 
    )


def test_DataCustomerAddress30_update(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.update(
                address_in=test_set.address_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_update was successful.")




def test_DataCustomerAddress30_delete(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.delete(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_delete was successful.")




def test_DataCustomerAddress30_get_state(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_state(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_state failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_state was successful.")




def test_DataCustomerAddress30_insert(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.insert(
                partner_id=test_set.partner_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerAddress30_insert was successful.")




def test_DataCustomerAddress30_get_country(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_country(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_country failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_country was successful.")




def test_DataCustomerAddress30_set_state(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_state(
                state=test_set.state,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_state failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_state was successful.")




def test_DataCustomerAddress30_get_description(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_description(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_description was successful.")




def test_DataCustomerAddress30_set_description(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_description(
                description=test_set.description,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_description was successful.")




def test_DataCustomerAddress30_get_sales_taxation_type(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_sales_taxation_type(
                address_id=test_set.address_id,
                language=test_set.language
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_sales_taxation_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_sales_taxation_type was successful.")




def test_DataCustomerAddress30_get_name1(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_name1(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_name1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_name1 was successful.")




def test_DataCustomerAddress30_set_name2(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_name2(
                name=test_set.name,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_name2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_name2 was successful.")




def test_DataCustomerAddress30_insert2(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.insert2(
                customer_id=test_set.customer_id,
                address_in=test_set.address_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerAddress30_insert2 was successful.")




def test_DataCustomerAddress30_set_name1(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_name1(
                name=test_set.name,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_name1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_name1 was successful.")




def test_DataCustomerAddress30_get_name2(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_name2(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_name2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_name2 was successful.")




def test_DataCustomerAddress30_get_cost_center(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_cost_center(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_cost_center failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_cost_center was successful.")




def test_DataCustomerAddress30_set_cost_center(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_cost_center(
                cost_center=test_set.cost_center,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_cost_center failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_cost_center was successful.")




def test_DataCustomerAddress30_get_all_addresses(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_all_addresses(
                customer_id=test_set.customer_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_all_addresses failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataCustomerAddress30_get_all_addresses was successful.")




def test_DataCustomerAddress30_get_address_id(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_address_id(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_address_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerAddress30_get_address_id was successful.")




def test_DataCustomerAddress30_set_office(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_office(
                external_id=test_set.external_id,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_office failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_office was successful.")




def test_DataCustomerAddress30_get_office(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_office(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_office failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_office was successful.")




def test_DataCustomerAddress30_set_street2(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_street2(
                street2=test_set.street2,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_street2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_street2 was successful.")




def test_DataCustomerAddress30_get_street2(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_street2(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_street2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_street2 was successful.")




def test_DataCustomerAddress30_set_zip(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_zip(
                zip=test_set.zip,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_zip failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_zip was successful.")




def test_DataCustomerAddress30_get_street(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_street(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_street failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_street was successful.")




def test_DataCustomerAddress30_set_street(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_street(
                street=test_set.street,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_street failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_street was successful.")




def test_DataCustomerAddress30_set_city(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_city(
                city=test_set.city,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_city failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_city was successful.")




def test_DataCustomerAddress30_set_country(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_country(
                country=test_set.country,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_country failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_country was successful.")




def test_DataCustomerAddress30_get_city(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_city(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_city failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_city was successful.")




def test_DataCustomerAddress30_get_zip(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_zip(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_zip failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_zip was successful.")




def test_DataCustomerAddress30_get_address_type(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_address_type(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_address_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCustomerAddress30_get_address_type was successful.")




def test_DataCustomerAddress30_get_taxation_type(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.get_taxation_type(
                address_id=test_set.address_id,
                language=test_set.language
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_get_taxation_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCustomerAddress30_get_taxation_type was successful.")




def test_DataCustomerAddress30_set_address_type(pc: PlunetClient, test_set: test_set_DataCustomerAddress30):
    try:
        resp = pc.customer_address.set_address_type(
                address_type=test_set.address_type,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCustomerAddress30_set_address_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCustomerAddress30_set_address_type was successful.")



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()
    test_DataCustomerAddress30_update(pc, test_set)
    test_DataCustomerAddress30_delete(pc, test_set)
    test_DataCustomerAddress30_get_state(pc, test_set)
    test_DataCustomerAddress30_insert(pc, test_set)
    test_DataCustomerAddress30_get_country(pc, test_set)
    test_DataCustomerAddress30_set_state(pc, test_set)
    test_DataCustomerAddress30_get_description(pc, test_set)
    test_DataCustomerAddress30_set_description(pc, test_set)
    test_DataCustomerAddress30_get_sales_taxation_type(pc, test_set)
    test_DataCustomerAddress30_get_name1(pc, test_set)
    test_DataCustomerAddress30_set_name2(pc, test_set)
    test_DataCustomerAddress30_insert2(pc, test_set)
    test_DataCustomerAddress30_set_name1(pc, test_set)
    test_DataCustomerAddress30_get_name2(pc, test_set)
    test_DataCustomerAddress30_get_cost_center(pc, test_set)
    test_DataCustomerAddress30_set_cost_center(pc, test_set)
    test_DataCustomerAddress30_get_all_addresses(pc, test_set)
    test_DataCustomerAddress30_get_address_id(pc, test_set)
    test_DataCustomerAddress30_set_office(pc, test_set)
    test_DataCustomerAddress30_get_office(pc, test_set)
    test_DataCustomerAddress30_set_street2(pc, test_set)
    test_DataCustomerAddress30_get_street2(pc, test_set)
    test_DataCustomerAddress30_set_zip(pc, test_set)
    test_DataCustomerAddress30_get_street(pc, test_set)
    test_DataCustomerAddress30_set_street(pc, test_set)
    test_DataCustomerAddress30_set_city(pc, test_set)
    test_DataCustomerAddress30_set_country(pc, test_set)
    test_DataCustomerAddress30_get_city(pc, test_set)
    test_DataCustomerAddress30_get_zip(pc, test_set)
    test_DataCustomerAddress30_get_address_type(pc, test_set)
    test_DataCustomerAddress30_get_taxation_type(pc, test_set)
    test_DataCustomerAddress30_set_address_type(pc, test_set)