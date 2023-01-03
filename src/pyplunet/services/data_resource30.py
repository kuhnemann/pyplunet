from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType, ResourceType
from ..models import IntegerList, PaymentInfo, ResourceIN, SearchFilter_Resource

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataResource30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def delete(self, resource_id: int):
        """
        Method to delete a resource via ID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.delete

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def deregister_callback_notify(self, event_type: EventType):
        """
        Deletes an registered notify request.

        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.deregisterCallback_Notify

        return self.__client.make_request(proxy, event_type.value, unpack_dict=False)

    def deregister_callback_observer(self, resource_id: int):
        """
        Deletes an observer.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.deregisterCallback_Observer

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_academic_title(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the academictitle depending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getAcademicTitle

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_account(self, account_id: int):
        """
        Allows the access to account details dependent on the transferedaccountID, which is part of PaymentInfo.

        :param account_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getAccount

        return self.__client.make_request(proxy, account_id, unpack_dict=False)

    def get_all_resource_objects(self, working_status: int, status: int):
        """
        Returns an instance of ResourceListResult, which contains a listof resource objects, which are filtered by the ResourceStatus and theWorkingStatus.

        :param working_status: int
        :param status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getAllResourceObjects

        arg = {"WorkingStatus": working_status, "Status": status}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_all_resource_objects2(
        self,
        working_status_list: Union[IntegerList, dict],
        status_list: Union[IntegerList, dict],
    ):
        """
        Returns an instance of ResourceListResult, which contains a listof resource objects, which are filtered by the ResourceStatus and theWorkingStatus.

        :param working_status_list: IntegerList
        :param status_list: IntegerList

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getAllResourceObjects2

        if type(working_status_list) != IntegerList:
            working_status_list = IntegerList(**working_status_list).dict()
        else:
            working_status_list = working_status_list.dict()

        if type(status_list) != IntegerList:
            status_list = IntegerList(**status_list).dict()
        else:
            status_list = status_list.dict()

        arg = {"WorkingStatusList": working_status_list, "StatusList": status_list}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_available_account_id_list(
        self,
    ):
        """
        Returns a list of all available accountID´s.


        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getAvailableAccountIDList

    def get_available_payment_method_list(
        self,
    ):
        """
        Returns a list of all available payment methods.


        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getAvailablePaymentMethodList

    def get_cost_center(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the costcenter depending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getCostCenter

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_currency(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the currencyof the selected resource.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getCurrency

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_email(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the e-mailaddress depending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getEmail

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_external_id(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the externalID depending on the resourceID .

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getExternalID

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_fax(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the faxaddress depending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getFax

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_form_of_address(self, resource_id: int):
        """
        Returns an instance of IntegerResult, which contains theFormOfAddressType.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getFormOfAddress

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_full_name(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the full namedepending on the resourceID .

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getFullName

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_mobile_phone(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the mobilephone number depending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getMobilePhone

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_name1(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains name1 (lastname).

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getName1

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_name2(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains name2 (firstname).

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getName2

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_opening(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the openingdepending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getOpening

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_payment_information(self, resource_id: int):
        """
        Returns an PaymentInfo included within the result, which containsinformation like IBAN, bank-code or credit account.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getPaymentInformation

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_payment_method_description(
        self, payment_method_id: int, system_language_code: str
    ):
        """
        Returns the description of the transfered payment method in the specifiedlanguage.

        :param payment_method_id: int
        :param system_language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getPaymentMethodDescription

        arg = {
            "paymentMethodID": payment_method_id,
            "systemLanguageCode": system_language_code,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_phone(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the phonenumber depending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getPhone

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_pricelists(self, resource_id: int):
        """
        Method to get all pricelists from a resource.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getPricelists

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_pricelists2(
        self, source_language: str, target_language: str, resource_id: int
    ):
        """
        Method to get all pricelists from a resource, depending on source and/ortarget-language.

        :param source_language: str
        :param target_language: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getPricelists2

        arg = {
            "SourceLanguage": source_language,
            "TargetLanguage": target_language,
            "resourceID": resource_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_resource_object(self, resource_id: int):
        """
        Returns an instance of ResourceResult, which contains an instanceof resource.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getResourceObject

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_resource_type(self, resource_id: int):
        """
        Returns the ResourceType of the selected resource.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getResourceType

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_saml_external_id(self, resource_id: int):
        """
        Method to get the samlExternalId of a resource

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getSamlExternalId

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_skype_id(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the SkypeIDdepending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getSkypeID

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_status(self, resource_id: int):
        """
        Returns an instance of IntegerResult, which contains theResourceStatus as integer.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getStatus

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_supervisor1(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the loginnameof the supervisor 1.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getSupervisor1

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_supervisor2(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the loginnameof the supervisor 2.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getSupervisor2

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_user_id(self, resource_id: int):
        """
        Returns an instance of IntegerResult, which contains the user idof the selected resource.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getUserId

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_website(self, resource_id: int):
        """
        Returns an instance of StringResult, which contains the websitedepending on the resourceID.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getWebsite

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_working_status(self, resource_id: int):
        """
        Returns an instance of IntegerResult, which contains theWorkingStatus of the currently fetched resource.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.getWorkingStatus

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def insert(self, working_status: int):
        """
        Method to create a new, empty resource dataset.

        :param working_status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.insert

        return self.__client.make_request(proxy, working_status, unpack_dict=False)

    def insert_object(self, resource: Union[ResourceIN, dict]):
        """
        Method to create a new resource dataset by Object.

        :param resource: ResourceIN

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.insertObject

        if type(resource) != ResourceIN:
            resource = ResourceIN(**resource).dict()
        else:
            resource = resource.dict()

        return self.__client.make_request(proxy, resource, unpack_dict=False)

    def register_callback_notify(
        self,
        server_authentication_string: str,
        server_address: str,
        event_type: EventType,
    ):
        """
        Register to get notified when the specified EventType occursfor any resource.

        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.registerCallback_Notify

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "EventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def register_callback_observer(
        self, server_authentication_string: str, server_address: str, resource_id: int
    ):
        """
        Register to observe a specific object for any supportedEventType.

        :param server_authentication_string: str
        :param server_address: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.registerCallback_Observer

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "ResourceID": resource_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def search(self, search_filter: Union[SearchFilter_Resource, dict]):
        """
        Search implementation to filter for any existing resources based onspecific criteria.

        :param search_filter: SearchFilter_Resource

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.search

        if type(search_filter) != SearchFilter_Resource:
            search_filter = SearchFilter_Resource(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(proxy, search_filter, unpack_dict=False)

    def seek_by_external_id(self, external_id: str):
        """
        Method returns an instance of IntegerResult, which contains the IDof the resource dataset, which was identified via the external id.

        :param external_id: str

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.seekByExternalID

        return self.__client.make_request(proxy, external_id, unpack_dict=False)

    def set_academic_title(self, academic_title: str, resource_id: int):
        """
        Method to set the academic title.

        :param academic_title: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setAcademicTitle

        arg = {"AcademicTitle": academic_title, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_cost_center(self, cost_center: str, resource_id: int):
        """
        Method to set the cost center.

        :param cost_center: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setCostCenter

        arg = {"CostCenter": cost_center, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_currency(self, resource_id: int, currency_iso_code: str):
        """
        Method to change the currency for the current resource.

        :param resource_id: int
        :param currency_iso_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setCurrency

        arg = {"resourceID": resource_id, "currencyIsoCode": currency_iso_code}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_email(self, e_mail: str, resource_id: int):
        """
        Method to set the e-mail address.

        :param e_mail: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setEmail

        arg = {"EMail": e_mail, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_external_id(self, external_id: str, resource_id: int):
        """
        Method to set the external ID.

        :param external_id: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setExternalID

        arg = {"ExternalID": external_id, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_fax(self, fax: str, resource_id: int):
        """
        Method to set the fax address.

        :param fax: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setFax

        arg = {"Fax": fax, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_form_of_address(self, form_of_address: int, resource_id: int):
        """
        Method to set the FormOfAddressType.

        :param form_of_address: int
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setFormOfAddress

        arg = {"FormOfAddress": form_of_address, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_mobile_phone(self, phone_number: str, resource_id: int):
        """
        Method to set the mobile number.

        :param phone_number: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setMobilePhone

        arg = {"PhoneNumber": phone_number, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name1(self, name: str, resource_id: int):
        """
        Method to set name1 (last name).

        :param name: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setName1

        arg = {"Name": name, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name2(self, name: str, resource_id: int):
        """
        Method to set name2 (first name).

        :param name: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setName2

        arg = {"Name": name, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_opening(self, opening: str, resource_id: int):
        """
        Method to set the opening.

        :param opening: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setOpening

        arg = {"Opening": opening, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_payment_information(
        self, resource_id: int, payment_info: Union[PaymentInfo, dict]
    ):
        """
        Allows to transfer a PaymentInfo object so change multiple paymentrelated values.

        :param resource_id: int
        :param payment_info: PaymentInfo

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setPaymentInformation

        if type(payment_info) != PaymentInfo:
            payment_info = PaymentInfo(**payment_info).dict()
        else:
            payment_info = payment_info.dict()

        arg = {"resourceID": resource_id, "paymentInfo": payment_info}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_phone(self, phone_number: str, resource_id: int):
        """
        Method to set the phone number.

        :param phone_number: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setPhone

        arg = {"PhoneNumber": phone_number, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_resource_type(self, resource_type: ResourceType, resource_id: int):
        """
        Method to set the ResourceType.

        :param resource_type: ResourceType
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setResourceType

        arg = {"ResourceType": resource_type.value, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_saml_external_id(self, resource_id: int, saml_external_id: str):
        """
        Method to set the samlExternalId of a resource.

        :param resource_id: int
        :param saml_external_id: str

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setSamlExternalId

        arg = {"resourceId": resource_id, "samlExternalId": saml_external_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_skype_id(self, skype_id: str, resource_id: int):
        """
        Method to set the SkypeID.

        :param skype_id: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setSkypeID

        arg = {"SkypeID": skype_id, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, resource_id: int):
        """
        Method to set the ResourceStatus of the resource.

        :param status: int
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setStatus

        arg = {"Status": status, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_supervisor1(self, login_name: str, resource_id: int):
        """
        Method to set the supervisor 1.

        :param login_name: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setSupervisor1

        arg = {"LoginName": login_name, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_supervisor2(self, login_name: str, resource_id: int):
        """
        Method to set the supervisor 2.

        :param login_name: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setSupervisor2

        arg = {"LoginName": login_name, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_website(self, website: str, resource_id: int):
        """
        Method to set the website.

        :param website: str
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setWebsite

        arg = {"Website": website, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_working_status(self, working_status: int, resource_id: int):
        """
        Method to set the WorkingStatus.

        :param working_status: int
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.setWorkingStatus

        arg = {"WorkingStatus": working_status, "resourceID": resource_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, resource: Union[ResourceIN, dict], enabled: bool):
        """
        Updates a resource per Object.

        :param resource: ResourceIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataResource30.update

        if type(resource) != ResourceIN:
            resource = ResourceIN(**resource).dict()
        else:
            resource = resource.dict()

        arg = {"Resource": resource, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
