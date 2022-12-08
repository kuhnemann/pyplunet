from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataAdmin30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_available_languages(self, interface_lang="en"):
        return self.__client.make_request(
            self.__client.plunet_server.DataAdmin30.getAvailableLanguages,
            interface_lang,
        )

    def get_available_services(self, interface_lang="en"):
        return self.__client.make_request(
            self.__client.plunet_server.DataAdmin30.getAvailableServices, interface_lang
        )

    def get_available_countries(self, interface_lang="en"):
        return self.__client.make_request(
            self.__client.plunet_server.DataAdmin30.getAvailableCountries,
            interface_lang,
        )

    def get_available_document_templates(self):
        return self.__client.make_request(
            self.__client.plunet_server.DataAdmin30.getAvailableDocumentTemplates, None
        )

    def get_company_code_list(self):
        return self.__client.make_request(
            self.__client.plunet_server.DataAdmin30.getCompanyCodeList, None
        )

    def get_domestic_currency(self):
        return self.__client.make_request(
            self.__client.plunet_server.DataAdmin30.getDomesticCurrency, None
        )

    def get_list_of_registered_callbacks(self):
        return self.__client.make_request(
            self.__client.plunet_server.DataAdmin30.getListOfRegisteredCallbacks, None
        )

    def get_system_currencies(self):
        return self.__client.make_request(
            self.__client.plunet_server.DataAdmin30.getSystemCurrencies, None
        )
