from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import AddressType
from ..models import AddressIN, IntegerArrayResult, IntegerResult, Result, StringResult

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataCustomerAddress30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def update(
        self, address_in: Union[AddressIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        updates an customer address per Object.
        Use EnableNullOrEmptyValues to decide if Null or empty Strings are saved
        into Plunet or ignored.


        :param address_in: AddressIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.update
        response_model = Result

        if type(address_in) != AddressIN:
            address_in = AddressIN(**address_in).dict()
        else:
            address_in = address_in.dict()

        arg = {
            "AddressIN": address_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete(self, address_id: int) -> Result:
        """
        Method to delete a customer address via ID. Returns an instance of Result.


        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_state(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the state depending
        on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getState
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert(self, partner_id: int) -> IntegerResult:
        """
        Method to create a new, empty customer address dataset.
        The method will return an instance of IntegerResult, which contains the identifier
        of the new generated customer address.


        :param partner_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=partner_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_country(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the country
        depending on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getCountry
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_state(self, state: str, address_id: int) -> Result:
        """
        Method to set state. Returns an instance of Result.


        :param state: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setState
        response_model = Result

        arg = {"State": state, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_address_type(self, address_id: int) -> IntegerResult:
        """
        Returns an instance of StringResult, which contains the AddressType of
        the currently selected customer.


        :param address_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getAddressType
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_description(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the address description.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getDescription
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_description(self, description: str, address_id: int) -> Result:
        """
        Method to set the address description. Returns an instance of Result.


        :param description: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setDescription
        response_model = Result

        arg = {"Description": description, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_sales_taxation_type(self, address_id: int, language: str) -> StringResult:
        """
        Returns the defined sales tax id./b>
        This is not a standard feature and requires an active module


        :param address_id: int
        :param language: str
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getSalesTaxationType
        response_model = StringResult

        arg = {"AddressID": address_id, "language": language}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_address_type(
        self, address_type: Union[AddressType, int], address_id: int
    ) -> Result:
        """
        Method to set the AddressType. Returns an instance of Result.


        :param address_type: AddressType
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setAddressType
        response_model = Result

        if type(address_type) == AddressType:
            address_type = address_type.value
        elif type(address_type) == int:
            address_type = address_type
        else:
            address_type = int(address_type)

        arg = {"AddressType": address_type, "addressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_taxation_type(self, address_id: int, language: str) -> StringResult:
        """
        Returns the defined taxation type for the specified address
        This is not a standard feature and requires an active module


        :param address_id: int
        :param language: str
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getTaxationType
        response_model = StringResult

        arg = {"AddressID": address_id, "language": language}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_street2(self, street2: str, address_id: int) -> Result:
        """
        Method to set street 2. Returns an instance of Result.


        :param street2: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setStreet2
        response_model = Result

        arg = {"Street2": street2, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_street2(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains street 2
        depending on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getStreet2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_city(self, city: str, address_id: int) -> Result:
        """
        Method to set city. Returns an instance of Result.


        :param city: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setCity
        response_model = Result

        arg = {"City": city, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_city(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the city
        depending on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getCity
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_country(self, country: str, address_id: int) -> Result:
        """
        Method to set the country. Returns an instance of Result.


        :param country: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setCountry
        response_model = Result

        arg = {"Country": country, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_addresses(self, customer_id: int) -> IntegerArrayResult:
        """
        Returns an instance of IntegerArrayResult, which contains a list of all
        available addressIDs for this customer.


        :param customer_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getAllAddresses
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=customer_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_address_id(
        self,
    ) -> IntegerResult:
        """
        Deprecated.


        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getAddressID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_office(self, external_id: str, address_id: int) -> Result:
        """
        Method to set the office name. Returns an instance of Result.


        :param external_id: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setOffice
        response_model = Result

        arg = {"ExternalID": external_id, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_street(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains street
        depending on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getStreet
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_street(self, street: str, address_id: int) -> Result:
        """
        Method to set street. Returns an instance of Result.


        :param street: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setStreet
        response_model = Result

        arg = {"Street": street, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_zip(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the zip code
        depending on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getZip
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_office(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the office name
        depending on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getOffice
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_zip(self, zip: str, address_id: int) -> Result:
        """
        Method to set zip code. Returns an instance of Result.


        :param zip: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setZip
        response_model = Result

        arg = {"Zip": zip, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_name1(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name1 / last name
        depending on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getName1
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert2(
        self, customer_id: int, address_in: Union[AddressIN, dict]
    ) -> IntegerResult:
        """
        Method to create a new customer address depending on the transfered object.


        :param customer_id: int
        :param address_in: AddressIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.insert2
        response_model = IntegerResult

        if type(address_in) != AddressIN:
            address_in = AddressIN(**address_in).dict()
        else:
            address_in = address_in.dict()

        arg = {"CustomerID": customer_id, "AddressIN": address_in}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_name1(self, name: str, address_id: int) -> Result:
        """
        Method to set the name1 / last name. Returns an instance of Result.


        :param name: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setName1
        response_model = Result

        arg = {"Name": name, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_cost_center(self, cost_center: str, address_id: int) -> Result:
        """
        Method to set the cost center. Returns an instance of Result.


        :param cost_center: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setCostCenter
        response_model = Result

        arg = {"CostCenter": cost_center, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_name2(self, name: str, address_id: int) -> Result:
        """
        Method to set the name2 / first name. Returns an instance of Result.


        :param name: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.setName2
        response_model = Result

        arg = {"Name": name, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_name2(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name2 / first name
        depending on the transfered AddressID.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getName2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_cost_center(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the cost center
        of the specified customer contact.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomerAddress30.getCostCenter
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )
