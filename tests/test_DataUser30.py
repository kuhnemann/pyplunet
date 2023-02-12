from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        UserListResult,
        UserResult
)



class test_set_DataUser30(BaseModel):
    user_id: int
    resource_id: int
    user_login_name: str

def get_test_set() -> test_set_DataUser30:
    return test_set_DataUser30(
            user_id=33,
            resource_id=1,
            user_login_name="Paul Leiter"
    )


def test_DataUser30_get_user_by_id(pc: PlunetClient, test_set: test_set_DataUser30):
    try:
        resp = pc.user.get_user_by_id(
                user_id=test_set.user_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataUser30_get_user_by_id failed with error {type(e)}: {e.status_message} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == UserResult
    print(f"test_DataUser30_get_user_by_id was successful.")




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



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()

    test_DataUser30_get_user_list_by_resource_id(pc, test_set)
    test_DataUser30_get_user_by_login_name(pc, test_set)
    test_DataUser30_get_user_by_id(pc, test_set)