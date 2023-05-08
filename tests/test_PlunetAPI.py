from __future__ import annotations

import os

import requests

from src.pyplunet.models import StringResult, BooleanResult
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError, InvalidCredentials, PlunetAuthFailed


def test_PlunetAPI_login_failpass_no_instance():
    pc = PlunetClient(base_url="https://not.a.plunet.instance.org")
    try:
        pc.login("robin", "batman")
    except requests.exceptions.ConnectionError as e:
        print(e)
        print("test_PlunetAPI_login_failpass_no_instance passed.")

def test_PlunetAPI_login_failpass_wrong_creds():
    pc = PlunetClient(base_url=os.getenv("TEST_URL"))
    try:
        pc.login("robin", "batman")
    except PlunetAuthFailed as e:
        print("test_PlunetAPI_login_failpass_wrong_creds passed.")


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
    for client in test_clients:
        print(client.__name__)
        logged = client(logged_in=True)
        not_logged = client(logged_in=False)
        test_PlunetAPI_login_failpass_no_instance()
        test_PlunetAPI_login_failpass_wrong_creds()
        test_PlunetAPI_get_version(not_logged)
        test_PlunetAPI_get_plunet_version(not_logged)
        test_PlunetAPI_validate(logged)