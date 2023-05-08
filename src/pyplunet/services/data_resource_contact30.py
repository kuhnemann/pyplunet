from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import (
    IntegerArrayResult,
    IntegerResult,
    ResourceContactIN,
    ResourceContactListResult,
    ResourceContactResult,
    Result,
    StringResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataResourceContact30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def update(
        self,
        resource_contact_in: Union[ResourceContactIN, dict],
        enable_null_or_empty_values: bool,
    ) -> Result:
        """
        updates an resource contact per Object. Use EnableNullOrEmptyValues to decide if Null or empty
        Strings are saved into Plunet or should ignored.


        :param resource_contact_in: ResourceContactIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.update
        response_model = Result

        if type(resource_contact_in) != ResourceContactIN:
            resource_contact_in = ResourceContactIN(**resource_contact_in).dict()
        else:
            resource_contact_in = resource_contact_in.dict()

        arg = {
            "ResourceContactIN": resource_contact_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert(
        self,
    ) -> IntegerResult:
        """
        Deprecated.


        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_resource_id(self, resource_id: int, contact_id: int) -> Result:
        """
        Method to set the resourceId. Returns an instance of Result.


        :param resource_id: int
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setResourceID
        response_model = Result

        arg = {"ResourceID": resource_id, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_contact_object(self, contact_id: int) -> ResourceContactResult:
        """
        Returns an instance of ResourceContactResult, which contains a specific resource contact object.


        :param contact_id: int
        :return: ResourceContactResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getContactObject
        response_model = ResourceContactResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_all_contacts(self, resource_id: int) -> IntegerArrayResult:
        """
        Returns an instance of IntegerArrayResult, which contains a list of all available resource
        contact IDs.


        :param resource_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getAllContacts
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_address_id(self, address_id: int, contact_id: int) -> Result:
        """
        Method to set the default addres for this resource contact. Use the DataResourceAddress25
        service, to manage addresses for this resource contact.


        :param address_id: int
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setAddressID
        response_model = Result

        arg = {"AddressID": address_id, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_status(self, contact_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the status id as integer.
        Status codes:

        0 = not active
        1 = active


        :param contact_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, contact_id: int) -> Result:
        """
        Method to set the status of the resource contact. Returns an instance of Result. Status
        codes:

        0 = not active
        1 = active


        :param status: int
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setStatus
        response_model = Result

        arg = {"Status": status, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_saml_external_id(self, contact_id: int, saml_external_id: str) -> Result:
        """
        Sets the samlExternalId for a contact person.


        :param contact_id: int
        :param saml_external_id: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setSamlExternalId
        response_model = Result

        arg = {"ContactID": contact_id, "SamlExternalID": saml_external_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_saml_external_id(self, contact_id: int) -> StringResult:
        """
        Gets the samlExternalId for a contact person.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getSamlExternalId
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_all_contact_objects(self, resource_id: int) -> ResourceContactListResult:
        """
        Returns an instance of ResourceContactListResult, which contains a list of all available resource contact objects.


        :param resource_id: int
        :return: ResourceContactListResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getAllContactObjects
        response_model = ResourceContactListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_address_id(self, contact_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the address id of the resource contact. Use
        the DataResourceAddress25 service, to manage addresses for this resource contact.


        :param contact_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getAddressID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_fax(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the fax address


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getFax
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_name1(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name1 / last name


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getName1
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_form_of_address(self, form_of_address: int, contact_id: int) -> Result:
        """
        Method to set the form of address. Returns an instance of Result. Form of address:

        1 = Mr
        2 = Mrs
        3 = Company


        :param form_of_address: int
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setFormOfAddress
        response_model = Result

        arg = {"FormOfAddress": form_of_address, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_form_of_address(self, contact_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the id of the form of address.
        Form of address:

        1 = Mr
        2 = Mrs
        3 = Company


        :param contact_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getFormOfAddress
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_fax(self, fax: str, contact_id: int) -> Result:
        """
        Method to set the fax address. Returns an instance of Result.


        :param fax: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setFax
        response_model = Result

        arg = {"Fax": fax, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_skype_id(self, skype_id: str, contact_id: int) -> Result:
        """
        Method to set the SkypeID. Returns an instance of Result.


        :param skype_id: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setSkypeID
        response_model = Result

        arg = {"SkypeID": skype_id, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_skype_id(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the SkypeID


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getSkypeID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_academic_title(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the academic title


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getAcademicTitle
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert2(
        self, resource_contact_in: Union[ResourceContactIN, dict]
    ) -> IntegerResult:
        """
        Method to create a new resource depending on transfered object


        :param resource_contact_in: ResourceContactIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.insert2
        response_model = IntegerResult

        if type(resource_contact_in) != ResourceContactIN:
            resource_contact_in = ResourceContactIN(**resource_contact_in).dict()
        else:
            resource_contact_in = resource_contact_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_contact_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_phone(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the phone number


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getPhone
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_name1(self, name: str, contact_id: int) -> Result:
        """
        Method to set the name1 / last name. Returns an instance of Result.


        :param name: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setName1
        response_model = Result

        arg = {"Name": name, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_mobile_phone(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the mobile phone number


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getMobilePhone
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_external_id(self, external_id: str, contact_id: int) -> Result:
        """
        Method to set the external ID. Returns an instance of Result.


        :param external_id: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setExternalID
        response_model = Result

        arg = {"ExternalID": external_id, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_name2(self, name: str, contact_id: int) -> Result:
        """
        Method to set the name2 / first name. Returns an instance of Result.


        :param name: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setName2
        response_model = Result

        arg = {"Name": name, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_email(self, e_mail: str, contact_id: int) -> Result:
        """
        Method to set the e-mail address. Returns an instance of Result.


        :param e_mail: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setEmail
        response_model = Result

        arg = {"EMail": e_mail, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_opening(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the opening


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getOpening
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_academic_title(self, academic_title: str, contact_id: int) -> Result:
        """
        Method to set the academic title. Returns an instance of Result.


        :param academic_title: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setAcademicTitle
        response_model = Result

        arg = {"AcademicTitle": academic_title, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_opening(self, opening: str, contact_id: int) -> Result:
        """
        Method to set the opening. Returns an instance of Result.


        :param opening: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setOpening
        response_model = Result

        arg = {"Opening": opening, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_phone(self, phone_number: str, contact_id: int) -> Result:
        """
        Method to set phone number. Returns an instance of Result.


        :param phone_number: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setPhone
        response_model = Result

        arg = {"PhoneNumber": phone_number, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_email(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the e-mail address


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getEmail
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_external_id(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the external id


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getExternalID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_mobile_phone(self, phone_number: str, contact_id: int) -> Result:
        """
        Method to set mobile number. Returns an instance of Result.


        :param phone_number: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setMobilePhone
        response_model = Result

        arg = {"PhoneNumber": phone_number, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_name2(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name2 / first name


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getName2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def seek_by_external_id(self, external_id: str) -> IntegerArrayResult:
        """
        Returns an instance of IntegerArrayResult, which contains a list of resource contact IDs.


        :param external_id: str
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.seekByExternalID
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=external_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_resource_id(self, contact_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains resourceId


        :param contact_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getResourceID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )
