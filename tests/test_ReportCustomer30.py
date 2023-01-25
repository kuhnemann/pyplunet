from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        SearchFilter_Customer,
        IntegerArrayResult
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
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()
    test_ReportCustomer30_search(pc, test_set)