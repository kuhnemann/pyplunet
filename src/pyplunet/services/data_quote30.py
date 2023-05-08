from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType, ProjectClassType
from ..models import (
    DateResult,
    DoubleResult,
    IntegerArrayResult,
    IntegerList,
    IntegerResult,
    QuoteIN,
    QuoteListResult,
    QuoteResult,
    Result,
    SearchFilter_Quote,
    StringResult,
    TemplateListResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataQuote30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def add_language_combination(
        self, source_language: str, target_language: str, quote_id: int
    ) -> IntegerResult:
        """
        Adds a language combination to the specified quote.
        All language descriptions were expected in English language or as ISO-Code.
        Returns an instance of Result.


        :param source_language: str
        :param target_language: str
        :param quote_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.addLanguageCombination
        response_model = IntegerResult

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "quoteID": quote_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_rate(self, quote_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the rate


        :param quote_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getRate
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_request_id(self, quote_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the requestId


        :param quote_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getRequestId
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_project_name(self, project_name: str, quote_id: int) -> Result:
        """
        Sets the project name.


        :param project_name: str
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectName
        response_model = Result

        arg = {"ProjectName": project_name, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_subject(self, quote_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the subject.


        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getSubject
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_subject(self, subject: str, quote_id: int) -> Result:
        """
        Sets the subject


        :param subject: str
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setSubject
        response_model = Result

        arg = {"subject": subject, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_project_name(self, quote_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the project name


        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectName
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_request_id(self, quote_id: int, request_id: int) -> Result:
        """
        Method to set the project related request ID.


        :param quote_id: int
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setRequestID
        response_model = Result

        arg = {"quoteID": quote_id, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_creation_date(self, quote_id: int) -> DateResult:
        """
        Returns an instance of DateResult, which contains the creation date


        :param quote_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getCreationDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def update(
        self, quote_in: Union[QuoteIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        updates the quote by the transfered object
        Use EnableNullOrEmptyValues to decide if Null or empty Strings are saved
        into Plunet or ignored.


        :param quote_in: QuoteIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.update
        response_model = Result

        if type(quote_in) != QuoteIN:
            quote_in = QuoteIN(**quote_in).dict()
        else:
            quote_in = quote_in.dict()

        arg = {
            "QuoteIN": quote_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete(self, quote_id: int) -> Result:
        """
        Method to delete an quote via ID


        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert(
        self,
    ) -> IntegerResult:
        """
        Method to create a new, empty quote.
        The method will return an instance
        of IntegerResult, which contains the quote id.
        Further api calls via this port will maninpulate this quote
        (except methods with an quote id as parameter ),
        until another quote is fetched or the session is invalidated.


        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def search(
        self, search_filter: Union[SearchFilter_Quote, dict]
    ) -> IntegerArrayResult:
        """
        Search implementation to filter for any existing quotes based on
        specific criteria.


        :param search_filter: SearchFilter_Quote
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataQuote30.search
        response_model = IntegerArrayResult

        if type(search_filter) != SearchFilter_Quote:
            search_filter = SearchFilter_Quote(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter,
            response_model=response_model,
            unpack_dict=False,
        )

    def request_order(self, quote_id: int) -> Result:
        """
        Request and order to the provided quoteID


        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.requestOrder
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def request_quote(self, project_class_type: Union[ProjectClassType, int]) -> Result:
        """
        Request a new quote


        :param project_class_type: ProjectClassType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.requestQuote
        response_model = Result

        if type(project_class_type) == ProjectClassType:
            project_class_type = project_class_type.value
        elif type(project_class_type) == int:
            project_class_type = project_class_type
        else:
            project_class_type = int(project_class_type)

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=project_class_type,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_currency(self, quote_id: int) -> StringResult:
        """
        Returns the currency


        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getCurrency
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_reference_number(self, quote_id: int, reference: str) -> Result:
        """
        Method set reference number for quote by quoteID.


        :param quote_id: int
        :param reference: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setReferenceNumber
        response_model = Result

        arg = {"quoteID": quote_id, "reference": reference}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_project_category(
        self, project_category: str, system_language_code: str, quote_id: int
    ) -> Result:
        """
        Set the the project category of the quote, specified by its name.


        For a full list of your project categories, see Admin | Miscellaneous |
        Project category.


        :param project_category: str
        :param system_language_code: str
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectCategory
        response_model = Result

        arg = {
            "projectCategory": project_category,
            "systemLanguageCode": system_language_code,
            "quoteID": quote_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_project_category(
        self, system_language_code: str, quote_id: int
    ) -> StringResult:
        """
        Get the name (in the language specified) of the project category of
        the quote.

        For a full list of your project categories, see Admin | Miscellaneous |
        Project category.


        :param system_language_code: str
        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectCategory
        response_model = StringResult

        arg = {"systemLanguageCode": system_language_code, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_customer_id(self, customer_id: int, quote_id: int) -> Result:
        """
        Sets the customerID


        :param customer_id: int
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setCustomerID
        response_model = Result

        arg = {"customerID": customer_id, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def deregister_callback_observer(self, quote_id: int) -> Result:
        """
        Deletes a observer.
        observer can only deleted by the user who has created them.


        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.deregisterCallback_Observer
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def register_callback_notify(
        self,
        server_authentication_string: str,
        server_address: str,
        event_type: Union[EventType, int],
    ) -> Result:
        """
        Register to get notified when the specified EventType occurs
        for any quote.

        If the EventType occurs PBM will call the callback web service,
        which is hosted within your environment. Please check
        CallbackQuote30 for the exact specification for this service.
        (each user can only create one notifier per event)


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackQuote30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.registerCallback_Notify
        response_model = Result

        if type(event_type) == EventType:
            event_type = event_type.value
        elif type(event_type) == int:
            event_type = event_type
        else:
            event_type = int(event_type)

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "EventType": event_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def deregister_callback_notify(self, event_type: Union[EventType, int]) -> Result:
        """
        Deletes an already registered notify request
        (notify requests can only be deleted by the user who has created them)


        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.deregisterCallback_Notify
        response_model = Result

        if type(event_type) == EventType:
            event_type = event_type.value
        elif type(event_type) == int:
            event_type = event_type
        else:
            event_type = int(event_type)

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=event_type,
            response_model=response_model,
            unpack_dict=False,
        )

    def register_callback_observer(
        self, server_authentication_string: str, server_address: str, quote_id: int
    ) -> Result:
        """
        Register to observe a specific object for any supported
        EventType.

        As soon as any supported event occurs, PBM will call the callback web
        service, which is hosted within your environment. Please check
        CallbackQuote30 for the exact specification for this service.
        (each user can only create one observer per id)


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackQuote30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.registerCallback_Observer
        response_model = Result

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "QuoteID": quote_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert_by_template(
        self, quote_in: Union[QuoteIN, dict], template_id: int
    ) -> IntegerResult:
        """
        Method to create a order depending on the transfered templateID and QuoteIN object.
        (object values will overwrite information set by the template)
        #setQuoteID(int) will be ignored as it
        will be auto generated by the system.


        :param quote_in: QuoteIN
        :param template_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.insert_byTemplate
        response_model = IntegerResult

        if type(quote_in) != QuoteIN:
            quote_in = QuoteIN(**quote_in).dict()
        else:
            quote_in = quote_in.dict()

        arg = {"QuoteIN": quote_in, "TemplateID": template_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_reference_number(self, quote_id: int) -> StringResult:
        """
        Method returns the reference number by quote ID.


        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getReferenceNumber
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_project_manager_memo(self, quote_id: int) -> StringResult:
        """
        Method returns project-manager memo for order by quoteID.


        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectManagerMemo
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_project_manager_memo(self, quote_id: int, memo: str) -> Result:
        """
        Method set the project-manager Memo for order by quoteID.


        :param quote_id: int
        :param memo: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectManagerMemo
        response_model = Result

        arg = {"quoteID": quote_id, "memo": memo}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_status(self, quote_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the QuoteStatusType.


        :param quote_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, quote_id: int) -> Result:
        """
        Sets the QuoteStatusType.


        :param status: int
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setStatus
        response_model = Result

        arg = {"Status": status, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_projectmanager_id(self, quote_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the resource id.


        :param quote_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectmanagerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_projectmanager_id(self, resource_id: int, quote_id: int) -> Result:
        """
        Sets the resourceID of the project manager to the given quote.


        :param resource_id: int
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectmanagerID
        response_model = Result

        arg = {"resourceID": resource_id, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_template_list(
        self,
    ) -> TemplateListResult:
        """
        Method returns an instance of TemplateListResult, which contains a list
        of template objects which can be accessed by the user.


        :return: TemplateListResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getTemplateList
        response_model = TemplateListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_customer_contact_id(
        self, customer_contact_id: int, quote_id: int
    ) -> Result:
        """
        Sets the customer contact ID for the currently selected project.


        :param customer_contact_id: int
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setCustomerContactID
        response_model = Result

        arg = {"customerContactID": customer_contact_id, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_customer_contact_id(self, quote_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the customer
        contact id.


        :param quote_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getCustomerContactID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_project_status(self, quote_id: int, project_status: int) -> Result:
        """
        Method allows to set the ArchivStatus to ARCHIVED (3).
        Other status changes are not supported due to underlying automated workflows.
        Please note that the current status must be either COMPLETED(6) or COMPLETED_ARCHIVABLE(2).


        :param quote_id: int
        :param project_status: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectStatus
        response_model = Result

        arg = {"quoteID": quote_id, "projectStatus": project_status}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_project_status(self, quote_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the
        ArchivStatus.


        :param quote_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_quote_object(self, quote_id: int) -> QuoteResult:
        """
        Method returns an instance of QuoteResult, which contains an instance of Quote.


        :param quote_id: int
        :return: QuoteResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteObject
        response_model = QuoteResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_quote_document(self, quote_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the relative network path to the quote document.
        Files can also directly be downloaded as file content over
        DataDocument30.download_Document(String, int, int, String)


        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteDocument
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_creation_date(self, date: datetime, quote_id: int) -> Result:
        """
        Sets the creation date


        :param date: datetime
        :param quote_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setCreationDate
        response_model = Result

        arg = {"date": date, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_quote_object2(self, quote_number: str) -> QuoteResult:
        """
        Method returns an instance of QuoteResult, which contains an instance of Quote.


        :param quote_number: str
        :return: QuoteResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteObject2
        response_model = QuoteResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_number,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_id_first_item(self, quote_id: int) -> IntegerResult:
        """
        If the currently selected quote is already changed to an order, this
        method returns the order ID by checking the first quote item.

        Returns an instance of IntegerResult.


        :param quote_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getOrderIDFirstItem
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_quote_no_for_view(self, quote_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the formatted quote number,
        which appears in the forms used by BusinessManager.


        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteNo_for_View
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_quote_object_list(
        self, quote_id_list: Union[IntegerList, dict]
    ) -> QuoteListResult:
        """
        Method returns an instance of QuoteListResult, which contains a list of quote objects.


        :param quote_id_list: IntegerList
        :return: QuoteListResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteObjectList
        response_model = QuoteListResult

        if type(quote_id_list) != IntegerList:
            quote_id_list = IntegerList(**quote_id_list).dict()
        else:
            quote_id_list = quote_id_list.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id_list,
            response_model=response_model,
            unpack_dict=False,
        )

    def create_quote_document(
        self, template: str, format_id: int, quote_id: int
    ) -> StringResult:
        """
        Method creates a quote document as rtf-file and returns the unc path where the file is located.
        Files can also directly be uploaded as file content over
        DataDocument30.upload_Document(String, int, int, byte[], String, long)


        :param template: str
        :param format_id: int
        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.createQuoteDocument
        response_model = StringResult

        arg = {"template": template, "formatId": format_id, "quoteID": quote_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert2(self, quote_in: Union[QuoteIN, dict]) -> IntegerResult:
        """
        Method to create a quote depending on the transfered object


        :param quote_in: QuoteIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.insert2
        response_model = IntegerResult

        if type(quote_in) != QuoteIN:
            quote_in = QuoteIN(**quote_in).dict()
        else:
            quote_in = quote_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_external_id(self, quote_id: int, external_id: str) -> Result:
        """
        Methode set External ID for Quote by quoteID


        :param quote_id: int
        :param external_id: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataQuote30.setExternalID
        response_model = Result

        arg = {"quoteID": quote_id, "externalID": external_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_external_id(self, quote_id: int) -> StringResult:
        """
        Method retuns ExternalID from Qute by quoteID


        :param quote_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getExternalID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_quote_id(self, display_no: str) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains the Quote ID.


        :param display_no: str
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=display_no,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_customer_id(self, quote_id: int) -> IntegerResult:
        """
        Returns an instance of customer id, which contains the customer id


        :param quote_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataQuote30.getCustomerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=quote_id,
            response_model=response_model,
            unpack_dict=False,
        )
