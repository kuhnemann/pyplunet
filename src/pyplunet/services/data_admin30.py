from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataAdmin30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_available_countries(self, language_code: str):
        """
        Method returns an instance of CountryListResult,which contains an array of available countries in the system,returned in the language specified by the language code.

        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableCountries

        return self.__client.make_request(proxy, language_code, unpack_dict=False)

    def get_available_document_templates(
        self,
    ):
        """
        Method returns an instance of StringArrayResult,which contains an array of template names.


        :return:
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableDocumentTemplates

    def get_available_languages(self, language_code: str):
        """
        Method returns an instance of LanguageListResult,which contains an array of available languages in the system,returned in the language specified by the language code.

        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableLanguages

        return self.__client.make_request(proxy, language_code, unpack_dict=False)

    def get_available_services(self, language_code: str):
        """
        Method returns an instance of ServiceListResult,which contains an array of the available services/job types in the system,returned in the language specified by the language code - Internal API user canaccess all services, customers only these that have been marked as available for customers.

        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableServices

        return self.__client.make_request(proxy, language_code, unpack_dict=False)

    def get_company_code_list(
        self,
    ):
        """
        Returns a list of all possible company-codes.


        :return:
        """

        proxy = self.__client.plunet_server.DataAdmin30.getCompanyCodeList

    def get_domestic_currency(
        self,
    ):
        """
        Returns the default currency.


        :return:
        """

        proxy = self.__client.plunet_server.DataAdmin30.getDomesticCurrency

    def get_list_of_registered_callbacks(
        self,
    ):
        """
        Returns a list of all registered callbacks (observer &amp; notifies) to the current user


        :return:
        """

        proxy = self.__client.plunet_server.DataAdmin30.getListOfRegisteredCallbacks

    def get_system_currencies(
        self,
    ):
        """
        Returns a list of all currencies configured within the administrationarea


        :return:
        """

        proxy = self.__client.plunet_server.DataAdmin30.getSystemCurrencies
