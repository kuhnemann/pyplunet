from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import (
    CustomerContactIN,
    CustomerContactListResult,
    CustomerContactResult,
    IntegerArrayResult,
    IntegerResult,
    Result,
    StringResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataCustomerContact30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def update(
        self,
        customer_contact_in: Union[CustomerContactIN, dict],
        enable_null_or_empty_values: bool,
    ) -> Result:
        """
        updates an customer contact per Object.

        Use EnableNullOrEmptyValues to decide if Null or empty Strings are saved into Plunet or should
        ignored.


        :param customer_contact_in: CustomerContactIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.update
        response_model = Result

        if type(customer_contact_in) != CustomerContactIN:
            customer_contact_in = CustomerContactIN(**customer_contact_in).dict()
        else:
            customer_contact_in = customer_contact_in.dict()

        arg = {
            "CustomerContactIN": customer_contact_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert(self, partner_id: int) -> IntegerResult:
        """
        Method to create a new, empty customer contact dataset.

        The method will return an instance of IntegerResult, which contains the identifier of the new
        generated customer contact.


        :param partner_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=partner_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_contact_object(self, contact_id: int) -> CustomerContactResult:
        """
        Returns an instance of CustomerContactResult, which contains a specific customer contact
        object.


        :param contact_id: int
        :return: CustomerContactResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getContactObject
        response_model = CustomerContactResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_supervisor1(self, login_name: str, contact_id: int) -> Result:
        """
        Method to set the supervisor 1


        :param login_name: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setSupervisor1
        response_model = Result

        arg = {"LoginName": login_name, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_supervisor1(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the loginname of the supervisor 1.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getSupervisor1
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_supervisor2(self, login_name: str, contact_id: int) -> Result:
        """
        Method to set the supervisor 2.


        :param login_name: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setSupervisor2
        response_model = Result

        arg = {"LoginName": login_name, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_supervisor2(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the loginname of the supervisor 2.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getSupervisor2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_all_contacts(self, customer_id: int) -> IntegerArrayResult:
        """
        Returns an instance of IntegerArrayResult, which contains a list of all available customer
        contact ids.


        :param customer_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getAllContacts
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_customer_id(self, customer_id: int, contact_id: int) -> Result:
        """
        Method to set the CustomerID.

        Returns an instance of Result.


        :param customer_id: int
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setCustomerID
        response_model = Result

        arg = {"CustomerID": customer_id, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_address_id(self, address_id: int, contact_id: int) -> Result:
        """
        Method to set the default address for this customer contact.

        Use the DataResourceAddress25 service, to manage addresses for this customer contact.


        :param address_id: int
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setAddressID
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
        Returns an instance of IntegerResult, which contains the ContactPersonStatus as
        integer.


        :param contact_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, contact_id: int) -> Result:
        """
        Method to set the status of the customer contact.

        Returns an instance of Result.


        :param status: int
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setStatus
        response_model = Result

        arg = {"Status": status, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_contact_objects(self, customer_id: int) -> CustomerContactListResult:
        """
        Returns an instance of CustomerContactListResult, which contains a list of all available
        customer contact objects.


        :param customer_id: int
        :return: CustomerContactListResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getAllContactObjects
        response_model = CustomerContactListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_address_id(self, contact_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the address id of the customer
        contact.

        Use the DataResourceAddress25 service, to manage addresses for this customer contact.


        :param contact_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getAddressID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_fax(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the fax address of the currently selected
        customer contact.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getFax
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_name1(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name1 / last name of the currently
        selected customer contact.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getName1
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_fax(self, fax: str, contact_id: int) -> Result:
        """
        Method to set the fax address.

        Returns an instance of Result.


        :param fax: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setFax
        response_model = Result

        arg = {"Fax": fax, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert2(
        self, customer_contact_in: Union[CustomerContactIN, dict]
    ) -> IntegerResult:
        """
        Method to create a new, empty customer contact dataset by Object.

        The method will return an instance of IntegerResult, which contains the identifier of the new
        generated customer contact. Further api calls via this port will maninpulate this customer
        contact (except methods with an customer contact id as parameter ), until another customer
        contact is fetched or the session is invalidated.


        :param customer_contact_in: CustomerContactIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.insert2
        response_model = IntegerResult

        if type(customer_contact_in) != CustomerContactIN:
            customer_contact_in = CustomerContactIN(**customer_contact_in).dict()
        else:
            customer_contact_in = customer_contact_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_contact_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_phone(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the phone number of the currently selected
        customer contact.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getPhone
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_name1(self, name: str, contact_id: int) -> Result:
        """
        Method to set the name1 / last name.

        Returns an instance of Result.


        :param name: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setName1
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
        Returns an instance of StringResult, which contains the mobile phone number of the currently
        selected customer contact.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getMobilePhone
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_external_id(self, external_id: str, contact_id: int) -> Result:
        """
        Method to set the external ID.

        Returns an instance of Result.


        :param external_id: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setExternalID
        response_model = Result

        arg = {"ExternalID": external_id, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_cost_center(self, cost_center: str, contact_id: int) -> Result:
        """
        Method to set the cost center.

        Returns an instance of Result.


        :param cost_center: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setCostCenter
        response_model = Result

        arg = {"CostCenter": cost_center, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_user_id(self, contact_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the user id of the selected customer
        contact.


        :param contact_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getUserId
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_name2(self, name: str, contact_id: int) -> Result:
        """
        Method to set the name2 / first name.

        Returns an instance of Result.


        :param name: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setName2
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
        Method to set the e-mail address.

        Returns an instance of Result.


        :param e_mail: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setEmail
        response_model = Result

        arg = {"EMail": e_mail, "ContactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_phone(self, phone_number: str, contact_id: int) -> Result:
        """
        Method to set phone number.

        Returns an instance of Result.


        :param phone_number: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setPhone
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
        Returns an instance of StringResult, which contains the e-mail address of the currently
        selected customer contact.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getEmail
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_external_id(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the external id of the currently selected
        customer contact.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getExternalID
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_mobile_phone(self, phone_number: str, contact_id: int) -> Result:
        """
        Method to set mobile number.

        Returns an instance of Result.


        :param phone_number: str
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.setMobilePhone
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
        Returns an instance of StringResult, which contains the name2 / first name of the currently
        selected customer contact.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getName2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def seek_by_external_id(self, external_id: str) -> IntegerArrayResult:
        """
        Returns an instance of IntegerArrayResult, which contains a list of customer contactIDs.


        :param external_id: str
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.seekByExternalID
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=external_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_cost_center(self, contact_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the cost center of the currently selected
        customer contact.


        :param contact_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getCostCenter
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_customer_id(self, contact_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains CustomerID of the currently selected
        customer contact.


        :param contact_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerContact30.getCustomerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=contact_id,
            response_model=response_model,
            unpack_dict=False,
        )
