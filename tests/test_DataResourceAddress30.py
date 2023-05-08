from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        IntegerArrayResult,
        AddressIN,
        StringResult
)


from src.pyplunet.enums import (
        AddressType
)


class test_set_DataResourceAddress30(BaseModel):
    address_in: AddressIN
    enable_null_or_empty_values: bool
    address_id: int
    resource_id: int
    state: str
    description: str
    address_type: AddressType
    street2: str
    city: str
    country: str
    external_id: str
    street: str
    zip: str
    name: str

def get_test_set() -> test_set_DataResourceAddress30:
    return test_set_DataResourceAddress30(
            address_in= ,
            enable_null_or_empty_values= ,
            address_id= ,
            resource_id= ,
            state= ,
            description= ,
            address_type= ,
            street2= ,
            city= ,
            country= ,
            external_id= ,
            street= ,
            zip= ,
            name= 
    )


def test_DataResourceAddress30_update(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.update(
                address_in=test_set.address_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_update was successful.")




def test_DataResourceAddress30_delete(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.delete(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_delete was successful.")




def test_DataResourceAddress30_get_state(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_state(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_state failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_state was successful.")




def test_DataResourceAddress30_insert(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.insert(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataResourceAddress30_insert was successful.")




def test_DataResourceAddress30_get_country(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_country(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_country failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_country was successful.")




def test_DataResourceAddress30_set_state(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_state(
                state=test_set.state,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_state failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_state was successful.")




def test_DataResourceAddress30_get_address_type(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_address_type(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_address_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataResourceAddress30_get_address_type was successful.")




def test_DataResourceAddress30_get_description(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_description(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_description was successful.")




def test_DataResourceAddress30_set_description(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_description(
                description=test_set.description,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_description was successful.")




def test_DataResourceAddress30_set_address_type(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_address_type(
                address_type=test_set.address_type,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_address_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_address_type was successful.")




def test_DataResourceAddress30_set_street2(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_street2(
                street2=test_set.street2,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_street2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_street2 was successful.")




def test_DataResourceAddress30_get_street2(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_street2(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_street2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_street2 was successful.")




def test_DataResourceAddress30_set_city(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_city(
                city=test_set.city,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_city failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_city was successful.")




def test_DataResourceAddress30_get_city(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_city(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_city failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_city was successful.")




def test_DataResourceAddress30_set_country(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_country(
                country=test_set.country,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_country failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_country was successful.")




def test_DataResourceAddress30_get_all_addresses(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_all_addresses(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_all_addresses failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataResourceAddress30_get_all_addresses was successful.")




def test_DataResourceAddress30_get_address_id(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_address_id(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_address_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataResourceAddress30_get_address_id was successful.")




def test_DataResourceAddress30_set_office(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_office(
                external_id=test_set.external_id,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_office failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_office was successful.")




def test_DataResourceAddress30_get_street(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_street(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_street failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_street was successful.")




def test_DataResourceAddress30_set_street(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_street(
                street=test_set.street,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_street failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_street was successful.")




def test_DataResourceAddress30_get_zip(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_zip(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_zip failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_zip was successful.")




def test_DataResourceAddress30_get_office(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_office(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_office failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_office was successful.")




def test_DataResourceAddress30_set_zip(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_zip(
                zip=test_set.zip,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_zip failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_zip was successful.")




def test_DataResourceAddress30_get_name1(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_name1(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_name1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_name1 was successful.")




def test_DataResourceAddress30_insert2(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.insert2(
                resource_id=test_set.resource_id,
                address_in=test_set.address_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataResourceAddress30_insert2 was successful.")




def test_DataResourceAddress30_set_name1(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_name1(
                name=test_set.name,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_name1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_name1 was successful.")




def test_DataResourceAddress30_set_name2(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.set_name2(
                name=test_set.name,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_set_name2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataResourceAddress30_set_name2 was successful.")




def test_DataResourceAddress30_get_name2(pc: PlunetClient, test_set: test_set_DataResourceAddress30):
    try:
        resp = pc.resource_address.get_name2(
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataResourceAddress30_get_name2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataResourceAddress30_get_name2 was successful.")



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
        test_DataResourceAddress30_update(pc, test_set)
        test_DataResourceAddress30_delete(pc, test_set)
        test_DataResourceAddress30_get_state(pc, test_set)
        test_DataResourceAddress30_insert(pc, test_set)
        test_DataResourceAddress30_get_country(pc, test_set)
        test_DataResourceAddress30_set_state(pc, test_set)
        test_DataResourceAddress30_get_address_type(pc, test_set)
        test_DataResourceAddress30_get_description(pc, test_set)
        test_DataResourceAddress30_set_description(pc, test_set)
        test_DataResourceAddress30_set_address_type(pc, test_set)
        test_DataResourceAddress30_set_street2(pc, test_set)
        test_DataResourceAddress30_get_street2(pc, test_set)
        test_DataResourceAddress30_set_city(pc, test_set)
        test_DataResourceAddress30_get_city(pc, test_set)
        test_DataResourceAddress30_set_country(pc, test_set)
        test_DataResourceAddress30_get_all_addresses(pc, test_set)
        test_DataResourceAddress30_get_address_id(pc, test_set)
        test_DataResourceAddress30_set_office(pc, test_set)
        test_DataResourceAddress30_get_street(pc, test_set)
        test_DataResourceAddress30_set_street(pc, test_set)
        test_DataResourceAddress30_get_zip(pc, test_set)
        test_DataResourceAddress30_get_office(pc, test_set)
        test_DataResourceAddress30_set_zip(pc, test_set)
        test_DataResourceAddress30_get_name1(pc, test_set)
        test_DataResourceAddress30_insert2(pc, test_set)
        test_DataResourceAddress30_set_name1(pc, test_set)
        test_DataResourceAddress30_set_name2(pc, test_set)
        test_DataResourceAddress30_get_name2(pc, test_set)