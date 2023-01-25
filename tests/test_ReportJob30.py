from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        SearchFilter_Job,
        IntegerArrayResult
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
        input(type(e))
        return
    assert type(resp) == IntegerArrayResult



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()
    test_ReportJob30_search(pc, test_set)