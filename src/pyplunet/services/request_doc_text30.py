from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from ..client import PlunetClient


class RequestDocText30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def delete(self, request_doc_text_id: int):
        """
        Method to delete a specific request text via requestText id.

        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.delete

        return self.__client.make_request(proxy, request_doc_text_id, unpack_dict=False)

    def get_additional_info(self, request_doc_text_id: int):
        """
        Returns an instance of StringResult, which contains the additional information of the currently fetched request text.

        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.getAdditionalInfo

        return self.__client.make_request(proxy, request_doc_text_id, unpack_dict=False)

    def get_all_by_request_id(self, request_id: int):
        """
        Returns an instance of IntegerArrayResult, which contains a list of request text identifier for a specific request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.getAll_ByRequestID

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_customer_text_id(self, request_doc_text_id: int):
        """
        Returns an instance of IntegerResult, which contains the customer text id.

        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.getCustomerTextID

        return self.__client.make_request(proxy, request_doc_text_id, unpack_dict=False)

    def get_source_text(self, request_doc_text_id: int):
        """
        Method returns an instance of StringResult, which contains the sourcetext of the currently fetched request text.

        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.getSourceText

        return self.__client.make_request(proxy, request_doc_text_id, unpack_dict=False)

    def get_target_text(self, target_language: str, request_doc_text_id: int):
        """
        Method to return the target text, of the currently fetched request text.

        :param target_language: str
        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.getTargetText

        arg = {
            "targetLanguage": target_language,
            "requestDocTextID": request_doc_text_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_word_count(self, request_doc_text_id: int):
        """
        Returns an instance of IntegerResult, which contains the word count of the currently fetched text.

        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.getWordCount

        return self.__client.make_request(proxy, request_doc_text_id, unpack_dict=False)

    def insert(self, request_id: int):
        """
        Method to create an empty request document text.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.insert

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def set_additional_info(self, additional_info: str, request_doc_text_id: int):
        """
        Method to add additional information to the currently fetched request text.

        :param additional_info: str
        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.setAdditionalInfo

        arg = {
            "additionalInfo": additional_info,
            "requestDocTextID": request_doc_text_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_text_id(self, customer_text_id: int, request_doc_text_id: int):
        """
        Method to set the customer text id of the currently fetched request text.

        :param customer_text_id: int
        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.setCustomerTextID

        arg = {
            "customerTextID": customer_text_id,
            "requestDocTextID": request_doc_text_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_source_text(self, source_text: str, request_doc_text_id: int):
        """
        Method to set the source text.

        :param source_text: str
        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.setSourceText

        arg = {"sourceText": source_text, "requestDocTextID": request_doc_text_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_source_text2(
        self, source_text: str, encoding: str, request_doc_text_id: int
    ):
        """
        Method returns an instance of StringResult, which contains the sourcetext of the currently fetched request text.

        :param source_text: str
        :param encoding: str
        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.setSourceText2

        arg = {
            "sourceText": source_text,
            "encoding": encoding,
            "requestDocTextID": request_doc_text_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_word_count(self, word_count: int, request_doc_text_id: int):
        """
        Method to set the word count of the currently fetched request text.

        :param word_count: int
        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.setWordCount

        arg = {"wordCount": word_count, "requestDocTextID": request_doc_text_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, request_doc_text_id: int):
        """
        Commits all changes for the currently selected request text to database.

        :param request_doc_text_id: int

        :return:
        """

        proxy = self.__client.plunet_server.RequestDocText30.update

        return self.__client.make_request(proxy, request_doc_text_id, unpack_dict=False)
