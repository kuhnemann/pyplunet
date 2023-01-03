from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import SearchFilter_Job

if TYPE_CHECKING:
    from ..client import PlunetClient


class ReportJob30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def search(self, search_filter_job: Union[SearchFilter_Job, dict]):
        """
        Search for all jobs which fulfill the requirements of the provided search-object.

        :param search_filter_job: SearchFilter_Job

        :return:
        """

        proxy = self.__client.plunet_server.ReportJob30.search

        if type(search_filter_job) != SearchFilter_Job:
            search_filter_job = SearchFilter_Job(**search_filter_job).dict()
        else:
            search_filter_job = search_filter_job.dict()

        return self.__client.make_request(proxy, search_filter_job, unpack_dict=False)
