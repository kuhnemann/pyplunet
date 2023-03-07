from __future__ import annotations

from src.pyplunet.models import StringResult, BooleanResult
from tests import get_test_client, get_test_client_inmemory_cache, get_test_configured_sql_cache, get_test_client_no_caching
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError, InvalidCredentials


def test_PlunetAPI_get_version(pc: PlunetClient):
    try:
        resp = pc.get_version()

    except PlunetAPIError as e:
        error = e
        print(f"test_PlunetAPI_get_version failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == float
    print(f"test_PlunetAPI_get_version was successful.")


def test_PlunetAPI_get_plunet_version(pc: PlunetClient):
    try:
        resp = pc.get_plunet_version()

    except PlunetAPIError as e:
        error = e
        print(f"test_PlunetAPI_get_plunet_version failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_PlunetAPI_get_plunet_version was successful.")

def test_PlunetAPI_validate(pc: PlunetClient):
    try:
        resp = pc.validate("user", "password")
        print(resp)
    except InvalidCredentials as resp:
        print(f"test_PlunetAPI_validate was successful.")
        return
    except PlunetAPIError as e:
        error = e
        print(f"test_PlunetAPI_validate failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == BooleanResult
    print(f"test_PlunetAPI_validate was successful.")

if __name__ == '__main__':
    test_clients = [get_test_client, get_test_client_inmemory_cache, get_test_configured_sql_cache, get_test_client_no_caching]
    for client in test_clients:
        print(client.__name__)
        logged = client(logged_in=True)
        not_logged = client(logged_in=False)
        test_PlunetAPI_get_version(not_logged)
        test_PlunetAPI_get_plunet_version(not_logged)
        test_PlunetAPI_validate(logged)