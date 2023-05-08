from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        IntegerArrayResult,
        SearchFilter_Job
)



class test_set_ReportJob30(BaseModel):
    search_filter_job: SearchFilter_Job

def get_test_set() -> test_set_ReportJob30:
    return test_set_ReportJob30(
            search_filter_job= 
    )


def test_ReportJob30_search(pc: PlunetClient, test_set: test_set_ReportJob30):
    try:
        resp = pc.report_job.search(
                search_filter_job=test_set.search_filter_job
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_ReportJob30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_ReportJob30_search was successful.")



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
        test_ReportJob30_search(pc, test_set)