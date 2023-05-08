from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import IntegerArrayResult, SearchFilter_Customer

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class ReportCustomer30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def search(
        self, search_filter_customer: Union[SearchFilter_Customer, dict]
    ) -> IntegerArrayResult:
        """
        Search for all customers which fulfill the requirements of the provided search-object.


        :param search_filter_customer: SearchFilter_Customer
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.ReportCustomer30.search
        response_model = IntegerArrayResult

        if type(search_filter_customer) != SearchFilter_Customer:
            search_filter_customer = SearchFilter_Customer(
                **search_filter_customer
            ).dict()
        else:
            search_filter_customer = search_filter_customer.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter_customer,
            response_model=response_model,
            unpack_dict=False,
        )
