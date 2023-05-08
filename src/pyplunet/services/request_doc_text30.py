from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import IntegerArrayResult, IntegerResult, Result, StringResult

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class RequestDocText30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def update(self, request_doc_text_id: int) -> Result:
        """
        Commits all changes for the currently selected request text to database. Returns an instance of Result.


        :param request_doc_text_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.RequestDocText30.update
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_doc_text_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def delete(self, request_doc_text_id: int) -> Result:
        """
        Method to delete a specific request text via requestText id.
        Returns an instance of Result, which contains status information.
        No update-call is required to commit changes to the database.


        :param request_doc_text_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.RequestDocText30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_doc_text_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert(self, request_id: int) -> IntegerResult:
        """
        Method to create an empty request document text.
        This method will return an instance of IntegerResult,
        which contains the identifier of the created text.
        Further api calls via this port will manipulate this text (except methods with a requestDocTextID as parameter ),
        until another text is fetched or the session is invalidated


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.RequestDocText30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_additional_info(
        self, additional_info: str, request_doc_text_id: int
    ) -> Result:
        """
        Method to add additional information to the currently fetched request text.
        Returns an instance of Result.


        :param additional_info: str
        :param request_doc_text_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.RequestDocText30.setAdditionalInfo
        response_model = Result

        arg = {
            "additionalInfo": additional_info,
            "requestDocTextID": request_doc_text_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_customer_text_id(
        self, customer_text_id: int, request_doc_text_id: int
    ) -> Result:
        """
        Method to set the customer text id of the currently fetched request text.
        This value is an external identifier,
        which is available for free use.
        Returns an instance of Result.


        :param customer_text_id: int
        :param request_doc_text_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.RequestDocText30.setCustomerTextID
        response_model = Result

        arg = {
            "customerTextID": customer_text_id,
            "requestDocTextID": request_doc_text_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_customer_text_id(self, request_doc_text_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the customer text id.


        :param request_doc_text_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.RequestDocText30.getCustomerTextID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_doc_text_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_all_by_request_id(self, request_id: int) -> IntegerArrayResult:
        """
        Returns an instance of IntegerArrayResult, which contains a list of request text identifier for a specific request.


        :param request_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.RequestDocText30.getAll_ByRequestID
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_additional_info(self, request_doc_text_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the additional information of the currently fetched request text.


        :param request_doc_text_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.RequestDocText30.getAdditionalInfo
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_doc_text_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_target_text(
        self, target_language: str, request_doc_text_id: int
    ) -> StringResult:
        """
        Method to return the target text, of the currently fetched request text.
        Method will return an instance of StringResult, which contains
        the target text for a specific language.
        System will search the target file within the target-folder of the order item.
        All language descriptions were expected in english language or as ISO-Code.


        :param target_language: str
        :param request_doc_text_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.RequestDocText30.getTargetText
        response_model = StringResult

        arg = {
            "targetLanguage": target_language,
            "requestDocTextID": request_doc_text_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_word_count(self, word_count: int, request_doc_text_id: int) -> Result:
        """
        Method to set the word count of the currently fetched request text.
        Returns an instance of Result.


        :param word_count: int
        :param request_doc_text_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.RequestDocText30.setWordCount
        response_model = Result

        arg = {"wordCount": word_count, "requestDocTextID": request_doc_text_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_source_text(self, source_text: str, request_doc_text_id: int) -> Result:
        """
        Method to set the source text.
        Returns an instance of Result.


        :param source_text: str
        :param request_doc_text_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.RequestDocText30.setSourceText
        response_model = Result

        arg = {"sourceText": source_text, "requestDocTextID": request_doc_text_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_source_text(self, request_doc_text_id: int) -> StringResult:
        """
        Method returns an instance of StringResult, which contains the sourcetext of the currently fetched request text.


        :param request_doc_text_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.RequestDocText30.getSourceText
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_doc_text_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_word_count(self, request_doc_text_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the word count of the currently fetched text.


        :param request_doc_text_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.RequestDocText30.getWordCount
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_doc_text_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_source_text2(
        self, source_text: str, encoding: str, request_doc_text_id: int
    ) -> Result:
        """
        Method returns an instance of StringResult, which contains the sourcetext of the currently fetched request text.
        With the encoding parameter, it is possible to choose the encoding type for the created source file.
        Valid encoding:

        UTF-8
        UTF-16LE
        UTF-16BE
        ANSI


        :param source_text: str
        :param encoding: str
        :param request_doc_text_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.RequestDocText30.setSourceText2
        response_model = Result

        arg = {
            "sourceText": source_text,
            "encoding": encoding,
            "requestDocTextID": request_doc_text_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )
