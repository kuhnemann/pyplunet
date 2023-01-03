from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import CustomerIN, IntegerList, PaymentInfo, SearchFilter_Customer

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataCustomer30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def delete(self, customer_id: int):
        """
        Method to delete a customer via ID.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.delete

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def deregister_callback_notify(self, event_type: EventType):
        """
        Deletes an registered notify request.

        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.deregisterCallback_Notify

        return self.__client.make_request(proxy, event_type.value, unpack_dict=False)

    def deregister_callback_observer(self, customer_id: int):
        """
        Deletes an observer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.deregisterCallback_Observer

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_academic_title(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the academic titleof the currently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAcademicTitle

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_account(self, account_id: int):
        """
        Allows the access to account details dependent on the transferedaccountID.

        :param account_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAccount

        return self.__client.make_request(proxy, account_id, unpack_dict=False)

    def get_account_manager_id(self, customer_id: int):
        """
        Returns the resourceID of the account-manager of thethe specified customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAccountManagerID

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_all_customer_objects(self, status: int):
        """
        Returns an instance of CustomerListResult, which contains a list ofcustomers, which are filtered by the CustomerStatus.

        :param status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAllCustomerObjects

        return self.__client.make_request(proxy, status, unpack_dict=False)

    def get_all_customer_objects2(self, status_list: Union[IntegerList, dict]):
        """
        Returns an instance of CustomerListResult, which contains a list ofcustomers, which are filtered by a list of CustomerStatus.

        :param status_list: IntegerList

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAllCustomerObjects2

        if type(status_list) != IntegerList:
            status_list = IntegerList(**status_list).dict()
        else:
            status_list = status_list.dict()

        return self.__client.make_request(proxy, status_list, unpack_dict=False)

    def get_available_account_id_list(
        self,
    ):
        """
        Returns a list of all available accountID´s.


        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAvailableAccountIDList

    def get_available_payment_method_list(
        self,
    ):
        """
        Returns a list of all available payment methods.


        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAvailablePaymentMethodList

    def get_available_workflows(self, customer_id: int):
        """
        Returns a list of all available workflows for the customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getAvailableWorkflows

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_created_by_resource_id(self, customer_id: int):
        """
        Returns the ResourceID which has created the Customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getCreatedByResourceID

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_currency(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the currencyof the selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getCurrency

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_customer_object(self, customer_id: int):
        """
        Returns an instance of CustomerResult, which contains an instance of customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getCustomerObject

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_date_of_initial_contact(self, customer_id: int):
        """
        Returns the Date set as initial contact.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getDateOfInitialContact

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_dossier(self, customer_id: int):
        """
        Returns the value of the dossier field.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getDossier

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_email(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the e-mail addressof the currently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getEmail

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_external_id(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the external id ofthe currently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getExternalID

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_fax(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the fax address ofthe currently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getFax

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_form_of_address(self, customer_id: int):
        """
        Returns an instance of IntegerResult, which contains the id of the form of address.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getFormOfAddress

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_full_name(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the full name of thecurrently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getFullName

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_mobile_phone(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the mobile phonenumber of the currently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getMobilePhone

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_name1(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the name1 / last nameof the currently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getName1

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_name2(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the name2 / firstname of the currently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getName2

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_opening(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the opening of thecurrently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getOpening

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_payment_information(self, customer_id: int):
        """
        Returns an PaymentInfo included within the result, whichcontains information like IBAN, bank-code or credit account.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getPaymentInformation

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_payment_method_description(
        self, payment_method_id: int, system_language_code: str
    ):
        """
        Returns the description of the transfered payment method in thespecified language.

        :param payment_method_id: int
        :param system_language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getPaymentMethodDescription

        arg = {
            "paymentMethodID": payment_method_id,
            "systemLanguageCode": system_language_code,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_phone(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the phone number ofthe currently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getPhone

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_project_manager_id(self, customer_id: int):
        """
        Returns the resourceID of the project-manager of thethe specified customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getProjectManagerID

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_skype_id(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the SkypeID of thecurrently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getSkypeID

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_source_of_contact(self, customer_id: int):
        """
        Returns the value of the &#39;source of contact&#39; test field.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getSourceOfContact

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_status(self, customer_id: int):
        """
        Returns an instance of IntegerResult, which contains the status id asinteger.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getStatus

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_website(self, customer_id: int):
        """
        Returns an instance of StringResult, which contains the website of thecurrently selected customer.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.getWebsite

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def insert(
        self,
    ):
        """
        Method to create a new, empty customer dataset.


        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.insert

    def insert2(self, customer: Union[CustomerIN, dict]):
        """
        Method to create a new customer due to transfered object.

        :param customer: CustomerIN

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.insert2

        if type(customer) != CustomerIN:
            customer = CustomerIN(**customer).dict()
        else:
            customer = customer.dict()

        return self.__client.make_request(proxy, customer, unpack_dict=False)

    def register_callback_notify(
        self,
        server_authentication_string: str,
        server_address: str,
        event_type: EventType,
    ):
        """
        Register to get notified when the specified event (EventType)occurs for any customerIf the EventType occurs PBM will call the callback web service,which is hosted within your environment.

        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.registerCallback_Notify

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "EventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def register_callback_observer(
        self, server_authentication_string: str, server_address: str, customer_id: int
    ):
        """
        Register to observe a specific object for any supportedEventType.

        :param server_authentication_string: str
        :param server_address: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.registerCallback_Observer

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "CustomerID": customer_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def search(self, search_filter: Union[SearchFilter_Customer, dict]):
        """
        Search implementation to filter for any existing customer based onspecific criteria.

        :param search_filter: SearchFilter_Customer

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.search

        if type(search_filter) != SearchFilter_Customer:
            search_filter = SearchFilter_Customer(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(proxy, search_filter, unpack_dict=False)

    def seek_by_external_id(self, external_id: str):
        """
        Method returns an instance of IntegerResult, which contains the ID ofthe customer dataset, which was identified via the external id.

        :param external_id: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.seekByExternalID

        return self.__client.make_request(proxy, external_id, unpack_dict=False)

    def set_academic_title(self, academic_title: str, customer_id: int):
        """
        Method to set the academic title.

        :param academic_title: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setAcademicTitle

        arg = {"AcademicTitle": academic_title, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_account_manager_id(self, customer_id: int, resource_id: int):
        """
        Sets a resource as the account manager for the specified customer.

        :param customer_id: int
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setAccountManagerID

        arg = {"customerID": customer_id, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_date_of_initial_contact(
        self, customer_id: int, date_initial_contact: datetime
    ):
        """
        Sets the provided Date as initial contact.

        :param customer_id: int
        :param date_initial_contact: datetime

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setDateOfInitialContact

        arg = {"customerID": customer_id, "dateInitialContact": date_initial_contact}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_dossier(self, customer_id: int, dossier: str):
        """
        Sets the dossier field.

        :param customer_id: int
        :param dossier: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setDossier

        arg = {"customerID": customer_id, "dossier": dossier}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_email(self, e_mail: str, customer_id: int):
        """
        Method to set the e-mail address.

        :param e_mail: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setEmail

        arg = {"EMail": e_mail, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_external_id(self, external_id: str, customer_id: int):
        """
        Method to set the external ID.

        :param external_id: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setExternalID

        arg = {"ExternalID": external_id, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_fax(self, fax: str, customer_id: int):
        """
        Method to set the fax address.

        :param fax: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setFax

        arg = {"Fax": fax, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_form_of_address(self, form_of_address: int, customer_id: int):
        """
        Method to set the form of address.

        :param form_of_address: int
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setFormOfAddress

        arg = {"FormOfAddress": form_of_address, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_mobile_phone(self, phone_number: str, customer_id: int):
        """
        Method to set mobile number.

        :param phone_number: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setMobilePhone

        arg = {"PhoneNumber": phone_number, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name1(self, name: str, customer_id: int):
        """
        Method to set the name1 / last name.

        :param name: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setName1

        arg = {"Name": name, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name2(self, name: str, customer_id: int):
        """
        Method to set the name2 / first name.

        :param name: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setName2

        arg = {"Name": name, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_opening(self, opening: str, customer_id: int):
        """
        Method to set the opening.

        :param opening: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setOpening

        arg = {"Opening": opening, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_payment_information(
        self, customer_id: int, payment_info: Union[PaymentInfo, dict]
    ):
        """
        Allows to transfer a PaymentInfo object so changemultiple payment related values.

        :param customer_id: int
        :param payment_info: PaymentInfo

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setPaymentInformation

        if type(payment_info) != PaymentInfo:
            payment_info = PaymentInfo(**payment_info).dict()
        else:
            payment_info = payment_info.dict()

        arg = {"customerID": customer_id, "paymentInfo": payment_info}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_phone(self, phone_number: str, customer_id: int):
        """
        Method to set phone number.

        :param phone_number: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setPhone

        arg = {"PhoneNumber": phone_number, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_manager_id(self, customer_id: int, resource_id: int):
        """
        Sets a resource as the project manager for the specified customer.

        :param customer_id: int
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setProjectManagerID

        arg = {"customerID": customer_id, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_skype_id(self, skype_id: str, customer_id: int):
        """
        Method to set the SkypeID.

        :param skype_id: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setSkypeID

        arg = {"SkypeID": skype_id, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_source_of_contact(self, customer_id: int, text: str):
        """
        Sets the value of the &#39;source of contact&#39; test field.

        :param customer_id: int
        :param text: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setSourceOfContact

        arg = {"customerID": customer_id, "text": text}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, customer_id: int):
        """
        Method to set the CustomerStatus.

        :param status: int
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setStatus

        arg = {"Status": status, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_website(self, website: str, customer_id: int):
        """
        Method to set the website.

        :param website: str
        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.setWebsite

        arg = {"Website": website, "customerID": customer_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, customer: Union[CustomerIN, dict], enabled: bool):
        """
        Updates an Customer per Object.

        :param customer: CustomerIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomer30.update

        if type(customer) != CustomerIN:
            customer = CustomerIN(**customer).dict()
        else:
            customer = customer.dict()

        arg = {"customer": customer, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
