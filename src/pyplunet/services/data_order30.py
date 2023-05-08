from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType, ProjectType
from ..models import (
    BooleanResult,
    DateResult,
    DoubleResult,
    IntegerArrayResult,
    IntegerList,
    IntegerResult,
    LinkListResult,
    OrderIN,
    OrderListResult,
    OrderResult,
    Result,
    SearchFilter_Order,
    StringArrayResult,
    StringResult,
    TemplateListResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataOrder30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def add_language_combination(
        self, source_language: str, target_language: str, order_id: int
    ) -> IntegerResult:
        """
        Adds a language combination to the specified order.
        All language descriptions were expected in English language or as ISO-Code.
        Returns an instance of Result.


        :param source_language: str
        :param target_language: str
        :param order_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.addLanguageCombination
        response_model = IntegerResult

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "orderID": order_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_rate(self, order_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the rate.


        :param order_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getRate
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_request_id(self, order_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the requestId.


        :param order_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getRequestId
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_project_name(self, name: str, order_id: int) -> Result:
        """
        Sets the project name for the currently selected project. Returns an instance of Result.


        :param name: str
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectName
        response_model = Result

        arg = {"name": name, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_subject(self, order_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the subject.


        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getSubject
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_subject(self, subject: str, order_id: int) -> Result:
        """
        Sets the subject for the currently selected project.


        :param subject: str
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setSubject
        response_model = Result

        arg = {"subject": subject, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_project_name(self, order_id: int) -> StringResult:
        """
        Returns an instance of String Result, which contains the project name.


        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectName
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_request_id(self, order_id: int, request_id: int) -> Result:
        """
        Method to set the project related request ID.


        :param order_id: int
        :param request_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setRequestID
        response_model = Result

        arg = {"orderID": order_id, "requestID": request_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_creation_date(self, order_id: int) -> DateResult:
        """
        Returns an instance of DateResult, which contains the creation date.


        :param order_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getCreationDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_property(
        self, order_id: int, property_name_english: str, property_value_english: str
    ) -> Result:
        """
        Deprecated.


        :param order_id: int
        :param property_name_english: str
        :param property_value_english: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setProperty
        response_model = Result

        arg = {
            "orderID": order_id,
            "propertyNameEnglish": property_name_english,
            "propertyValueEnglish": property_value_english,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_property(self, order_id: int, property_name_english: str) -> StringResult:
        """
        Deprecated.


        :param order_id: int
        :param property_name_english: str
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getProperty
        response_model = StringResult

        arg = {"orderID": order_id, "propertyNameEnglish": property_name_english}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update(
        self, order_in: Union[OrderIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        Updates the Order by the transfered object.
        Use EnableNullOrEmptyValues to decide if Null or empty Strings are saved
        into Plunet or ignored.


        :param order_in: OrderIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.update
        response_model = Result

        if type(order_in) != OrderIN:
            order_in = OrderIN(**order_in).dict()
        else:
            order_in = order_in.dict()

        arg = {
            "OrderIN": order_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete(self, order_id: int) -> Result:
        """
        Method to delete an order via ID.


        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert(
        self,
    ) -> IntegerResult:
        """
        Method to create a new, empty order.
        The method will return an instance of
        IntegerResult, which contains the identifier of the new generated order.
        Further api calls via this port will maninpulate this order
        (except methods with an order id as parameter ),
        until another order is fetched or the session is invalidated.


        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def search(
        self, search_filter: Union[SearchFilter_Order, dict]
    ) -> IntegerArrayResult:
        """
        Search implementation to filter for any existing order based on
        specific criteria.


        :param search_filter: SearchFilter_Order
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataOrder30.search
        response_model = IntegerArrayResult

        if type(search_filter) != SearchFilter_Order:
            search_filter = SearchFilter_Order(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter,
            response_model=response_model,
            unpack_dict=False,
        )

    def create_link(
        self,
        source_order_id: int,
        target_id: int,
        project_type: Union[ProjectType, int],
        is_bidirectional: bool,
        memo: str,
    ) -> Result:
        """
        Creates a link between two orders.


        :param source_order_id: int
        :param target_id: int
        :param project_type: ProjectType
        :param is_bidirectional: bool
        :param memo: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.createLink
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "sourceOrderId": source_order_id,
            "targetId": target_id,
            "projectType": project_type,
            "isBidirectional": is_bidirectional,
            "memo": memo,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_currency(self, order_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the currency.


        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getCurrency
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_reference_number(self, order_id: int, reference: str) -> Result:
        """
        Method set reference number for order by orderID.


        :param order_id: int
        :param reference: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setReferenceNumber
        response_model = Result

        arg = {"orderID": order_id, "reference": reference}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_project_category(
        self, project_category: str, system_language_code: str, order_id: int
    ) -> Result:
        """
        Set the the project category of the order, specified by its name.


        For a full list of your project categories, see Admin | Miscellaneous |
        Project category.


        :param project_category: str
        :param system_language_code: str
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectCategory
        response_model = Result

        arg = {
            "projectCategory": project_category,
            "systemLanguageCode": system_language_code,
            "orderID": order_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_project_category(
        self, system_language_code: str, order_id: int
    ) -> StringResult:
        """
        Get the name (in the language specified) of the project category of
        the order.

        For a full list of your project categories, see Admin | Miscellaneous |
        Project category.


        :param system_language_code: str
        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectCategory
        response_model = StringResult

        arg = {"systemLanguageCode": system_language_code, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_customer_id(self, customer_id: int, order_id: int) -> Result:
        """
        Sets the customerID for the currently selected project.


        :param customer_id: int
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setCustomerID
        response_model = Result

        arg = {"customerID": customer_id, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def deregister_callback_observer(self, order_id: int) -> Result:
        """
        Deletes an observer.
        (observer can only deleted by the user who has created them)


        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.deregisterCallback_Observer
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
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
        for any order.

        If the EventType occurs PBM will call the callback web service,
        which is hosted within your environment. Please check
        CallbackOrder30 for the exact specification for this service.
        (each user can only create one notifier per event)


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackOrder30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.registerCallback_Notify
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
        Deletes an registered notify request.
        Notify requests can only be deleted by the user who has created them


        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.deregisterCallback_Notify
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
        self, server_authentication_string: str, server_address: str, order_id: int
    ) -> Result:
        """
        Register to observe a specific object for any supported
        EventType.

        As soon as any supported event occurs, PBM will call the callback web
        service, which is hosted within your environment. Please check
        CallbackOrder30 for the exact specification for this service.
        (each user can only create one observer per id)


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackOrder30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.registerCallback_Observer
        response_model = Result

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "OrderID": order_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert_by_template(
        self, order_in: Union[OrderIN, dict], template_id: int
    ) -> IntegerResult:
        """
        Method to create a order depending on the transfered templateID and OrderIN object.
        (object values will overwrite information set by the template)
        #setOrderID(int) will be ignored as it
        will be auto generated by the system.


        :param order_in: OrderIN
        :param template_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.insert_byTemplate
        response_model = IntegerResult

        if type(order_in) != OrderIN:
            order_in = OrderIN(**order_in).dict()
        else:
            order_in = order_in.dict()

        arg = {"OrderIN": order_in, "TemplateID": template_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_reference_number(self, order_id: int) -> StringResult:
        """
        Method returns the reference number by order ID.


        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getReferenceNumber
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_project_manager_memo(self, order_id: int) -> StringResult:
        """
        Method returns project-manager memo for order by orderID.


        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectManagerMemo
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_master_project_id(self, order_id: int) -> IntegerResult:
        """
        Method to get the MasterProjectID of the specified order.


        :param order_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getMasterProjectID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_master_project_id(self, order_id: int, master_project_id: int) -> Result:
        """
        Method to set the MasterProjectID of the specified order.


        :param order_id: int
        :param master_project_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setMasterProjectID
        response_model = Result

        arg = {"orderID": order_id, "MasterProjectID": master_project_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_project_manager_memo(self, order_id: int, memo: str) -> Result:
        """
        Method set the project-manager Memo for order by orderID.


        :param order_id: int
        :param memo: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectManagerMemo
        response_model = Result

        arg = {"orderID": order_id, "memo": memo}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_delivery_deadline(
        self, delivery_deadline: datetime, order_id: int
    ) -> Result:
        """
        Sets the delivery deadline for the currently selected project.


        :param delivery_deadline: datetime
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setDeliveryDeadline
        response_model = Result

        arg = {"deliveryDeadline": delivery_deadline, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_delivery_deadline(self, order_id: int) -> DateResult:
        """
        Returns an instance of DateResult, which contains the delivery deadline.


        :param order_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getDeliveryDeadline
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_confirmations(self, order_id: int) -> StringArrayResult:
        """
        Returns an instance of StringArrayResult, which contains a list of relative
        network paths to all existing order confirmation documents.
        Info: For content based file up/download please use DataDocument30


        :param order_id: int
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderConfirmations
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_en15038_requested(self, is_en15038: bool, order_id: int) -> Result:
        """
        Method to mark a project, that the clients wants the project to correspond to the EN 10538 standard.


        :param is_en15038: bool
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setEN15038Requested
        response_model = Result

        arg = {"isEN15038": is_en15038, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_language_combination(self, order_id: int) -> StringArrayResult:
        """
        Returns an instance of StringArrayResult which contains a list.


        :param order_id: int
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getLanguageCombination
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_delivery_comment(self, order_id: int) -> StringResult:
        """
        Method returns an instance of StringResult, which contains the delivery comment.


        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getDeliveryComment
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_object_list(
        self, order_id_list: Union[IntegerList, dict]
    ) -> OrderListResult:
        """
        Method returns an instance of OrderListResult, which contains a list of order objects.


        :param order_id_list: IntegerList
        :return: OrderListResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderObjectList
        response_model = OrderListResult

        if type(order_id_list) != IntegerList:
            order_id_list = IntegerList(**order_id_list).dict()
        else:
            order_id_list = order_id_list.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id_list,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_projectmanager_id(self, order_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the resource id.


        :param order_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectmanagerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_closing_date(self, order_id: int) -> DateResult:
        """
        Method returns an instance of DateResult, which contains the order closing date.


        :param order_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderClosingDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_projectmanager_id(self, resource_id: int, order_id: int) -> Result:
        """
        Sets the resourceID of the project manager for defined order.


        :param resource_id: int
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectmanagerID
        response_model = Result

        arg = {"resourceID": resource_id, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_en15038_requested(self, order_id: int) -> BooleanResult:
        """
        Method returns an instance of BooleanResult, which contains the information,
        whether the client requests the EN15038 standard.


        :param order_id: int
        :return: BooleanResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getEN15038Requested
        response_model = BooleanResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_object(self, order_id: int) -> OrderResult:
        """
        Method returns an instance of OrderResult, which contains an instance of Order.


        :param order_id: int
        :return: OrderResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderObject
        response_model = OrderResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_object2(self, order_number: str) -> OrderResult:
        """
        Method returns an instance of OrderResult, which contains an instance of Order.


        :param order_number: str
        :return: OrderResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderObject2
        response_model = OrderResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_number,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_template_list(
        self,
    ) -> TemplateListResult:
        """
        Method returns an instance of TemplateListResult, which contains a list
        of template objects which can be accessed by the user.


        :return: TemplateListResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getTemplateList
        response_model = TemplateListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_customer_contact_id(
        self, customer_contact_id: int, order_id: int
    ) -> Result:
        """
        Sets the customer contact ID for the currently selected project.


        :param customer_contact_id: int
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setCustomerContactID
        response_model = Result

        arg = {"customerContactID": customer_contact_id, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_customer_contact_id(self, order_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the customer contact id.


        :param order_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getCustomerContactID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_project_status(self, order_id: int, project_status: int) -> Result:
        """
        Method allows to set the ArchivStatus to ARCHIVED(3).
        Other status changes are not supported due to underlying automated workflows.
        Please note that the current status must be either COMPLETED(6) or COMPLETED_ARCHIVABLE(2).


        :param order_id: int
        :param project_status: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectStatus
        response_model = Result

        arg = {"orderID": order_id, "projectStatus": project_status}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_project_status(self, order_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the ArchivStatus.


        :param order_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_action_link(
        self, order_id: int, user_id: int, action_link_type: int
    ) -> StringResult:
        """
        Method to obtain any kind of order related action link.


        :param order_id: int
        :param user_id: int
        :param action_link_type: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getActionLink
        response_model = StringResult

        arg = {
            "orderID": order_id,
            "userID": user_id,
            "actionLinkType": action_link_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_links(
        self, order_id: int, project_type: Union[ProjectType, int]
    ) -> LinkListResult:
        """
        Outputs all incoming and outgoing links for an order.


        :param order_id: int
        :param project_type: ProjectType
        :return: LinkListResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getLinks
        response_model = LinkListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"orderId": order_id, "projectType": project_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_order_date(self, order_id: int) -> DateResult:
        """
        Get the order date.


        :param order_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_order_date(self, order_date: datetime, order_id: int) -> Result:
        """
        Set the order date.


        :param order_date: datetime
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setOrderDate
        response_model = Result

        arg = {"orderDate": order_date, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def check_en15038(self, order_id: int) -> BooleanResult:
        """
        Method returns an instance of BooleanResult, which contains the information,
        whether a project corresponds the EN15038 standard or not.


        :param order_id: int
        :return: BooleanResult
        """

        proxy = self.__client.plunet_server.DataOrder30.checkEN15038
        response_model = BooleanResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_creation_date(self, creation_date: datetime, order_id: int) -> Result:
        """
        Sets the creation date for the currently selected project.


        :param creation_date: datetime
        :param order_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setCreationDate
        response_model = Result

        arg = {"creationDate": creation_date, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_order_no_for_view(self, order_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the formatted order number.


        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderNo_for_View
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_currency_and_rate(
        self, order_id: int, currency_iso_code: str, rate: float
    ) -> Result:
        """
        Method to change the currency and rate for the current project.
        The rate refers to the default currency / domestic currency,
        which is configured in the admin section of the Plunet BusinessManager.
        Changing the currency / rate will cause a recalculation of item prices.


        :param order_id: int
        :param currency_iso_code: str
        :param rate: float
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setCurrencyAndRate
        response_model = Result

        arg = {"orderID": order_id, "currencyIsoCode": currency_iso_code, "rate": rate}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_documents_within_source_folder(self, order_id: int) -> StringArrayResult:
        """
        Deprecated. Please use DataDocument30.getFileList(String, int, int) with Folder Type = 6 instead
        for compatibility reasons with DataDocument30.

        Returns an instance of StringArrayResult, which contains a list
        of network paths to source files.
        Info: For content based file up/download please use DataDocument30


        :param order_id: int
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getDocuments_Within_SourceFolder
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_documents_within_final_folder(self, order_id: int) -> StringArrayResult:
        """
        Deprecated. Please use DataDocument30.getFileList(String, int, int) with Folder Type = 12 instead
        for compatibility reasons with DataDocument30.

        Returns an instance of StringArrayResult, which contains a list of network
        paths to all documents located in the final folder.
        Info: For content based file up/download please use DataDocument30


        :param order_id: int
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getDocuments_Within_FinalFolder
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def create_order_confirmation(
        self, template: str, format_id: int, order_id: int
    ) -> StringResult:
        """
        Method creates the order confirmation as rtf-file and returns an instance of StringResult,
        which contains the network path where the file is located.


        :param template: str
        :param format_id: int
        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.createOrderConfirmation
        response_model = StringResult

        arg = {"template": template, "formatId": format_id, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert2(self, order_in: Union[OrderIN, dict]) -> IntegerResult:
        """
        Method to create a order depending on the transfered object.


        :param order_in: OrderIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.insert2
        response_model = IntegerResult

        if type(order_in) != OrderIN:
            order_in = OrderIN(**order_in).dict()
        else:
            order_in = order_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_external_id(self, order_id: int, external_id: str) -> Result:
        """
        Method set ExternalID of Order by orderID


        :param order_id: int
        :param external_id: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOrder30.setExternalID
        response_model = Result

        arg = {"orderID": order_id, "externalID": external_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_external_id(self, order_id: int) -> StringResult:
        """
        Method returns the ExternalID by orderID


        :param order_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getExternalID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_id(self, display_no: str) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains an order ID.


        :param display_no: str
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=display_no,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_documents_within_reference_folder(self, order_id: int) -> StringArrayResult:
        """
        Deprecated. Please use DataDocument30.getFileList(String, int, int) with Folder Type = 5 instead
        for compatibility reasons with DataDocument30.

        Returns an instance of StringArrayResult, which contains a list of network
        paths to the reference files.
        Info: For content based file up/download please use DataDocument30


        :param order_id: int
        :return: StringArrayResult
        """

        proxy = (
            self.__client.plunet_server.DataOrder30.getDocuments_Within_ReferenceFolder
        )
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_documents_within_source_folder_by_language(
        self, language: str, order_id: int
    ) -> StringArrayResult:
        """
        Deprecated. Please use DataDocument30.getFileList(String, int, int) with Folder Type = 6 instead
        for compatibility reasons with DataDocument30.

        Returns an instance of StringArrayResult, which contains a list of network
        paths to source files, connected to a specific language.
        Info: For content based file up/download please use DataDocument30


        :param language: str
        :param order_id: int
        :return: StringArrayResult
        """

        proxy = (
            self.__client.plunet_server.DataOrder30.getDocuments_Within_SourceFolder_ByLanguage
        )
        response_model = StringArrayResult

        arg = {"language": language, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_documents_within_reference_folder_by_language(
        self, language: str, order_id: int
    ) -> StringArrayResult:
        """
        Deprecated. Please use DataDocument30.getFileList(String, int, int) with Folder Type = 5 instead
        for compatibility reasons with DataDocument30.

        Returns an instance of StringArrayResult, which contains a list of network
        paths to the reference files, which are connected to a specific language.
        Info: For content based file up/download please use DataDocument30


        :param language: str
        :param order_id: int
        :return: StringArrayResult
        """

        proxy = (
            self.__client.plunet_server.DataOrder30.getDocuments_Within_ReferenceFolder_ByLanguage
        )
        response_model = StringArrayResult

        arg = {"language": language, "orderID": order_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_customer_id(self, order_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the customer id.


        :param order_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getCustomerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=order_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_item_status(
        self, source_language: str, target_language: str, order_id: int
    ) -> IntegerResult:
        """
        Method returns the status of a project item associated to a specific language combination.


        :param source_language: str
        :param target_language: str
        :param order_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOrder30.getItemStatus
        response_model = IntegerResult

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "orderID": order_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )
