from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import CustomerContactIN

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataCustomerContact30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_address_id(self, contact_id: int):
        """
        Returns an instance of IntegerResult, which contains the address id of the customercontact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getAddressID

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_all_contact_objects(self, customer_id: int):
        """
        Returns an instance of CustomerContactListResult, which contains a list of all availablecustomer contact objects.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getAllContactObjects

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_all_contacts(self, customer_id: int):
        """
        Returns an instance of IntegerArrayResult, which contains a list of all available customercontact ids.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getAllContacts

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def get_contact_object(self, contact_id: int):
        """
        Returns an instance of CustomerContactResult, which contains a specific customer contactobject.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getContactObject

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_cost_center(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the cost center of the currently selectedcustomer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getCostCenter

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_customer_id(self, contact_id: int):
        """
        Returns an instance of IntegerResult, which contains CustomerID of the currently selectedcustomer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getCustomerID

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_email(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the e-mail address of the currentlyselected customer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getEmail

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_external_id(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the external id of the currently selectedcustomer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getExternalID

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_fax(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the fax address of the currently selectedcustomer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getFax

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_mobile_phone(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the mobile phone number of the currentlyselected customer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getMobilePhone

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_name1(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the name1 / last name of the currentlyselected customer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getName1

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_name2(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the name2 / first name of the currentlyselected customer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getName2

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_phone(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the phone number of the currently selectedcustomer contact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getPhone

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_status(self, contact_id: int):
        """
        Returns an instance of IntegerResult, which contains the ContactPersonStatus asinteger.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getStatus

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_supervisor1(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the loginname of the supervisor 1.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getSupervisor1

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_supervisor2(self, contact_id: int):
        """
        Returns an instance of StringResult, which contains the loginname of the supervisor 2.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getSupervisor2

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def get_user_id(self, contact_id: int):
        """
        Returns an instance of IntegerResult, which contains the user id of the selected customercontact.

        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getUserId

        return self.__client.make_request(proxy, contact_id, unpack_dict=False)

    def insert(self, customer_id: int):
        """
        Method to create a new, empty customer contact dataset.

        :param customer_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.insert

        return self.__client.make_request(proxy, customer_id, unpack_dict=False)

    def insert2(self, customer_contact: Union[CustomerContactIN, dict]):
        """
        Method to create a new, empty customer contact dataset by Object.

        :param customer_contact: CustomerContactIN

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.insert2

        if type(customer_contact) != CustomerContactIN:
            customer_contact = CustomerContactIN(**customer_contact).dict()
        else:
            customer_contact = customer_contact.dict()

        return self.__client.make_request(proxy, customer_contact, unpack_dict=False)

    def seek_by_external_id(self, external_id: str):
        """
        Returns an instance of IntegerArrayResult, which contains a list of customer contactIDs.

        :param external_id: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.seekByExternalID

        return self.__client.make_request(proxy, external_id, unpack_dict=False)

    def set_address_id(self, address_id: int, contact_id: int):
        """
        Method to set the default address for this customer contact.

        :param address_id: int
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setAddressID

        arg = {"AddressID": address_id, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_cost_center(self, cost_center: str, contact_id: int):
        """
        Method to set the cost center.

        :param cost_center: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setCostCenter

        arg = {"CostCenter": cost_center, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_id(self, customer_id: int, contact_id: int):
        """
        Method to set the CustomerID.

        :param customer_id: int
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setCustomerID

        arg = {"CustomerID": customer_id, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_email(self, e_mail: str, contact_id: int):
        """
        Method to set the e-mail address.

        :param e_mail: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setEmail

        arg = {"EMail": e_mail, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_external_id(self, external_id: str, contact_id: int):
        """
        Method to set the external ID.

        :param external_id: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setExternalID

        arg = {"ExternalID": external_id, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_fax(self, fax: str, contact_id: int):
        """
        Method to set the fax address.

        :param fax: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setFax

        arg = {"Fax": fax, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_mobile_phone(self, phone_number: str, contact_id: int):
        """
        Method to set mobile number.

        :param phone_number: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setMobilePhone

        arg = {"PhoneNumber": phone_number, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name1(self, name: str, contact_id: int):
        """
        Method to set the name1 / last name.

        :param name: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setName1

        arg = {"Name": name, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name2(self, name: str, contact_id: int):
        """
        Method to set the name2 / first name.

        :param name: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setName2

        arg = {"Name": name, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_phone(self, phone_number: str, contact_id: int):
        """
        Method to set phone number.

        :param phone_number: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setPhone

        arg = {"PhoneNumber": phone_number, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, contact_id: int):
        """
        Method to set the status of the customer contact.

        :param status: int
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setStatus

        arg = {"Status": status, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_supervisor1(self, login_name: str, contact_id: int):
        """
        Method to set the supervisor 1

        :param login_name: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setSupervisor1

        arg = {"LoginName": login_name, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_supervisor2(self, login_name: str, contact_id: int):
        """
        Method to set the supervisor 2.

        :param login_name: str
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setSupervisor2

        arg = {"LoginName": login_name, "ContactID": contact_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, customer_contact: Union[CustomerContactIN, dict], enabled: bool):
        """
        updates an customer contact per Object.

        :param customer_contact: CustomerContactIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.update

        if type(customer_contact) != CustomerContactIN:
            customer_contact = CustomerContactIN(**customer_contact).dict()
        else:
            customer_contact = customer_contact.dict()

        arg = {"CustomerContact": customer_contact, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
