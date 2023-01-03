from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import AddressType
from ..models import AddressIN

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataResourceAddress30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def delete(self, address_id: int):
        """
        Method to delete a resource address via ID.

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.delete

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_address_id(self, address_id: int):
        """
        Returns an instance of IntegerResult, which contains the addressID of the currently fetchedaddress.

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getAddressID

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_address_type(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the AddressType ofthe currently selected Resource.

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getAddressType

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_all_addresses(self, resource_id: int):
        """
        Returns an instance of IntegerArrayResult, which contains a list of all available addressIDsfor this resource address

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getAllAddresses

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def get_city(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the city.

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getCity

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_country(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the country.

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getCountry

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_description(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the address description.

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getDescription

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_name1(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the name1 / last name

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getName1

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_name2(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the name2 / first name

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getName2

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_office(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the office name

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getOffice

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_state(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the state.

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getState

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_street(self, address_id: int):
        """
        Returns an instance of StringResult, which contains street

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getStreet

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_street2(self, address_id: int):
        """
        Returns an instance of StringResult, which contains street 2

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getStreet2

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def get_zip(self, address_id: int):
        """
        Returns an instance of StringResult, which contains the zip code

        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.getZip

        return self.__client.make_request(proxy, address_id, unpack_dict=False)

    def insert(self, resource_id: int):
        """
        Method to create a new, empty resource address dataset.

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.insert

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)

    def insert2(self, resource_id: int, address: Union[AddressIN, dict]):
        """
        Method to create a new, address dataset depinding on the tansfered Object

        :param resource_id: int
        :param address: AddressIN

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.insert2

        if type(address) != AddressIN:
            address = AddressIN(**address).dict()
        else:
            address = address.dict()

        arg = {"ResourceID": resource_id, "Address": address}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_address_type(self, address_type: AddressType, address_id: int):
        """
        Method to set the AddressType.

        :param address_type: AddressType
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setAddressType

        arg = {"AddressType": address_type.value, "addressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_city(self, city: str, address_id: int):
        """
        Method to set city.

        :param city: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setCity

        arg = {"City": city, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_country(self, country: str, address_id: int):
        """
        Method to set the country.

        :param country: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setCountry

        arg = {"Country": country, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_description(self, description: str, address_id: int):
        """
        Method to set the address description.

        :param description: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setDescription

        arg = {"Description": description, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name1(self, name: str, address_id: int):
        """
        Method to set the name1 / last name.

        :param name: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setName1

        arg = {"Name": name, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_name2(self, name: str, address_id: int):
        """
        Method to set the name2 / first name.

        :param name: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setName2

        arg = {"Name": name, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_office(self, office: str, address_id: int):
        """
        Method to set the office name.

        :param office: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setOffice

        arg = {"Office": office, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_state(self, state: str, address_id: int):
        """
        Method to set state.

        :param state: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setState

        arg = {"State": state, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_street(self, street: str, address_id: int):
        """
        Method to set street.

        :param street: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setStreet

        arg = {"Street": street, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_street2(self, street2: str, address_id: int):
        """
        Method to set street 2.

        :param street2: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setStreet2

        arg = {"Street2": street2, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_zip(self, zip: str, address_id: int):
        """
        Method to set zip code.

        :param zip: str
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.setZip

        arg = {"Zip": zip, "AddressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, address: Union[AddressIN, dict], enabled: bool):
        """
        updates an resource address per Object.

        :param address: AddressIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataResourceAddress30.update

        if type(address) != AddressIN:
            address = AddressIN(**address).dict()
        else:
            address = address.dict()

        arg = {"Address": address, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
