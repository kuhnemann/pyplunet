from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        UserResult,
        UserListResult
)



class test_set_DataUser30(BaseModel):
    user_login_name: str
    resource_id: int
    user_id: int

def get_test_set() -> test_set_DataUser30:
    return test_set_DataUser30(
            user_login_name= ,
            resource_id= ,
            user_id= 
    )


def test_DataUser30_get_user_by_login_name(pc: PlunetClient, test_set: test_set_DataUser30):
    try:
        resp = pc.user.get_user_by_login_name(
                user_login_name=test_set.user_login_name
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataUser30_get_user_by_login_name failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == UserResult
    print(f"test_DataUser30_get_user_by_login_name was successful.")




def test_DataUser30_get_user_list_by_resource_id(pc: PlunetClient, test_set: test_set_DataUser30):
    try:
        resp = pc.user.get_user_list_by_resource_id(
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataUser30_get_user_list_by_resource_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == UserListResult
    print(f"test_DataUser30_get_user_list_by_resource_id was successful.")




def test_DataUser30_get_user_by_id(pc: PlunetClient, test_set: test_set_DataUser30):
    try:
        resp = pc.user.get_user_by_id(
                user_id=test_set.user_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataUser30_get_user_by_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == UserResult
    print(f"test_DataUser30_get_user_by_id was successful.")



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
        test_DataUser30_get_user_by_login_name(pc, test_set)
        test_DataUser30_get_user_list_by_resource_id(pc, test_set)
        test_DataUser30_get_user_by_id(pc, test_set)