from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import IntegerList, RequestIN, SearchFilter_Request

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataRequest30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def add_language_combination(
        self, source_language: str, target_language: str, request_id: int
    ):
        """
        Adds a language combination to the specified request.

        :param source_language: str
        :param target_language: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.addLanguageCombination

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "requestID": request_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def add_service(self, service: str, request_id: int):
        """
        Adds a service type to the specified request.

        :param service: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.addService

        arg = {"service": service, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def copy_document_to_reference_folder(
        self, ref_language: str, unc_file_name: str, request_id: int
    ):
        """
        Deprecated.Please use DataDocument30.upload_Document(String, int, int, byte[], String, long) instead.Please note that this call is now deactivated by default. For Reactivation please contact Support@plunet.com.Copies a file to the reference folder.In general &#34;uncFileName&#34; describes the location of a file, which islocated within the local network.Usually the path has the following format:\\ComputerName\SharedFolder\ResourceIt is also possible to commit an URL (http://... / https://...) to afile on an external server via &#34;uncFileName&#34;. The URL must end with the filename.The reference language description is expected in english language or as ISO-Code.Method returns an instance of ResultFiles can also directly be uploaded as file content overDataDocument30.upload_Document(String, int, int, byte[], String, long)

        :param ref_language: str
        :param unc_file_name: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.copyDocument_toReferenceFolder

        arg = {
            "refLanguage": ref_language,
            "uncFileName": unc_file_name,
            "requestID": request_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def copy_document_to_source_folder(
        self, source_language: str, unc_file_name: str, request_id: int
    ):
        """
        Deprecated.Please use DataDocument30.upload_Document(String, int, int, byte[], String, long) instead.Copies a file to the source folder.In general &#34;uncFileName&#34; describes the location of a file, which is located within the local network.Usually the path has the following format:\\ComputerName\SharedFolder\ResourceIt is also possible to commit an URL (http://... / https://...) to afile on an external server via &#34;uncFileName&#34;. The URL must end with the filename.The source language description is expected in english language or as ISO-Code.Returns an instance of Result.Files can also directly be uploaded as file content overDataDocument30.upload_Document(String, int, int, byte[], String, long)

        :param source_language: str
        :param unc_file_name: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.copyDocument_toSourceFolder

        arg = {
            "sourceLanguage": source_language,
            "uncFileName": unc_file_name,
            "requestID": request_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete(self, request_id: int):
        """
        Method to delete a specific request via request id.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.delete

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def deregister_callback_notify(self, event_type: EventType):
        """
        Deletes an registered notify requestNotify requests can only be deleted by the user who has created them.

        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.deregisterCallback_Notify

        return self.__client.make_request(proxy, event_type.value, unpack_dict=False)

    def deregister_callback_observer(self, request_id: int):
        """
        Deletes an observerObserver can only deleted by the user who has created them

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.deregisterCallback_Observer

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_all_requests(
        self,
    ):
        """
        Method returns an instance of IntegerArrayResult, which contains a list of request ids.


        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getAll_Requests

    def get_brief_description(self, request_id: int):
        """
        Returns an instance of StringResult, containing the project name andfurther status information.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getBriefDescription

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_creation_date(self, request_id: int):
        """
        Returns an instance of DateResult, containing the creation date of the specified request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getCreationDate

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_customer_contact_id(self, request_id: int):
        """
        Method to get the customer contact for the specified request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getCustomerContactID

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_customer_id(self, request_id: int):
        """
        Returns an instance of IntegerResult, which contains the customer id ofthe current request and general status information.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getCustomerID

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_customer_ref_no_prev_order(self, request_id: int):
        """
        Method returns an instance of StringResult, which contains thecustomer reference number of the previous order.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getCustomerRefNo_PrevOrder

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_customer_ref_no(self, request_id: int):
        """
        Method returns an instance of StringResult, which contains the customerreference number of the definied request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getCustomerRefNo

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_delivery_date(self, request_id: int):
        """
        Returns an instance of DateResult, containing the delivery date of the current request

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getDeliveryDate

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_en15038_requested(self, request_id: int):
        """
        Method returns an instance of BooleanResult, which contains the information,whether the client requests the EN15038 standard.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getEN15038Requested

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_master_project_id(self, request_id: int):
        """
        Method to get the MasterProjectID of the specified request

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getMasterProjectID

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_order_id(self, request_id: int):
        """
        Deprecated.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getOrderID

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_order_id_list(self, request_id: int):
        """
        Method returns an instance of IntegerArrayResult, containing all orderID&#39;s for the specified request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getOrderIDList

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_price(self, request_id: int):
        """
        Method returns an instance of DoubleResult, which contains the price ofthe currently definied request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getPrice

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_property(self, request_id: int, property_name_english: str):
        """
        Deprecated.

        :param request_id: int
        :param property_name_english: str

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getProperty

        arg = {"requestID": request_id, "propertyNameEnglish": property_name_english}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_quotation_date(self, request_id: int):
        """
        Returns an instance of DateResult, containing the quotation date of thecurrent request

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getQuotationDate

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_quote_id(self, request_id: int):
        """
        Deprecated.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getQuoteID

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_quote_id_list(self, request_id: int):
        """
        Method returns an instance of IntegerArrayResult, containing all quoteID&#39;s for the specified request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getQuoteIDList

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_request_id(self, display_no: str):
        """
        Method returns an instance of IntegerResult, containing the ID of the current request.

        :param display_no: str

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestID

        return self.__client.make_request(proxy, display_no, unpack_dict=False)

    def get_request_no_for_view(self, request_id: int):
        """
        Returns an instance of StringResult, containing status information andthe formatted request number, which appears in the forms of theBusinessManager ( don’t confuse it with the request id, whichlooks similar to the request number ).

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestNo_for_View

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_request_object(self, request_id: int):
        """
        Method returns an instance of RequestResult, which contains an instance of Request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestObject

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_request_object2(self, request_number: str):
        """
        Method returns an instance of RequestResult, which contains an instance of Request.

        :param request_number: str

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestObject2

        return self.__client.make_request(proxy, request_number, unpack_dict=False)

    def get_request_object_list(self, request_id_list: Union[IntegerList, dict]):
        """
        Method returns an instance of RequestListResult, which contains a list of Request objects.

        :param request_id_list: IntegerList

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestObjectList

        if type(request_id_list) != IntegerList:
            request_id_list = IntegerList(**request_id_list).dict()
        else:
            request_id_list = request_id_list.dict()

        return self.__client.make_request(proxy, request_id_list, unpack_dict=False)

    def get_rush_request(self, request_id: int):
        """
        Returns an instance of StringResult, containing the project name andfurther status information.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getRushRequest

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_status(self, request_id: int):
        """
        Returns an instance of IntegerResult, which contains the RequestStatusType.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getStatus

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_subject(self, request_id: int):
        """
        Returns an instance of StringResult, which contains the subject of thecurrent request and general status information.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getSubject

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_type_of_project(self, request_id: int):
        """
        Method to get the type of the projectInfo: Type of Project does not displays the standard project-types likeorder, request... and can be configured within the admin area ofbusiness manager.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getTypeOfProject

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_word_count(self, request_id: int):
        """
        Method returns an instance of IntegerResult, which contains the wordcount for the currently fetched request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getWordCount

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def get_workflow_id(self, request_id: int):
        """
        Method to get the workflowID of the specified request

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.getWorkflowID

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def insert(
        self,
    ):
        """
        Method to create a new, empty request.


        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.insert

    def insert2(self, request: Union[RequestIN, dict]):
        """
        Method to create a quote depending on the transfered object

        :param request: RequestIN

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.insert2

        if type(request) != RequestIN:
            request = RequestIN(**request).dict()
        else:
            request = request.dict()

        return self.__client.make_request(proxy, request, unpack_dict=False)

    def order_request_by_template(self, request_id: int, template_id: int):
        """
        Method to order the specified request, using the transfered template.

        :param request_id: int
        :param template_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.orderRequest_byTemplate

        arg = {"requestID": request_id, "templateID": template_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def order_request(self, request_id: int):
        """
        Method to order the specified request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.orderRequest

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def quote_request_by_template(self, request_id: int, template_id: int):
        """
        Method to quote the specified request using the transfered template.

        :param request_id: int
        :param template_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.quoteRequest_byTemplate

        arg = {"requestID": request_id, "templateID": template_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def quote_request(self, request_id: int):
        """
        Method to create a quote from the specified request.

        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.quoteRequest

        return self.__client.make_request(proxy, request_id, unpack_dict=False)

    def register_callback_notify(
        self,
        server_authentication_string: str,
        server_address: str,
        event_type: EventType,
    ):
        """
        Register to get notified when the specified EventType occursfor any request.

        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.registerCallback_Notify

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "EventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def register_callback_observer(
        self, server_authentication_string: str, server_address: str, request_id: int
    ):
        """
        Register to observe a specific object for any supportedEventType.

        :param server_authentication_string: str
        :param server_address: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.registerCallback_Observer

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "RequestID": request_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def search(self, search_filter: Union[SearchFilter_Request, dict]):
        """
        Search implementation to filter for any existing requests based onspecific criteria.

        :param search_filter: SearchFilter_Request

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.search

        if type(search_filter) != SearchFilter_Request:
            search_filter = SearchFilter_Request(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(proxy, search_filter, unpack_dict=False)

    def set_brief_description(self, brief_description: str, request_id: int):
        """
        Sets the project name.

        :param brief_description: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setBriefDescription

        arg = {"briefDescription": brief_description, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_creation_date(self, date: datetime, request_id: int):
        """
        Sets the creation date of the specified request.

        :param date: datetime
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setCreationDate

        arg = {"date": date, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_contact_id(self, request_id: int, customer_contact_id: int):
        """
        Method to set the customer contact for the specified request.

        :param request_id: int
        :param customer_contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setCustomerContactID

        arg = {"requestID": request_id, "customerContactID": customer_contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_id(self, customer_id: int, request_id: int):
        """
        Sets the customer id for the specified request.

        :param customer_id: int
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setCustomerID

        arg = {"customerID": customer_id, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_ref_no_prev_order(
        self, customer_ref_no_previous_order: str, request_id: int
    ):
        """
        Method to set the customer reference number of the previous order.

        :param customer_ref_no_previous_order: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setCustomerRefNo_PrevOrder

        arg = {
            "CustomerRefNo_PreviousOrder": customer_ref_no_previous_order,
            "requestID": request_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_ref_no(self, customer_ref_no: str, request_id: int):
        """
        Method to set the customer reference number.

        :param customer_ref_no: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setCustomerRefNo

        arg = {"CustomerRefNo": customer_ref_no, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_delivery_date(self, date: datetime, request_id: int):
        """
        Sets the delivery date of the current request.

        :param date: datetime
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setDeliveryDate

        arg = {"date": date, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_en15038_requested(self, is_en15038: bool, request_id: int):
        """
        Method to mark a request, that the client wants the request to correspondto the EN 10538 standard.

        :param is_en15038: bool
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setEN15038Requested

        arg = {"isEN15038": is_en15038, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_master_project_id(self, request_id: int, master_project_id: int):
        """
        Method to set the MasterProjectID of the specified request

        :param request_id: int
        :param master_project_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setMasterProjectID

        arg = {"requestID": request_id, "MasterProjectID": master_project_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_order_id(self, order_id: int, request_id: int):
        """
        Deprecated.

        :param order_id: int
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setOrderID

        arg = {"orderID": order_id, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_price(self, price: float, request_id: int):
        """
        Method to set the price.

        :param price: float
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setPrice

        arg = {"price": price, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_property(
        self, request_id: int, property_name_english: str, property_value_english: str
    ):
        """
        Deprecated.

        :param request_id: int
        :param property_name_english: str
        :param property_value_english: str

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setProperty

        arg = {
            "requestID": request_id,
            "propertyNameEnglish": property_name_english,
            "propertyValueEnglish": property_value_english,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_quotation_date(self, date: datetime, request_id: int):
        """
        Sets the quotation date of the current request.

        :param date: datetime
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setQuotationDate

        arg = {"date": date, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_quote_id(self, quote_id: int, request_id: int):
        """
        Deprecated.

        :param quote_id: int
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setQuoteID

        arg = {"quoteID": quote_id, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_rush_request(self, is_rush_request: bool, request_id: int):
        """
        Sets the flag for rush request.

        :param is_rush_request: bool
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setRushRequest

        arg = {"isRushRequest": is_rush_request, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, request_id: int):
        """
        Sets the RequestStatusType.

        :param status: int
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setStatus

        arg = {"Status": status, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_subject(self, subject: str, request_id: int):
        """
        Sets the subject of the current request.

        :param subject: str
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setSubject

        arg = {"subject": subject, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_type_of_project(self, request_id: int, type_of_project_english: str):
        """
        Method to set the type of the project.

        :param request_id: int
        :param type_of_project_english: str

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setTypeOfProject

        arg = {"requestID": request_id, "TypeOfProjectEnglish": type_of_project_english}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_word_count(self, word_count: int, request_id: int):
        """
        Method to set the word count.

        :param word_count: int
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setWordCount

        arg = {"wordCount": word_count, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_workflow_id(self, request_id: int, workflow_id: int):
        """
        Method to set the workflowID of the specified requestA workflowID equals -1 will remove the workflow currently set for therequest.

        :param request_id: int
        :param workflow_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.setWorkflowID

        arg = {"requestID": request_id, "workflowID": workflow_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, request: Union[RequestIN, dict], enabled: bool):
        """
        Updates the quote by the transfered objectUse EnableNullOrEmptyValues to decide if Null or empty Strings are savedinto Plunet or ignored.

        :param request: RequestIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataRequest30.update

        if type(request) != RequestIN:
            request = RequestIN(**request).dict()
        else:
            request = request.dict()

        arg = {"request": request, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
