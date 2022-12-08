from __future__ import annotations
from typing import List, Union

from zeep.helpers import serialize_object

from ..models import (
    CustomerContactIN,
    CustomerContactObject,
    CustomerObject,
    CustomerPaymentInformation,
    SearchFilter_Customer,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataCustomer30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_customer_object(self, customer_id: int) -> CustomerObject:
        return self.__client.make_request(
            self.__client.plunet_server.DataCustomer30.getCustomerObject, customer_id
        )

    def get_customer_payment_information(
        self, customer_id: int
    ) -> CustomerPaymentInformation:
        data = self.__client.make_request(
            self.__client.plunet_server.DataCustomer30.getPaymentInformation,
            customer_id,
        )
        return CustomerPaymentInformation(**serialize_object(data, dict))


class DataCustomerContact30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_all_customer_contact_objects(
        self, customer_id: int
    ) -> List[CustomerContactObject]:
        """
        :param customer_id: int
        :return: List of customer objects
        """
        return self.__client.make_request(
            self.__client.plunet_server.DataCustomerContact30.getAllContactObjects,
            customer_id,
        )

    def get_all_customer_contact_ids(self, customer_id: int) -> List[int]:
        """
        :param customer_id: int
        :return: list of customer IDs
        """
        return self.__client.make_request(
            self.__client.plunet_server.DataCustomerContact30.getAllContacts,
            customer_id,
        )

    def get_customer_contact_object(self, contact_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataCustomerContact30.getContactObject,
            contact_id,
        )

    def update_customer_contact(self, contact_in: CustomerContactIN):

        arg = {"CustomerContact": contact_in.dict(), "enabled": False}
        return self.__client.make_request(
            self.__client.plunet_server.DataCustomerContact30.update,
            arg,
            unpack_dict=True,
        )


class ReportCustomer30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def search_for_customers(
        self, search_filter: Union[SearchFilter_Customer, dict]
    ) -> list:
        if type(search_filter) != SearchFilter_Customer:
            arg = SearchFilter_Customer(**search_filter).dict()
        else:
            arg = search_filter.dict()
        return self.__client.make_request(
            self.__client.plunet_server.ReportCustomer30.search, arg
        )
