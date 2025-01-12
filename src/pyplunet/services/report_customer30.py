from __future__ import annotations

from typing import TYPE_CHECKING, Union


from ..models import SearchFilter_Customer, IntegerArrayResult


if TYPE_CHECKING:
    from ..client import PlunetClient


class ReportCustomer30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def search(
        self, search_filter_customer: Union[SearchFilter_Customer, dict]
    ) -> IntegerArrayResult:
        """
        Deprecated. A better solution is already added at DataCustomer30.search(String, SearchFilter_Customer)
        Search for all customers which fulfill the requirements of the provided search-object.


        :param search_filter_customer: SearchFilter_Customer
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.ReportCustomer30.search
        response_model = IntegerArrayResult

        if type(search_filter_customer) is not SearchFilter_Customer:
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
