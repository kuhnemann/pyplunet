from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import ResourceContactIN

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataResourceContact30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_academic_title(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the academic title

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getAcademicTitle

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_address_id(self, contact_id: int):
        """
        Returns an instance of IntegerResult, which contains the address id of the resource contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getAddressID

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_all_contact_objects(self, resource_id: int):
        """
        Returns an instance of ResourceContactListResult, which contains a list of all available resource contact objects.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getAllContactObjects

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_all_contacts(self, resource_id: int):
        """
        Returns an instance of IntegerArrayResult, which contains a list of all available resourcecontact IDs.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getAllContacts

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_contact_object(self, contact_id: int):
        """
        Returns an instance of ResourceContactResult, which contains a specific resource contact object.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getContactObject

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_email(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the e-mail address

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getEmail

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_external_id(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the external id

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getExternalID

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_fax(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the fax address

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getFax

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_form_of_address(self, contact_id: int):
        """
        Returns an instance of IntegerResult, which contains the id of the form of address.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getFormOfAddress

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_mobile_phone(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the mobile phone number

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getMobilePhone

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_name1(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the name1 / last name

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getName1

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_name2(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the name2 / first name

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getName2

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_opening(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the opening

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getOpening

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_phone(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the phone number

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getPhone

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_resource_id(self, contact_id: int):
        """
        Returns an instance of IntegerResult, which contains resourceId

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getResourceID

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_saml_external_id(self, contact_id: int):
        """
        Gets the samlExternalId for a contact person.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getSamlExternalId

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_skype_id(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the SkypeID

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getSkypeID

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_status(self, contact_id: int):
        """
        Returns an instance of IntegerResult, which contains the status id as integer.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.getStatus

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def insert(
        self,
    ):
        """
        Deprecated.


        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.insert

    def insert2(self, resource_contact: Union[ResourceContactIN, dict]):
        """
        Method to create a new resource depending on transfered object

        :param resource_contact: ResourceContactIN

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.insert2

        if type(resource_contact) != ResourceContactIN:
            resource_contact = ResourceContactIN(**resource_contact).dict()
        else:
            resource_contact = resource_contact.dict()

        return self.__client.make_request(proxy, resource_contact, unpack_dict=False)

    def seek_by_external_id(self, external_id: str):
        """
        Returns an instance of IntegerArrayResult, which contains a list of resource contact IDs.

        :param external_id: str

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.seekByExternalID

        return self.__client.make_request(proxy, external_id, unpack_dict=False)

    def set_academic_title(self, academic_title: str, contact_id: int):
        """
        Method to set the academic title.

        :param academic_title: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setAcademicTitle

        arg = {"AcademicTitle": academic_title, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_address_id(self, address_id: int, contact_id: int):
        """
        Method to set the default addres for this resource contact.

        :param address_id: int
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setAddressID

        arg = {"AddressID": address_id, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_email(self, e_mail: str, contact_id: int):
        """
        Method to set the e-mail address.

        :param e_mail: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setEmail

        arg = {"EMail": e_mail, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_external_id(self, external_id: str, contact_id: int):
        """
        Method to set the external ID.

        :param external_id: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setExternalID

        arg = {"ExternalID": external_id, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_fax(self, fax: str, contact_id: int):
        """
        Method to set the fax address.

        :param fax: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setFax

        arg = {"Fax": fax, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_form_of_address(self, form_of_address: int, contact_id: int):
        """
        Method to set the form of address.

        :param form_of_address: int
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setFormOfAddress

        arg = {"FormOfAddress": form_of_address, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_mobile_phone(self, phone_number: str, contact_id: int):
        """
        Method to set mobile number.

        :param phone_number: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setMobilePhone

        arg = {"PhoneNumber": phone_number, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name1(self, name: str, contact_id: int):
        """
        Method to set the name1 / last name.

        :param name: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setName1

        arg = {"Name": name, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name2(self, name: str, contact_id: int):
        """
        Method to set the name2 / first name.

        :param name: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setName2

        arg = {"Name": name, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_opening(self, opening: str, contact_id: int):
        """
        Method to set the opening.

        :param opening: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setOpening

        arg = {"Opening": opening, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_phone(self, phone_number: str, contact_id: int):
        """
        Method to set phone number.

        :param phone_number: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setPhone

        arg = {"PhoneNumber": phone_number, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_resource_id(self, resource_id: int, contact_id: int):
        """
        Method to set the resourceId.

        :param resource_id: int
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setResourceID

        arg = {"ResourceID": resource_id, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_saml_external_id(self, contact_id: int, saml_external_id: str):
        """
        Sets the samlExternalId for a contact person.

        :param contact_id: int
        :param saml_external_id: str

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setSamlExternalId

        arg = {"ContactID": contact_id, "samlExternalId": saml_external_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_skype_id(self, skype_id: str, contact_id: int):
        """
        Method to set the SkypeID.

        :param skype_id: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setSkypeID

        arg = {"SkypeID": skype_id, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, contact_id: int):
        """
        Method to set the status of the resource contact.

        :param status: int
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.setStatus

        arg = {"Status": status, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, resource_contact: Union[ResourceContactIN, dict], enabled: bool):
        """
        updates an resource contact per Object.

        :param resource_contact: ResourceContactIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceContact30.update

        if type(resource_contact) != ResourceContactIN:
            resource_contact = ResourceContactIN(**resource_contact).dict()
        else:
            resource_contact = resource_contact.dict()

        arg = {"ResourceContact": resource_contact, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
