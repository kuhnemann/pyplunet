from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import (
    AccountResult,
    CustomerIN,
    CustomerListResult,
    CustomerResult,
    DateResult,
    IntegerArrayResult,
    IntegerList,
    IntegerResult,
    PaymentInfo,
    PaymentInfoResult,
    Result,
    SearchFilter_Customer,
    StringResult,
    WorkflowListResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataCustomer30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def update(
        self, customer_in: Union[CustomerIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        Updates an Customer per Object.
        Use EnableNullOrEmptyValues to decide if Null or empty Strings are saved
        into Plunet or ignored.


        :param customer_in: CustomerIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.update
        response_model = Result

        if type(customer_in) != CustomerIN:
            customer_in = CustomerIN(**customer_in).dict()
        else:
            customer_in = customer_in.dict()

        arg = {
            "CustomerIN": customer_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete(self, customer_id: int) -> Result:
        """
        Method to delete a customer via ID. Returns an instance of Result.


        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert(
        self,
    ) -> IntegerResult:
        """
        Method to create a new, empty customer dataset.
        The method will return an instance of IntegerResult, which contains
        the identifier of the new generated customer.


        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def search(
        self, search_filter: Union[SearchFilter_Customer, dict]
    ) -> IntegerArrayResult:
        """
        Search implementation to filter for any existing customer based on
        specific criteria.


        :param search_filter: SearchFilter_Customer
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.search
        response_model = IntegerArrayResult

        if type(search_filter) != SearchFilter_Customer:
            search_filter = SearchFilter_Customer(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_currency(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the currency
        of the selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getCurrency
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_project_manager_id(self, customer_id: int) -> IntegerResult:
        """
        Returns the resourceID of the project-manager of the
        the specified customer.

        Returns resourceID = 0 when no project-manager is specified.


        :param customer_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getProjectManagerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_created_by_resource_id(self, customer_id: int) -> IntegerResult:
        """
        Returns the ResourceID which has created the Customer.


        :param customer_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getCreatedByResourceID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_payment_information(
        self, customer_id: int, payment_info: Union[PaymentInfo, dict]
    ) -> Result:
        """
        Allows to transfer a PaymentInfo object so change
        multiple payment related values.
        External-resources are not allowed to change account information


        :param customer_id: int
        :param payment_info: PaymentInfo
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setPaymentInformation
        response_model = Result

        if type(payment_info) != PaymentInfo:
            payment_info = PaymentInfo(**payment_info).dict()
        else:
            payment_info = payment_info.dict()

        arg = {"customerID": customer_id, "paymentInfo": payment_info}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_account_manager_id(self, customer_id: int) -> IntegerResult:
        """
        Returns the resourceID of the account-manager of the
        the specified customer.

        Returns resourceID = 0 when no account-manager is specified.


        :param customer_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAccountManagerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_account_manager_id(self, customer_id: int, resource_id: int) -> Result:
        """
        Sets a resource as the account manager for the specified customer.


        :param customer_id: int
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setAccountManagerID
        response_model = Result

        arg = {"customerID": customer_id, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_project_manager_id(self, customer_id: int, resource_id: int) -> Result:
        """
        Sets a resource as the project manager for the specified customer.


        :param customer_id: int
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setProjectManagerID
        response_model = Result

        arg = {"customerID": customer_id, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_available_workflows(self, customer_id: int) -> WorkflowListResult:
        """
        Returns a list of all available workflows for the customer.


        :param customer_id: int
        :return: WorkflowListResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAvailableWorkflows
        response_model = WorkflowListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_payment_information(self, customer_id: int) -> PaymentInfoResult:
        """
        Returns an PaymentInfo included within the result, which
        contains information like IBAN, bank-code or credit account.


        :param customer_id: int
        :return: PaymentInfoResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getPaymentInformation
        response_model = PaymentInfoResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
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

        proxy = self.__client.plunet_server.DataCustomer30.getAvailablePaymentMethodList
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_source_of_contact(self, customer_id: int, text: str) -> Result:
        """
        Sets the value of the 'source of contact' test field.
        Located in contacts -> customers -> marketing


        :param customer_id: int
        :param text: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setSourceOfContact
        response_model = Result

        arg = {"customerID": customer_id, "text": text}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_date_of_initial_contact(self, customer_id: int) -> DateResult:
        """
        Returns the Date set as initial contact.


        :param customer_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getDateOfInitialContact
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_payment_method_description(
        self, payment_method_id: int, system_language_code: str
    ) -> StringResult:
        """
        Returns the description of the transfered payment method in the
        specified language.


        :param payment_method_id: int
        :param system_language_code: str
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getPaymentMethodDescription
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

    def get_source_of_contact(self, customer_id: int) -> StringResult:
        """
        Returns the value of the 'source of contact' test field.
        Located in contacts -> customers -> marketing


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getSourceOfContact
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def deregister_callback_observer(self, customer_id: int) -> Result:
        """
        Deletes an observer.
        Warning: observer can only deleted by the user who has created them


        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.deregisterCallback_Observer
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
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
        Register to get notified when the specified event (EventType)
        occurs for any customer

        If the EventType occurs PBM will call the callback web service,
        which is hosted within your environment. Please check
        CallbackCustomer30 for the exact specification for this service.


        Warning: each user can only create one notifier per event


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackCustomer30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.registerCallback_Notify
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

    def set_date_of_initial_contact(
        self, customer_id: int, date_initial_contact: datetime
    ) -> Result:
        """
        Sets the provided Date as initial contact.


        :param customer_id: int
        :param date_initial_contact: datetime
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setDateOfInitialContact
        response_model = Result

        arg = {"customerID": customer_id, "dateInitialContact": date_initial_contact}

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

        proxy = self.__client.plunet_server.DataCustomer30.getAvailableAccountIDList
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
        Warning: notify requests can only be deleted by the user who has created them


        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.deregisterCallback_Notify
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
        self, server_authentication_string: str, server_address: str, customer_id: int
    ) -> Result:
        """
        Register to observe a specific object for any supported
        EventType.

        As soon as any supported event occurs, PBM will call the callback web
        service, which is hosted within your environment. Please check
        CallbackCustomer30 for the exact specification for this service.


        (each user can only create one observer per id)


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackCustomer30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.registerCallback_Observer
        response_model = Result

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "CustomerID": customer_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_full_name(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the full name of the
        currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getFullName
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_status(self, customer_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the status id as
        integer.


        :param customer_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, customer_id: int) -> Result:
        """
        Method to set the CustomerStatus. Returns an instance of Result.


        :param status: int
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setStatus
        response_model = Result

        arg = {"Status": status, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_customer_objects2(
        self, status_list: Union[IntegerList, dict]
    ) -> CustomerListResult:
        """
        Returns an instance of CustomerListResult, which contains a list of
        customers, which are filtered by a list of CustomerStatus.


        :param status_list: IntegerList
        :return: CustomerListResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAllCustomerObjects2
        response_model = CustomerListResult

        if type(status_list) != IntegerList:
            status_list = IntegerList(**status_list).dict()
        else:
            status_list = status_list.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=status_list,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_customer_object(self, customer_id: int) -> CustomerResult:
        """
        Returns an instance of CustomerResult, which contains an instance of customer.


        :param customer_id: int
        :return: CustomerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getCustomerObject
        response_model = CustomerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_all_customer_objects(self, status: int) -> CustomerListResult:
        """
        Returns an instance of CustomerListResult, which contains a list of
        customers, which are filtered by the CustomerStatus.


        :param status: int
        :return: CustomerListResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAllCustomerObjects
        response_model = CustomerListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=status,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_account(self, account_id: int) -> AccountResult:
        """
        Allows the access to account details dependent on the transfered
        accountID.


        :param account_id: int
        :return: AccountResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAccount
        response_model = AccountResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=account_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_dossier(self, customer_id: int, dossier: str) -> Result:
        """
        Sets the dossier field.


        :param customer_id: int
        :param dossier: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setDossier
        response_model = Result

        arg = {"customerID": customer_id, "dossier": dossier}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_dossier(self, customer_id: int) -> StringResult:
        """
        Returns the value of the dossier field.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getDossier
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_fax(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the fax address of
        the currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getFax
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_name1(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name1 / last name
        of the currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getName1
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_form_of_address(self, form_of_address: int, customer_id: int) -> Result:
        """
        Method to set the form of address. Returns an instance of Result.


        :param form_of_address: int
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setFormOfAddress
        response_model = Result

        arg = {"FormOfAddress": form_of_address, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_form_of_address(self, customer_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the id of the form of address.


        :param customer_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getFormOfAddress
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_website(self, website: str, customer_id: int) -> Result:
        """
        Method to set the website. Returns an instance of Result.


        :param website: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setWebsite
        response_model = Result

        arg = {"Website": website, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_fax(self, fax: str, customer_id: int) -> Result:
        """
        Method to set the fax address. Returns an instance of Result.


        :param fax: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setFax
        response_model = Result

        arg = {"Fax": fax, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_skype_id(self, skype_id: str, customer_id: int) -> Result:
        """
        Method to set the SkypeID. Returns an instance of Result.


        :param skype_id: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setSkypeID
        response_model = Result

        arg = {"SkypeID": skype_id, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_skype_id(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the SkypeID of the
        currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getSkypeID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_academic_title(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the academic title
        of the currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAcademicTitle
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert2(self, customer_in: Union[CustomerIN, dict]) -> IntegerResult:
        """
        Method to create a new customer due to transfered object.


        :param customer_in: CustomerIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.insert2
        response_model = IntegerResult

        if type(customer_in) != CustomerIN:
            customer_in = CustomerIN(**customer_in).dict()
        else:
            customer_in = customer_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_phone(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the phone number of
        the currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getPhone
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_name1(self, name: str, customer_id: int) -> Result:
        """
        Method to set the name1 / last name. Returns an instance of Result.


        :param name: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setName1
        response_model = Result

        arg = {"Name": name, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_mobile_phone(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the mobile phone
        number of the currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getMobilePhone
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_website(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the website of the
        currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getWebsite
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_external_id(self, external_id: str, customer_id: int) -> Result:
        """
        Method to set the external ID. Returns an instance of Result.


        :param external_id: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setExternalID
        response_model = Result

        arg = {"ExternalID": external_id, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_name2(self, name: str, customer_id: int) -> Result:
        """
        Method to set the name2 / first name. Returns an instance of Result.


        :param name: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setName2
        response_model = Result

        arg = {"Name": name, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_email(self, e_mail: str, customer_id: int) -> Result:
        """
        Method to set the e-mail address. Returns an instance of Result.


        :param e_mail: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setEmail
        response_model = Result

        arg = {"EMail": e_mail, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_opening(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the opening of the
        currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getOpening
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_academic_title(self, academic_title: str, customer_id: int) -> Result:
        """
        Method to set the academic title. Returns an instance of Result.


        :param academic_title: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setAcademicTitle
        response_model = Result

        arg = {"AcademicTitle": academic_title, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_opening(self, opening: str, customer_id: int) -> Result:
        """
        Method to set the opening. Returns an instance of Result.


        :param opening: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setOpening
        response_model = Result

        arg = {"Opening": opening, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_phone(self, phone_number: str, customer_id: int) -> Result:
        """
        Method to set phone number. Returns an instance of Result.


        :param phone_number: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setPhone
        response_model = Result

        arg = {"PhoneNumber": phone_number, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_email(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the e-mail address
        of the currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getEmail
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_external_id(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the external id of
        the currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getExternalID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_mobile_phone(self, phone_number: str, customer_id: int) -> Result:
        """
        Method to set mobile number. Returns an instance of Result.


        :param phone_number: str
        :param customer_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomer30.setMobilePhone
        response_model = Result

        arg = {"PhoneNumber": phone_number, "customerID": customer_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_name2(self, customer_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name2 / first
        name of the currently selected customer.


        :param customer_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.getName2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def seek_by_external_id(self, external_id: str) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains the ID of
        the customer dataset, which was identified via the external id.


        :param external_id: str
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomer30.seekByExternalID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=external_id,
            response_model=response_model,
            unpack_dict=False,
        )
