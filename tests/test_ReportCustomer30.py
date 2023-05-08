from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        IntegerArrayResult,
        SearchFilter_Customer
)



class test_set_ReportCustomer30(BaseModel):
    search_filter_customer: SearchFilter_Customer

def get_test_set() -> test_set_ReportCustomer30:
    return test_set_ReportCustomer30(
            search_filter_customer= 
    )


def test_ReportCustomer30_search(pc: PlunetClient, test_set: test_set_ReportCustomer30):
    try:
        resp = pc.report_customer.search(
                search_filter_customer=test_set.search_filter_customer
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_ReportCustomer30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_ReportCustomer30_search was successful.")



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
        test_ReportCustomer30_search(pc, test_set)