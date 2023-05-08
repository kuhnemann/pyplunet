from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType, ResourceType, WorkingStatus
from ..models import (
    AccountResult,
    IntegerArrayResult,
    IntegerList,
    IntegerResult,
    PaymentInfo,
    PaymentInfoResult,
    PricelistListResult,
    ResourceIN,
    ResourceListResult,
    ResourceResult,
    Result,
    SearchFilter_Resource,
    StringResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataResource30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def update(
        self, resource_in: Union[ResourceIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        Updates a resource per Object.

        Use EnableNullOrEmptyValues to decide if Null or empty Strings are saved into
        Plunet or should ignored.


        :param resource_in: ResourceIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.update
        response_model = Result

        if type(resource_in) != ResourceIN:
            resource_in = ResourceIN(**resource_in).dict()
        else:
            resource_in = resource_in.dict()

        arg = {
            "ResourceIN": resource_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete(self, resource_id: int) -> Result:
        """
        Method to delete a resource via ID. Returns an instance of
        Result.


        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert(self, working_status: Union[WorkingStatus, int]) -> IntegerResult:
        """
        Method to create a new, empty resource dataset.

        The method will return an instance of IntegerResult, which contains
        the identifier of the new generated resource.


        Further API calls via this port will manipulate this resource (except methods
        with an resource id as parameter), until another resource is fetched or the
        session is invalidated.


        :param working_status: WorkingStatus
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResource30.insert
        response_model = IntegerResult

        if type(working_status) == WorkingStatus:
            working_status = working_status.value
        elif type(working_status) == int:
            working_status = working_status
        else:
            working_status = int(working_status)

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=working_status,
            response_model=response_model,
            unpack_dict=False,
        )

    def search(
        self, search_filter_resource: Union[SearchFilter_Resource, dict]
    ) -> IntegerArrayResult:
        """
        Search implementation to filter for any existing resources based on
        specific criteria.


        :param search_filter_resource: SearchFilter_Resource
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataResource30.search
        response_model = IntegerArrayResult

        if type(search_filter_resource) != SearchFilter_Resource:
            search_filter_resource = SearchFilter_Resource(
                **search_filter_resource
            ).dict()
        else:
            search_filter_resource = search_filter_resource.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter_resource,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_currency(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the currency
        of the selected resource.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getCurrency
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_currency(self, resource_id: int, currency_iso_code: str) -> Result:
        """
        Method to change the currency for the current resource.


        :param resource_id: int
        :param currency_iso_code: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setCurrency
        response_model = Result

        arg = {"resourceID": resource_id, "currencyIsoCode": currency_iso_code}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_supervisor1(self, login_name: str, resource_id: int) -> Result:
        """
        Method to set the supervisor 1.


        :param login_name: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setSupervisor1
        response_model = Result

        arg = {"LoginName": login_name, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_supervisor1(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the loginname
        of the supervisor 1.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getSupervisor1
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_supervisor2(self, login_name: str, resource_id: int) -> Result:
        """
        Method to set the supervisor 2.


        :param login_name: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setSupervisor2
        response_model = Result

        arg = {"LoginName": login_name, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_supervisor2(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the loginname
        of the supervisor 2.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getSupervisor2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_resource_type(self, resource_id: int) -> IntegerResult:
        """
        Returns the ResourceType of the selected resource.


        :param resource_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResource30.getResourceType
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_pricelists2(
        self, sourcelanguage: str, targetlanguage: str, resource_id: int
    ) -> PricelistListResult:
        """
        Method to get all pricelists from a resource, depending on source and/or
        target-language.


        :param sourcelanguage: str
        :param targetlanguage: str
        :param resource_id: int
        :return: PricelistListResult
        """

        proxy = self.__client.plunet_server.DataResource30.getPricelists2
        response_model = PricelistListResult

        arg = {
            "sourcelanguage": sourcelanguage,
            "targetlanguage": targetlanguage,
            "resourceID": resource_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_working_status(
        self, working_status: Union[WorkingStatus, int], resource_id: int
    ) -> Result:
        """
        Method to set the WorkingStatus. Returns an instance of
        Result.


        :param working_status: WorkingStatus
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setWorkingStatus
        response_model = Result

        if type(working_status) == WorkingStatus:
            working_status = working_status.value
        elif type(working_status) == int:
            working_status = working_status
        else:
            working_status = int(working_status)

        arg = {"WorkingStatus": working_status, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_working_status(self, resource_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the
        WorkingStatus of the currently fetched resource.


        :param resource_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResource30.getWorkingStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_resource_type(
        self, resource_type: Union[ResourceType, int], resource_id: int
    ) -> Result:
        """
        Method to set the ResourceType. Returns an instance of
        Result.


        :param resource_type: ResourceType
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setResourceType
        response_model = Result

        if type(resource_type) == ResourceType:
            resource_type = resource_type.value
        elif type(resource_type) == int:
            resource_type = resource_type
        else:
            resource_type = int(resource_type)

        arg = {"ResourceType": resource_type, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelists(self, resource_id: int) -> PricelistListResult:
        """
        Method to get all pricelists from a resource.


        :param resource_id: int
        :return: PricelistListResult
        """

        proxy = self.__client.plunet_server.DataResource30.getPricelists
        response_model = PricelistListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_payment_information(
        self, resource_id: int, payment_info: Union[PaymentInfo, dict]
    ) -> Result:
        """
        Allows to transfer a PaymentInfo object so change multiple payment
        related values.

        External-resources are not allowed to change the account information.


        :param resource_id: int
        :param payment_info: PaymentInfo
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setPaymentInformation
        response_model = Result

        if type(payment_info) != PaymentInfo:
            payment_info = PaymentInfo(**payment_info).dict()
        else:
            payment_info = payment_info.dict()

        arg = {"resourceID": resource_id, "paymentInfo": payment_info}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_payment_information(self, resource_id: int) -> PaymentInfoResult:
        """
        Returns an PaymentInfo included within the result, which contains
        information like IBAN, bank-code or credit account.


        :param resource_id: int
        :return: PaymentInfoResult
        """

        proxy = self.__client.plunet_server.DataResource30.getPaymentInformation
        response_model = PaymentInfoResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_available_payment_method_list(
        self,
    ) -> IntegerArrayResult:
        """
        Returns a list of all available payment methods.


        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataResource30.getAvailablePaymentMethodList
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_payment_method_description(
        self, payment_method_id: int, system_language_code: str
    ) -> StringResult:
        """
        Returns the description of the transfered payment method in the specified
        language.


        :param payment_method_id: int
        :param system_language_code: str
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getPaymentMethodDescription
        response_model = StringResult

        arg = {
            "paymentMethodID": payment_method_id,
            "systemLanguageCode": system_language_code,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def deregister_callback_observer(self, resource_id: int) -> Result:
        """
        Deletes an observer.

        Warning:


        Observer can only deleted by the user who has created them.


        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.deregisterCallback_Observer
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
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
        for any resource.

        If the EventType occurs PBM will call the callback web service,
        which is hosted within your environment. Also each user can only create
        one notify request per event type.


        Please check CallbackResource30 for the exact specification for
        this service.


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackResource30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.registerCallback_Notify
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

    def get_available_account_id_list(
        self,
    ) -> IntegerArrayResult:
        """
        Returns a list of all available accountIDÂ´s.


        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataResource30.getAvailableAccountIDList
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def deregister_callback_notify(self, event_type: Union[EventType, int]) -> Result:
        """
        Deletes an registered notify request.

        Warning:


        Notify requests can only be deleted by the user who has created them).


        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.deregisterCallback_Notify
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
        self, server_authentication_string: str, server_address: str, resource_id: int
    ) -> Result:
        """
        Register to observe a specific object for any supported
        EventType.

        As soon as any supported EventType occurs, PBM will call the
        callback web service, which is hosted within your environment.


        Please check CallbackResource30 for the exact specification for
        this service.


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackResource30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.registerCallback_Observer
        response_model = Result

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "ResourceID": resource_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_full_name(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the full name
        depending on the resourceID .


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getFullName
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_status(self, resource_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the
        ResourceStatus as integer.


        :param resource_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResource30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, resource_id: int) -> Result:
        """
        Method to set the ResourceStatus of the resource. Returns an
        instance of Result.


        :param status: int
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setStatus
        response_model = Result

        arg = {"Status": status, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_resource_objects2(
        self,
        working_status_list: Union[IntegerList, dict],
        status_list: Union[IntegerList, dict],
    ) -> ResourceListResult:
        """
        Returns an instance of ResourceListResult, which contains a list
        of resource objects, which are filtered by the ResourceStatus and the
        WorkingStatus.


        :param working_status_list: IntegerList
        :param status_list: IntegerList
        :return: ResourceListResult
        """

        proxy = self.__client.plunet_server.DataResource30.getAllResourceObjects2
        response_model = ResourceListResult

        if type(working_status_list) != IntegerList:
            working_status_list = IntegerList(**working_status_list).dict()
        else:
            working_status_list = working_status_list.dict()

        if type(status_list) != IntegerList:
            status_list = IntegerList(**status_list).dict()
        else:
            status_list = status_list.dict()

        arg = {"WorkingStatusList": working_status_list, "StatusList": status_list}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_resource_objects(
        self, working_status: Union[WorkingStatus, int], status: int
    ) -> ResourceListResult:
        """
        Returns an instance of ResourceListResult, which contains a list
        of resource objects, which are filtered by the ResourceStatus and the
        WorkingStatus.


        :param working_status: WorkingStatus
        :param status: int
        :return: ResourceListResult
        """

        proxy = self.__client.plunet_server.DataResource30.getAllResourceObjects
        response_model = ResourceListResult

        if type(working_status) == WorkingStatus:
            working_status = working_status.value
        elif type(working_status) == int:
            working_status = working_status
        else:
            working_status = int(working_status)

        arg = {"WorkingStatus": working_status, "Status": status}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_resource_object(self, resource_id: int) -> ResourceResult:
        """
        Returns an instance of ResourceResult, which contains an instance
        of resource.


        :param resource_id: int
        :return: ResourceResult
        """

        proxy = self.__client.plunet_server.DataResource30.getResourceObject
        response_model = ResourceResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_saml_external_id(self, resource_id: int, saml_external_id: str) -> Result:
        """
        Method to set the samlExternalId of a resource.


        :param resource_id: int
        :param saml_external_id: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setSamlExternalId
        response_model = Result

        arg = {"resourceId": resource_id, "samlExternalId": saml_external_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_saml_external_id(self, resource_id: int) -> StringResult:
        """
        Method to get the samlExternalId of a resource


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getSamlExternalId
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert_object(self, resource_in: Union[ResourceIN, dict]) -> IntegerResult:
        """
        Method to create a new resource dataset by Object.

        The method will return an instance of IntegerResult, which contains
        the identifier of the new generated resource. Further API calls via this port
        will manipulate this resource (except methods with an resource id as
        parameter ), until another resource is fetched or the session is invalidated.


        :param resource_in: ResourceIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResource30.insertObject
        response_model = IntegerResult

        if type(resource_in) != ResourceIN:
            resource_in = ResourceIN(**resource_in).dict()
        else:
            resource_in = resource_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_account(self, account_id: int) -> AccountResult:
        """
        Allows the access to account details dependent on the transfered
        accountID, which is part of PaymentInfo.


        :param account_id: int
        :return: AccountResult
        """

        proxy = self.__client.plunet_server.DataResource30.getAccount
        response_model = AccountResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=account_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_fax(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the fax
        address depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getFax
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_name1(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains name1 (last
        name).


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getName1
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_form_of_address(self, form_of_address: int, resource_id: int) -> Result:
        """
        Method to set the FormOfAddressType. Returns an instance of
        Result.


        :param form_of_address: int
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setFormOfAddress
        response_model = Result

        arg = {"FormOfAddress": form_of_address, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_form_of_address(self, resource_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the
        FormOfAddressType.


        :param resource_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResource30.getFormOfAddress
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_website(self, website: str, resource_id: int) -> Result:
        """
        Method to set the website. Returns an instance of Result.


        :param website: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setWebsite
        response_model = Result

        arg = {"Website": website, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_fax(self, fax: str, resource_id: int) -> Result:
        """
        Method to set the fax address. Returns an instance of Result.


        :param fax: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setFax
        response_model = Result

        arg = {"Fax": fax, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_skype_id(self, skype_id: str, resource_id: int) -> Result:
        """
        Method to set the SkypeID. Returns an instance of Result.


        :param skype_id: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setSkypeID
        response_model = Result

        arg = {"SkypeID": skype_id, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_skype_id(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the SkypeID
        depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getSkypeID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_academic_title(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the academic
        title depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getAcademicTitle
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_phone(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the phone
        number depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getPhone
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_name1(self, name: str, resource_id: int) -> Result:
        """
        Method to set name1 (last name). Returns an instance of Result.


        :param name: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setName1
        response_model = Result

        arg = {"Name": name, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_mobile_phone(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the mobile
        phone number depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getMobilePhone
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_website(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the website
        depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getWebsite
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_external_id(self, external_id: str, resource_id: int) -> Result:
        """
        Method to set the external ID. Returns an instance of Result.


        :param external_id: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setExternalID
        response_model = Result

        arg = {"ExternalID": external_id, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_cost_center(self, cost_center: str, resource_id: int) -> Result:
        """
        Method to set the cost center. Returns an instance of Result.


        :param cost_center: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setCostCenter
        response_model = Result

        arg = {"CostCenter": cost_center, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_user_id(self, resource_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the user id
        of the selected resource.


        :param resource_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResource30.getUserId
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_name2(self, name: str, resource_id: int) -> Result:
        """
        Method to set name2 (first name). Returns an instance of Result.


        :param name: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setName2
        response_model = Result

        arg = {"Name": name, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_email(self, e_mail: str, resource_id: int) -> Result:
        """
        Method to set the e-mail address. Returns an instance of
        Result.


        :param e_mail: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setEmail
        response_model = Result

        arg = {"EMail": e_mail, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_opening(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the opening
        depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getOpening
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_academic_title(self, academic_title: str, resource_id: int) -> Result:
        """
        Method to set the academic title. Returns an instance of Result.


        :param academic_title: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setAcademicTitle
        response_model = Result

        arg = {"AcademicTitle": academic_title, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_opening(self, opening: str, resource_id: int) -> Result:
        """
        Method to set the opening. Returns an instance of Result.


        :param opening: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setOpening
        response_model = Result

        arg = {"Opening": opening, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_phone(self, phone_number: str, resource_id: int) -> Result:
        """
        Method to set the phone number. Returns an instance of Result.


        :param phone_number: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setPhone
        response_model = Result

        arg = {"PhoneNumber": phone_number, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_email(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the e-mail
        address depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getEmail
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_external_id(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the external
        ID depending on the resourceID .


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getExternalID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_mobile_phone(self, phone_number: str, resource_id: int) -> Result:
        """
        Method to set the mobile number. Returns an instance of
        Result.


        :param phone_number: str
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResource30.setMobilePhone
        response_model = Result

        arg = {"PhoneNumber": phone_number, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_name2(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains name2 (first
        name).


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getName2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def seek_by_external_id(self, external_id: str) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains the ID
        of the resource dataset, which was identified via the external id.


        :param external_id: str
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResource30.seekByExternalID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=external_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_cost_center(self, resource_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the cost
        center depending on the resourceID.


        :param resource_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResource30.getCostCenter
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )
