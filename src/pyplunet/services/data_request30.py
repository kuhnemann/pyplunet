from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import (
    BooleanResult,
    DateResult,
    DoubleResult,
    IntegerArrayResult,
    IntegerList,
    IntegerResult,
    RequestIN,
    RequestListResult,
    RequestResult,
    Result,
    SearchFilter_Request,
    StringResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataRequest30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def add_language_combination(
        self, source_language: str, target_language: str, request_id: int
    ) -> Result:
        """
        Adds a language combination to the specified request.
        All language descriptions were expected in english language or as ISO-Code.
        Returns an instance of Result.


        :param source_language: str
        :param target_language: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.addLanguageCombination
        response_model = Result

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "requestID": request_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_subject(self, request_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the subject of the
        current request and general status information.


        :param request_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getSubject
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_subject(self, subject: str, request_id: int) -> Result:
        """
        Sets the subject of the current request. Returns an instance of Result.


        :param subject: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setSubject
        response_model = Result

        arg = {"subject": subject, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_creation_date(self, request_id: int) -> DateResult:
        """
        Returns an instance of DateResult, containing the creation date of the specified request.


        :param request_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getCreationDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_property(
        self, request_id: int, property_name_english: str, property_value_english: str
    ) -> Result:
        """
        Deprecated.


        :param request_id: int
        :param property_name_english: str
        :param property_value_english: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setProperty
        response_model = Result

        arg = {
            "requestID": request_id,
            "propertyNameEnglish": property_name_english,
            "propertyValueEnglish": property_value_english,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_property(self, request_id: int, property_name_english: str) -> StringResult:
        """
        Deprecated.


        :param request_id: int
        :param property_name_english: str
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getProperty
        response_model = StringResult

        arg = {"requestID": request_id, "propertyNameEnglish": property_name_english}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update(
        self, request_in: Union[RequestIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        Updates the quote by the transfered object
        Use EnableNullOrEmptyValues to decide if Null or empty Strings are saved
        into Plunet or ignored.


        :param request_in: RequestIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.update
        response_model = Result

        if type(request_in) != RequestIN:
            request_in = RequestIN(**request_in).dict()
        else:
            request_in = request_in.dict()

        arg = {
            "RequestIN": request_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete(self, request_id: int) -> Result:
        """
        Method to delete a specific request via request id.
        Returns an instance of Result, which contains status information.
        No update-call is required to commit changes to the database.


        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert(
        self,
    ) -> IntegerResult:
        """
        Method to create a new, empty request.

        The method will return an instance of IntegerResult, which contains the
        identifier of the new generated order. Further api calls via this port
        will manipulate this order (except methods with an order id as parameter
        ), until another order is fetched or the session is invalidated.


        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def search(
        self, search_filter: Union[SearchFilter_Request, dict]
    ) -> IntegerArrayResult:
        """
        Search implementation to filter for any existing requests based on
        specific criteria.


        :param search_filter: SearchFilter_Request
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataRequest30.search
        response_model = IntegerArrayResult

        if type(search_filter) != SearchFilter_Request:
            search_filter = SearchFilter_Request(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_rush_request(self, is_rush_request: bool, request_id: int) -> Result:
        """
        Sets the flag for rush request.


        :param is_rush_request: bool
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setRushRequest
        response_model = Result

        arg = {"IsRushRequest": is_rush_request, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_type_of_project(self, request_id: int, type_of_project: str) -> Result:
        """
        Method to set the type of the project.
        Info: Type of Project does not displays the standard project-types like
        order, request... and can be configured within the admin area of
        business manager.


        :param request_id: int
        :param type_of_project: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setTypeOfProject
        response_model = Result

        arg = {"requestID": request_id, "TypeOfProject": type_of_project}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_workflow_id(self, request_id: int) -> IntegerResult:
        """
        Method to get the workflowID of the specified request


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getWorkflowID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def quote_request(self, request_id: int) -> IntegerResult:
        """
        Method to create a quote from the specified request.
        Language combinations and items will be created.
        Also the source/reference files will be copied to the created quote.
        Returns an instance of IntegerResult, which contains the identifier of the new quote.


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.quoteRequest
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_type_of_project(self, request_id: int) -> StringResult:
        """
        Method to get the type of the project
        Info: Type of Project does not displays the standard project-types like
        order, request... and can be configured within the admin area of
        business manager.


        :param request_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getTypeOfProject
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_workflow_id(self, request_id: int, workflow_id: int) -> Result:
        """
        Method to set the workflowID of the specified request

        A workflowID equals -1 will remove the workflow currently set for the
        request.


        :param request_id: int
        :param workflow_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setWorkflowID
        response_model = Result

        arg = {"requestID": request_id, "workflowID": workflow_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_rush_request(self, request_id: int) -> BooleanResult:
        """
        Returns an instance of StringResult, containing the project name and
        further status information.


        :param request_id: int
        :return: BooleanResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getRushRequest
        response_model = BooleanResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def order_request_by_template(
        self, request_id: int, order_template_id: int
    ) -> IntegerResult:
        """
        Method to order the specified request, using the transfered template.
        Language combinations and items will be created.
        Also the source/reference files will be copied to the created order.
        Returns an instance of IntegerResult, which contains the identifier of the new order.
        OrderTemplateID can be 0, to not use any template.


        :param request_id: int
        :param order_template_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.orderRequest_byTemplate
        response_model = IntegerResult

        arg = {"requestID": request_id, "OrderTemplateID": order_template_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def quote_request_by_template(
        self, request_id: int, quote_template_id: int
    ) -> IntegerResult:
        """
        Method to quote the specified request using the transfered template.
        Language combinations and items will be created.
        Also the source/reference files will be copied to the created quote.
        Returns an instance of IntegerResult, which contains the identifier of the new quote.
        QuoteTemplateID can be 0, to not use any template.


        :param request_id: int
        :param quote_template_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.quoteRequest_byTemplate
        response_model = IntegerResult

        arg = {"requestID": request_id, "QuoteTemplateID": quote_template_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def add_service(self, service: str, request_id: int) -> Result:
        """
        Adds a service type to the specified request.
        Service types were expected in english language.
        Returns an instance of Result.


        :param service: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.addService
        response_model = Result

        arg = {"service": service, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_customer_id(self, customer_id: int, request_id: int) -> Result:
        """
        Sets the customer id for the specified request.


        :param customer_id: int
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setCustomerID
        response_model = Result

        arg = {"customerID": customer_id, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def deregister_callback_observer(self, request_id: int) -> Result:
        """
        Deletes an observer

        Observer can only deleted by the user who has created them


        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.deregisterCallback_Observer
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
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
        for any request.

        If the EventType occurs PBM will call the callback web service,
        which is hosted within your environment. Also each user can only create
        one notify request per event.

        Please check CallbackRequest30 for the exact specification for
        this service.


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackRequest30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.registerCallback_Notify
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
        Deletes an registered notify request
        Notify requests can only be deleted by the user who has created them.


        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.deregisterCallback_Notify
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
        self, server_authentication_string: str, server_address: str, request_id: int
    ) -> Result:
        """
        Register to observe a specific object for any supported
        EventType.

        As soon as any supported event occurs, PBM will call the callback web
        service, which is hosted within your environment.

        Please check CallbackRequest30 for the exact specification for
        this service.


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackRequest30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.registerCallback_Observer
        response_model = Result

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "RequestID": request_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_master_project_id(self, request_id: int) -> IntegerResult:
        """
        Method to get the MasterProjectID of the specified request


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getMasterProjectID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_master_project_id(self, request_id: int, master_project_id: int) -> Result:
        """
        Method to set the MasterProjectID of the specified request


        :param request_id: int
        :param master_project_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setMasterProjectID
        response_model = Result

        arg = {"requestID": request_id, "MasterProjectID": master_project_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_status(self, request_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the RequestStatusType.


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, request_id: int) -> Result:
        """
        Sets the RequestStatusType. Returns an instance of Result.


        :param status: int
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setStatus
        response_model = Result

        arg = {"Status": status, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_brief_description(self, request_id: int) -> StringResult:
        """
        Returns an instance of StringResult, containing the project name and
        further status information.


        :param request_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getBriefDescription
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_brief_description(self, brief_description: str, request_id: int) -> Result:
        """
        Sets the project name.


        :param brief_description: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setBriefDescription
        response_model = Result

        arg = {"briefDescription": brief_description, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_en15038_requested(self, is_en15038: bool, request_id: int) -> Result:
        """
        Method to mark a request, that the client wants the request to correspond
        to the EN 10538 standard.


        :param is_en15038: bool
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setEN15038Requested
        response_model = Result

        arg = {"isEN15038": is_en15038, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_en15038_requested(self, request_id: int) -> BooleanResult:
        """
        Method returns an instance of BooleanResult, which contains the information,
        whether the client requests the EN15038 standard.


        :param request_id: int
        :return: BooleanResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getEN15038Requested
        response_model = BooleanResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_customer_contact_id(
        self, request_id: int, customer_contact_id: int
    ) -> Result:
        """
        Method to set the customer contact for the specified request.


        :param request_id: int
        :param customer_contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setCustomerContactID
        response_model = Result

        arg = {"requestID": request_id, "customerContactID": customer_contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_customer_contact_id(self, request_id: int) -> IntegerResult:
        """
        Method to get the customer contact for the specified request.


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getCustomerContactID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_id_list(self, request_id: int) -> IntegerArrayResult:
        """
        Method returns an instance of IntegerArrayResult, containing all order
        ID's for the specified request.


        :param request_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getOrderIDList
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_delivery_date(self, date: datetime, request_id: int) -> Result:
        """
        Sets the delivery date of the current request. Returns an instance of Result


        :param date: datetime
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setDeliveryDate
        response_model = Result

        arg = {"date": date, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_delivery_date(self, request_id: int) -> DateResult:
        """
        Returns an instance of DateResult, containing the delivery date of the current request


        :param request_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getDeliveryDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_price(self, price: float, request_id: int) -> Result:
        """
        Method to set the price. Returns an instance of Result.
        This value is available for free use.


        :param price: float
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setPrice
        response_model = Result

        arg = {"price": price, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_quotation_date(self, date: datetime, request_id: int) -> Result:
        """
        Sets the quotation date of the current request. Returns an instance of Result.


        :param date: datetime
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setQuotationDate
        response_model = Result

        arg = {"date": date, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_customer_ref_no(self, customer_ref_no: str, request_id: int) -> Result:
        """
        Method to set the customer reference number.


        :param customer_ref_no: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setCustomerRefNo
        response_model = Result

        arg = {"CustomerRefNo": customer_ref_no, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_quote_id(self, quote_id: int, request_id: int) -> Result:
        """
        Deprecated.


        :param quote_id: int
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setQuoteID
        response_model = Result

        arg = {"quoteID": quote_id, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_quote_id_list(self, request_id: int) -> IntegerArrayResult:
        """
        Method returns an instance of IntegerArrayResult, containing all quote
        ID's for the specified request.


        :param request_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getQuoteIDList
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_creation_date(self, date: datetime, request_id: int) -> Result:
        """
        Sets the creation date of the specified request.


        :param date: datetime
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setCreationDate
        response_model = Result

        arg = {"date": date, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_order_id(self, order_id: int, request_id: int) -> Result:
        """
        Deprecated.


        :param order_id: int
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setOrderID
        response_model = Result

        arg = {"orderID": order_id, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_quotation_date(self, request_id: int) -> DateResult:
        """
        Returns an instance of DateResult, containing the quotation date of the
        current request


        :param request_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getQuotationDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_request_object(self, request_id: int) -> RequestResult:
        """
        Method returns an instance of RequestResult, which contains an instance of Request.
        Do not loop through an array of requestIDs using this call. Use getRequestObjectList(String, IntegerList) instead.


        :param request_id: int
        :return: RequestResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestObject
        response_model = RequestResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_customer_ref_no(self, request_id: int) -> StringResult:
        """
        Method returns an instance of StringResult, which contains the customer
        reference number of the definied request.


        :param request_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getCustomerRefNo
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_price(self, request_id: int) -> DoubleResult:
        """
        Method returns an instance of DoubleResult, which contains the price of
        the currently definied request.


        :param request_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getPrice
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def order_request(self, request_id: int) -> IntegerResult:
        """
        Method to order the specified request.
        Language combinations and items will be created.
        Also the source/reference files will be copied to the created order.
        Returns an instance of IntegerResult, which contains the identifier of the new order.


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.orderRequest
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_all_requests(
        self,
    ) -> IntegerArrayResult:
        """
        Method returns an instance of IntegerArrayResult, which contains a list of request ids.
        System will search for all request, which were connected to the user, which is currently logged in.
        For a customer user, this method will return all requests from this customer


        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getAll_Requests
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_customer_ref_no_prev_order(
        self, customer_ref_no_previous_order: str, request_id: int
    ) -> Result:
        """
        Method to set the customer reference number of the previous order.
        Retuns an instance of Result. This value is available for free use.


        :param customer_ref_no_previous_order: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setCustomerRefNo_PrevOrder
        response_model = Result

        arg = {
            "CustomerRefNo_PreviousOrder": customer_ref_no_previous_order,
            "requestID": request_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_customer_ref_no_prev_order(self, request_id: int) -> StringResult:
        """
        Method returns an instance of StringResult, which contains the
        customer reference number of the previous order.


        :param request_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getCustomerRefNo_PrevOrder
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def copy_document_to_reference_folder(
        self, ref_language: str, unc_file_name: str, request_id: int
    ) -> Result:
        """
        Deprecated. Please use DataDocument30.upload_Document(String, int, int, byte[], String, long) instead.
        Please note that this call is now deactivated by default. For Reactivation please contact Support@plunet.com.

        Copies a file to the reference folder.
        In general "uncFileName" describes the location of a file, which is
        located within the local network.Usually the path has the following format:
        \\ComputerName\SharedFolder\Resource
        It is also possible to commit an URL (http://... / https://...) to a
        file on an external server via "uncFileName". The URL must end with the filename.
        The reference language description is expected in english language or as ISO-Code.
        Method returns an instance of Result
        Files can also directly be uploaded as file content over
        DataDocument30.upload_Document(String, int, int, byte[], String, long)


        :param ref_language: str
        :param unc_file_name: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.copyDocument_toReferenceFolder
        response_model = Result

        arg = {
            "refLanguage": ref_language,
            "uncFileName": unc_file_name,
            "requestID": request_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def copy_document_to_source_folder(
        self, source_language: str, unc_file_name: str, request_id: int
    ) -> Result:
        """
        Deprecated. Please use DataDocument30.upload_Document(String, int, int, byte[], String, long) instead.

        Copies a file to the source folder.
        In general "uncFileName" describes the location of a file, which is located within the local network.
        Usually the path has the following format:
        \\ComputerName\SharedFolder\Resource
        It is also possible to commit an URL (http://... / https://...) to a
        file on an external server via "uncFileName". The URL must end with the filename.
        The source language description is expected in english language or as ISO-Code.
        Returns an instance of Result.
        Files can also directly be uploaded as file content over
        DataDocument30.upload_Document(String, int, int, byte[], String, long)


        :param source_language: str
        :param unc_file_name: str
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.copyDocument_toSourceFolder
        response_model = Result

        arg = {
            "sourceLanguage": source_language,
            "uncFileName": unc_file_name,
            "requestID": request_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_request_object2(self, request_number: str) -> RequestResult:
        """
        Method returns an instance of RequestResult, which contains an instance of Request.


        :param request_number: str
        :return: RequestResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestObject2
        response_model = RequestResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_number,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_request_no_for_view(self, request_id: int) -> StringResult:
        """
        Returns an instance of StringResult, containing status information and
        the formatted request number, which appears in the forms of the
        BusinessManager ( donât confuse it with the request id, which
        looks similar to the request number ).


        :param request_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestNo_for_View
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_request_object_list(
        self, request_id_list: Union[IntegerList, dict]
    ) -> RequestListResult:
        """
        Method returns an instance of RequestListResult, which contains a list of Request objects.
        WARNING: This call can cause performance issues. It has been optimized from Plunet version 8.15


        :param request_id_list: IntegerList
        :return: RequestListResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestObjectList
        response_model = RequestListResult

        if type(request_id_list) != IntegerList:
            request_id_list = IntegerList(**request_id_list).dict()
        else:
            request_id_list = request_id_list.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id_list,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert2(self, request_in: Union[RequestIN, dict]) -> IntegerResult:
        """
        Method to create a quote depending on the transfered object


        :param request_in: RequestIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.insert2
        response_model = IntegerResult

        if type(request_in) != RequestIN:
            request_in = RequestIN(**request_in).dict()
        else:
            request_in = request_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_word_count(self, word_count: int, request_id: int) -> Result:
        """
        Method to set the word count. Returns an instance of Result.
        This value is available for free use.


        :param word_count: int
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataRequest30.setWordCount
        response_model = Result

        arg = {"wordCount": word_count, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_word_count(self, request_id: int) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains the word
        count for the currently fetched request.


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getWordCount
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_quote_id(self, request_id: int) -> IntegerResult:
        """
        Deprecated.


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getQuoteID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_request_id(self, display_no: str) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, containing the ID of the current request.


        :param display_no: str
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getRequestID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=display_no,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_id(self, request_id: int) -> IntegerResult:
        """
        Deprecated.


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getOrderID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_customer_id(self, request_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the customer id of
        the current request and general status information.


        :param request_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataRequest30.getCustomerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=request_id,
            response_model=response_model,
            unpack_dict=False,
        )
