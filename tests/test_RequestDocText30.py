from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        IntegerArrayResult,
        Result,
        IntegerResult,
        StringResult
)



class test_set_RequestDocText30(BaseModel):
    request_doc_text_id: int
    request_id: int
    additional_info: str
    customer_text_id: int
    target_language: str
    word_count: int
    source_text: str
    encoding: str

def get_test_set() -> test_set_RequestDocText30:
    return test_set_RequestDocText30(
            request_doc_text_id= ,
            request_id= ,
            additional_info= ,
            customer_text_id= ,
            target_language= ,
            word_count= ,
            source_text= ,
            encoding= 
    )


def test_RequestDocText30_update(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.update(
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_RequestDocText30_update was successful.")




def test_RequestDocText30_delete(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.delete(
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_RequestDocText30_delete was successful.")




def test_RequestDocText30_insert(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.insert(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_RequestDocText30_insert was successful.")




def test_RequestDocText30_set_additional_info(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.set_additional_info(
                additional_info=test_set.additional_info,
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_set_additional_info failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_RequestDocText30_set_additional_info was successful.")




def test_RequestDocText30_set_customer_text_id(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.set_customer_text_id(
                customer_text_id=test_set.customer_text_id,
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_set_customer_text_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_RequestDocText30_set_customer_text_id was successful.")




def test_RequestDocText30_get_customer_text_id(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.get_customer_text_id(
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_get_customer_text_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_RequestDocText30_get_customer_text_id was successful.")




def test_RequestDocText30_get_all_by_request_id(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.get_all_by_request_id(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_get_all_by_request_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_RequestDocText30_get_all_by_request_id was successful.")




def test_RequestDocText30_get_additional_info(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.get_additional_info(
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_get_additional_info failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_RequestDocText30_get_additional_info was successful.")




def test_RequestDocText30_get_target_text(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.get_target_text(
                target_language=test_set.target_language,
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_get_target_text failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_RequestDocText30_get_target_text was successful.")




def test_RequestDocText30_set_word_count(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.set_word_count(
                word_count=test_set.word_count,
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_set_word_count failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_RequestDocText30_set_word_count was successful.")




def test_RequestDocText30_set_source_text(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.set_source_text(
                source_text=test_set.source_text,
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_set_source_text failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_RequestDocText30_set_source_text was successful.")




def test_RequestDocText30_get_source_text(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.get_source_text(
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_get_source_text failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_RequestDocText30_get_source_text was successful.")




def test_RequestDocText30_get_word_count(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.get_word_count(
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_get_word_count failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_RequestDocText30_get_word_count was successful.")




def test_RequestDocText30_set_source_text2(pc: PlunetClient, test_set: test_set_RequestDocText30):
    try:
        resp = pc.request_doc_text.set_source_text2(
                source_text=test_set.source_text,
                encoding=test_set.encoding,
                request_doc_text_id=test_set.request_doc_text_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_RequestDocText30_set_source_text2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_RequestDocText30_set_source_text2 was successful.")



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
        test_RequestDocText30_update(pc, test_set)
        test_RequestDocText30_delete(pc, test_set)
        test_RequestDocText30_insert(pc, test_set)
        test_RequestDocText30_set_additional_info(pc, test_set)
        test_RequestDocText30_set_customer_text_id(pc, test_set)
        test_RequestDocText30_get_customer_text_id(pc, test_set)
        test_RequestDocText30_get_all_by_request_id(pc, test_set)
        test_RequestDocText30_get_additional_info(pc, test_set)
        test_RequestDocText30_get_target_text(pc, test_set)
        test_RequestDocText30_set_word_count(pc, test_set)
        test_RequestDocText30_set_source_text(pc, test_set)
        test_RequestDocText30_get_source_text(pc, test_set)
        test_RequestDocText30_get_word_count(pc, test_set)
        test_RequestDocText30_set_source_text2(pc, test_set)