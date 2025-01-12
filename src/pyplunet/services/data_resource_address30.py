from __future__ import annotations

from typing import TYPE_CHECKING, Union


from ..models import Result, AddressIN, StringResult, IntegerArrayResult, IntegerResult


from ..enums import AddressType

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataResourceAddress30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def update(
        self, address_in: Union[AddressIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        updates an resource address per Object.

        Use EnableNullOrEmptyValues to decide if Null or empty Strings are saved into Plunet or ignored.


        :param address_in: AddressIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.update
        response_model = Result

        if type(address_in) is not AddressIN:
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

    def insert(self, resource_id: int) -> IntegerResult:
        """
        Method to create a new, empty resource address dataset.

        The method will return an instance of IntegerResult, which contains the identifier of the new
        generated resource address.


        :param resource_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.insert
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def delete(self, address_id: int) -> Result:
        """
        Method to delete a resource address via ID.

        Returns an instance of Result.


        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_state(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the state.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getState
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_country(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the country.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getCountry
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

        proxy = self.__client.plunet_server.DataResourceAddress30.setState
        response_model = Result

        arg = {"State": state, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_description(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the address description.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getDescription
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

        proxy = self.__client.plunet_server.DataResourceAddress30.setDescription
        response_model = Result

        arg = {"Description": description, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert2(
        self, resource_id: int, address_in: Union[AddressIN, dict]
    ) -> IntegerResult:
        """
        Method to create a new, address dataset depinding on the tansfered Object


        :param resource_id: int
        :param address_in: AddressIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.insert2
        response_model = IntegerResult

        if type(address_in) is not AddressIN:
            address_in = AddressIN(**address_in).dict()
        else:
            address_in = address_in.dict()

        arg = {"ResourceID": resource_id, "AddressIN": address_in}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_city(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the city.


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getCity
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_name1(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name1 / last name


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getName1
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_name2(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the name2 / first name


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getName2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_street(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains street


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getStreet
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_street2(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains street 2


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getStreet2
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_name1(self, name: str, address_id: int) -> Result:
        """
        Method to set the name1 / last name. Returns an instance of Result.


        :param name: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setName1
        response_model = Result

        arg = {"Name": name, "AddressID": address_id}

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

        proxy = self.__client.plunet_server.DataResourceAddress30.setName2
        response_model = Result

        arg = {"Name": name, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_city(self, city: str, address_id: int) -> Result:
        """
        Method to set city.

        Returns an instance of Result.


        :param city: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setCity
        response_model = Result

        arg = {"City": city, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_street(self, street: str, address_id: int) -> Result:
        """
        Method to set street. Returns an instance of Result.


        :param street: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setStreet
        response_model = Result

        arg = {"Street": street, "AddressID": address_id}

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

        proxy = self.__client.plunet_server.DataResourceAddress30.setStreet2
        response_model = Result

        arg = {"Street2": street2, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_country(self, country: str, address_id: int) -> Result:
        """
        Method to set the country. Returns an instance of Result.


        :param country: str
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setCountry
        response_model = Result

        arg = {"Country": country, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_addresses(self, resource_id: int) -> IntegerArrayResult:
        """
        Returns an instance of IntegerArrayResult, which contains a list of all available addressIDs
        for this resource address


        :param resource_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getAllAddresses
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
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

        proxy = self.__client.plunet_server.DataResourceAddress30.setZip
        response_model = Result

        arg = {"Zip": zip, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_address_id(self, address_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the addressID of the currently fetched
        address.


        :param address_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getAddressID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
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

        proxy = self.__client.plunet_server.DataResourceAddress30.setOffice
        response_model = Result

        arg = {"ExternalID": external_id, "AddressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_office(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the office name


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getOffice
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_zip(self, address_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the zip code


        :param address_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getZip
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_address_type(self, address_id: int) -> IntegerResult:
        """
        Returns an instance of StringResult, which contains the AddressType of
        the currently selected Resource.


        :param address_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getAddressType
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=address_id,
            response_model=response_model,
            unpack_dict=False,
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

        proxy = self.__client.plunet_server.DataResourceAddress30.setAddressType
        response_model = Result

        if type(address_type) is AddressType:
            address_type = address_type.value
        elif type(address_type) is int:
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
