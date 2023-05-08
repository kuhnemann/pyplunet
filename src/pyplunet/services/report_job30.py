from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import IntegerArrayResult, SearchFilter_Job

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class ReportJob30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def search(
        self, search_filter_job: Union[SearchFilter_Job, dict]
    ) -> IntegerArrayResult:
        """
        Search for all jobs which fulfill the requirements of the provided search-object.


        :param search_filter_job: SearchFilter_Job
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.ReportJob30.search
        response_model = IntegerArrayResult

        if type(search_filter_job) != SearchFilter_Job:
            search_filter_job = SearchFilter_Job(**search_filter_job).dict()
        else:
            search_filter_job = search_filter_job.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter_job,
            response_model=response_model,
            unpack_dict=False,
        )
