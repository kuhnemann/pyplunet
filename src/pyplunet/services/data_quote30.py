from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType, ProjectClassType
from ..models import IntegerList, QuoteIN, SearchFilter_Quote

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataQuote30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def add_language_combination(
        self, source_language: str, target_language: str, quote_id: int
    ):
        """
        Adds a language combination to the specified quote.

        :param source_language: str
        :param target_language: str
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.addLanguageCombination

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "quoteID": quote_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def create_quote_document(self, template: str, format_id: int, quote_id: int):
        """
        Method creates a quote document as rtf-file and returns the unc path where the file is located.

        :param template: str
        :param format_id: int
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.createQuoteDocument

        arg = {"template": template, "formatId": format_id, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete(self, quote_id: int):
        """
        Method to delete an quote via ID

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.delete

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def deregister_callback_notify(self, event_type: EventType):
        """
        Deletes an already registered notify request(notify requests can only be deleted by the user who has created them)

        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.deregisterCallback_Notify

        return self.__client.make_request(proxy, event_type.value, unpack_dict=False)

    def deregister_callback_observer(self, quote_id: int):
        """
        Deletes a observer.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.deregisterCallback_Observer

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_creation_date(self, quote_id: int):
        """
        Returns an instance of DateResult, which contains the creation date

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getCreationDate

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_currency(self, quote_id: int):
        """
        Returns the currency

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getCurrency

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_customer_contact_id(self, quote_id: int):
        """
        Returns an instance of IntegerResult, which contains the customercontact id.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getCustomerContactID

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_customer_id(self, quote_id: int):
        """
        Returns an instance of customer id, which contains the customer id

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getCustomerID

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_external_id(self, quote_id: int):
        """
        Method retuns ExternalID from Qute by quoteID

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getExternalID

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_order_id_first_item(self, quote_id: int):
        """
        If the currently selected quote is already changed to an order, thismethod returns the order ID by checking the first quote item.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getOrderIDFirstItem

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_project_category(self, system_language_code: str, quote_id: int):
        """
        Get the name (in the language specified) of the project category ofthe quote.

        :param system_language_code: str
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectCategory

        arg = {"systemLanguageCode": system_language_code, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_projectmanager_id(self, quote_id: int):
        """
        Returns an instance of IntegerResult, which contains the resource id.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectmanagerID

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_project_manager_memo(self, quote_id: int):
        """
        Method returns project-manager memo for order by quoteID.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectManagerMemo

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_project_name(self, quote_id: int):
        """
        Returns an instance of StringResult, which contains the project name

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectName

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_project_status(self, quote_id: int):
        """
        Returns an instance of IntegerResult, which contains theArchivStatus.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getProjectStatus

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_quote_document(self, quote_id: int):
        """
        Returns an instance of StringResult, which contains the relative network path to the quote document.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteDocument

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_quote_id(self, display_no: str):
        """
        Method returns an instance of IntegerResult, which contains the Quote ID.

        :param display_no: str

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteID

        return self.__client.make_request(proxy, display_no, unpack_dict=False)

    def get_quote_no_for_view(self, quote_id: int):
        """
        Returns an instance of StringResult, which contains the formatted quote number,which appears in the forms used by BusinessManager.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteNo_for_View

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_quote_object(self, quote_id: int):
        """
        Method returns an instance of QuoteResult, which contains an instance of Quote.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteObject

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_quote_object2(self, quote_number: str):
        """
        Method returns an instance of QuoteResult, which contains an instance of Quote.

        :param quote_number: str

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteObject2

        return self.__client.make_request(proxy, quote_number, unpack_dict=False)

    def get_quote_object_list(self, quote_id_list: Union[IntegerList, dict]):
        """
        Method returns an instance of QuoteListResult, which contains a list of quote objects.

        :param quote_id_list: IntegerList

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getQuoteObjectList

        if type(quote_id_list) != IntegerList:
            quote_id_list = IntegerList(**quote_id_list).dict()
        else:
            quote_id_list = quote_id_list.dict()

        return self.__client.make_request(proxy, quote_id_list, unpack_dict=False)

    def get_rate(self, quote_id: int):
        """
        Returns an instance of DoubleResult, which contains the rate

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getRate

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_reference_number(self, quote_id: int):
        """
        Method returns the reference number by quote ID.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getReferenceNumber

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_request_id(self, quote_id: int):
        """
        Returns an instance of IntegerResult, which contains the requestId

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getRequestId

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_status(self, quote_id: int):
        """
        Returns an instance of IntegerResult, which contains the QuoteStatusType.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getStatus

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_subject(self, quote_id: int):
        """
        Returns an instance of StringResult, which contains the subject.

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getSubject

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def get_template_list(
        self,
    ):
        """
        Method returns an instance of TemplateListResult, which contains a listof template objects which can be accessed by the user.


        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.getTemplateList

    def insert_by_template(self, quote: Union[QuoteIN, dict], template_id: int):
        """
        Method to create a order depending on the transfered templateID and QuoteIN object.

        :param quote: QuoteIN
        :param template_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.insert_byTemplate

        if type(quote) != QuoteIN:
            quote = QuoteIN(**quote).dict()
        else:
            quote = quote.dict()

        arg = {"quote": quote, "templateID": template_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def insert(
        self,
    ):
        """
        Method to create a new, empty quote.


        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.insert

    def insert2(self, quote: Union[QuoteIN, dict]):
        """
        Method to create a quote depending on the transfered object

        :param quote: QuoteIN

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.insert2

        if type(quote) != QuoteIN:
            quote = QuoteIN(**quote).dict()
        else:
            quote = quote.dict()

        return self.__client.make_request(proxy, quote, unpack_dict=False)

    def register_callback_notify(
        self,
        server_authentication_string: str,
        server_address: str,
        event_type: EventType,
    ):
        """
        Register to get notified when the specified EventType occursfor any quote.

        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.registerCallback_Notify

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "EventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def register_callback_observer(
        self, server_authentication_string: str, server_address: str, quote_id: int
    ):
        """
        Register to observe a specific object for any supportedEventType.

        :param server_authentication_string: str
        :param server_address: str
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.registerCallback_Observer

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "QuoteID": quote_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def request_order(self, quote_id: int):
        """
        Request and order to the provided quoteID

        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.requestOrder

        return self.__client.make_request(proxy, quote_id, unpack_dict=False)

    def request_quote(self, class_type: ProjectClassType):
        """
        Request a new quote

        :param class_type: ProjectClassType

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.requestQuote

        return self.__client.make_request(proxy, class_type.value, unpack_dict=False)

    def search(self, search_filter: Union[SearchFilter_Quote, dict]):
        """
        Search implementation to filter for any existing quotes based onspecific criteria.

        :param search_filter: SearchFilter_Quote

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.search

        if type(search_filter) != SearchFilter_Quote:
            search_filter = SearchFilter_Quote(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(proxy, search_filter, unpack_dict=False)

    def set_creation_date(self, date: datetime, quote_id: int):
        """
        Sets the creation date

        :param date: datetime
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setCreationDate

        arg = {"date": date, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_contact_id(self, customer_contact_id: int, quote_id: int):
        """
        Sets the customer contact ID for the currently selected project.

        :param customer_contact_id: int
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setCustomerContactID

        arg = {"customerContactID": customer_contact_id, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_id(self, customer_id: int, quote_id: int):
        """
        Sets the customerID

        :param customer_id: int
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setCustomerID

        arg = {"customerID": customer_id, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_external_id(self, quote_id: int, external_id: str):
        """
        Methode set External ID for Quote by quoteID

        :param quote_id: int
        :param external_id: str

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setExternalID

        arg = {"quoteID": quote_id, "externalID": external_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_category(
        self, project_category: str, system_language_code: str, quote_id: int
    ):
        """
        Set the the project category of the quote, specified by its name.

        :param project_category: str
        :param system_language_code: str
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectCategory

        arg = {
            "projectCategory": project_category,
            "systemLanguageCode": system_language_code,
            "quoteID": quote_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_projectmanager_id(self, resource_id: int, quote_id: int):
        """
        Sets the resourceID of the project manager to the given quote.

        :param resource_id: int
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectmanagerID

        arg = {"resourceID": resource_id, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_manager_memo(self, quote_id: int, memo: str):
        """
        Method set the project-manager Memo for order by quoteID.

        :param quote_id: int
        :param memo: str

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectManagerMemo

        arg = {"quoteID": quote_id, "memo": memo}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_name(self, project_name: str, quote_id: int):
        """
        Sets the project name.

        :param project_name: str
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectName

        arg = {"ProjectName": project_name, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_status(self, quote_id: int, status: int):
        """
        Method allows to set the ArchivStatus to ARCHIVED (3).

        :param quote_id: int
        :param status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setProjectStatus

        arg = {"quoteID": quote_id, "status": status}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_reference_number(self, quote_id: int, reference: str):
        """
        Method set reference number for quote by quoteID.

        :param quote_id: int
        :param reference: str

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setReferenceNumber

        arg = {"quoteID": quote_id, "reference": reference}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_request_id(self, quote_id: int, request_id: int):
        """
        Method to set the project related request ID.

        :param quote_id: int
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setRequestID

        arg = {"quoteID": quote_id, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, quote_id: int):
        """
        Sets the QuoteStatusType.

        :param status: int
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setStatus

        arg = {"Status": status, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_subject(self, subject: str, quote_id: int):
        """
        Sets the subject

        :param subject: str
        :param quote_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.setSubject

        arg = {"subject": subject, "quoteID": quote_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, quote: Union[QuoteIN, dict], enabled: bool):
        """
        updates the quote by the transfered objectUse EnableNullOrEmptyValues to decide if Null or empty Strings are savedinto Plunet or ignored.

        :param quote: QuoteIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataQuote30.update

        if type(quote) != QuoteIN:
            quote = QuoteIN(**quote).dict()
        else:
            quote = quote.dict()

        arg = {"quote": quote, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
