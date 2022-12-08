from __future__ import annotations
from typing import List, Union

from ..models import SearchFilter_Order, SearchFilter_Quote, SearchFilter_Request

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import PlunetClient

from ..enums import ProjectType


class DataOrder30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_order_language_combinations(self, order_id: int):
        """
        TODO: check return type
        :param order_id:
        :return:
        """
        return self.__client.make_request(
            self.__client.plunet_server.DataOrder30.getLanguageCombination, order_id
        )

    def get_order_id_from_display_string_name(self, order_display_number: str) -> int:
        """
        Takes the order number string, f.ex. O-00123, and returns the order id as an int.

        :param order_display_number:
        :return:
        """
        return self.__client.make_request(
            self.__client.plunet_server.DataOrder30.getOrderID, order_display_number
        )

    def get_order_creation_date(self, order_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataOrder30.getCreationDate, order_id
        )

    def search_for_orders(
        self, search_filter: Union[SearchFilter_Order, dict]
    ) -> List[int]:
        if type(search_filter) != SearchFilter_Order:
            arg = SearchFilter_Order(**search_filter).dict()
        else:
            arg = search_filter.dict()
        data_item = self.__client.make_request(
            self.__client.plunet_server.DataOrder30.search, arg
        )
        return data_item

    def get_order_object(self, order_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataOrder30.getOrderObject, order_id
        )

    def get_order_object_list(self, order_object_ids: List[int]):
        arg = self.__client.plunet_server.DataOrder30.factory.IntegerList(
            order_object_ids
        )
        return self.__client.make_request(
            self.__client.plunet_server.DataOrder30.getOrderObjectList, arg
        )


class DataItem30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_order_item_id_by_language_combi(
        self,
        order_id: int,
        source_lang: str,
        target_lang: str,
        project_type: ProjectType = ProjectType.ORDER,
    ):
        arg = {
            "projectType": project_type.value,
            "projectID": order_id,
            "sourceLanguage": source_lang,
            "targetLanguage": target_lang,
        }

        return self.__client.make_request(
            self.__client.plunet_server.DataItem30.get_ByLanguage, arg, unpack_dict=True
        )

    def get_all_order_item_objects(
        self, order_id: int, project_type: ProjectType = ProjectType.ORDER
    ):

        arg = {"projectType": project_type.value, "projectID": order_id}

        return self.__client.make_request(
            self.__client.plunet_server.DataItem30.getAllItemObjects,
            arg,
            unpack_dict=True,
        )


class DataQuote30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def search_for_quotes(self, search_filter: Union[SearchFilter_Quote, dict]):
        if type(search_filter) != SearchFilter_Quote:
            arg = SearchFilter_Quote(**search_filter).dict()
        else:
            arg = search_filter.dict()

        return self.__client.make_request(
            self.__client.plunet_server.DataQuote30.search, arg
        )

    def get_quote_object_list(self, quote_id_list: List[int]):
        arg = self.__client.plunet_server.DataQuote30.factory.IntegerList(quote_id_list)
        return self.__client.make_request(
            self.__client.plunet_server.DataQuote30.getQuoteObjectList, arg
        )

    def get_quote_object(self, quote_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataQuote30.getQuoteObject, quote_id
        )

    def get_quote_customer_contact_person(self, quote_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataQuote30.getCustomerContactID, quote_id
        )


class DataRequest30:
    def __init__(self, client: PlunetClient):
        self.client = client

    def search_for_requests(self, search_filter: Union[SearchFilter_Request, dict]):
        if type(search_filter) != SearchFilter_Request:
            arg = SearchFilter_Request(**search_filter).dict()
        else:
            arg = search_filter.dict()
        return self.client.make_request(
            self.client.plunet_server.DataRequest30.search, arg
        )

    def get_request_object_list(self, request_id_list: List[int]):
        arg = self.client.plunet_server.DataRequest30.factory.IntegerList(
            request_id_list
        )
        return self.client.make_request(
            self.client.plunet_server.DataRequest30.getRequestObjectList, arg
        )

    def get_request_customer_contact_person(self, request_id: int):
        return self.client.make_request(
            self.client.plunet_server.DataRequest30.getCustomerContactID, request_id
        )
