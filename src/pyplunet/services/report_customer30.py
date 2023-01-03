from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import SearchFilter_Customer

if TYPE_CHECKING:
    from ..client import PlunetClient


class ReportCustomer30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def search(self, search_filter_customer: Union[SearchFilter_Customer, dict]):
        """
        Search for all customers which fulfill the requirements of the provided search-object.

        :param search_filter_customer: SearchFilter_Customer

        :return:
        """

        proxy = self.__client.plunet_server.ReportCustomer30.search

        if type(search_filter_customer) != SearchFilter_Customer:
            search_filter_customer = SearchFilter_Customer(
                **search_filter_customer
            ).dict()
        else:
            search_filter_customer = search_filter_customer.dict()

        return self.__client.make_request(
            proxy, search_filter_customer, unpack_dict=False
        )
