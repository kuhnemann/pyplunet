from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import (
    CallbackListResult,
    CompanyCodeListResult,
    CountryListResult,
    CurrencyList,
    LanguageListResult,
    ServiceListResult,
    StringArrayResult,
    StringResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataAdmin30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def get_domestic_currency(
        self,
    ) -> StringResult:
        """
        Returns the default currency.


        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getDomesticCurrency
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_available_document_templates(
        self,
    ) -> StringArrayResult:
        """
        Method returns an instance of StringArrayResult,
        which contains an array of template names.


        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableDocumentTemplates
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_list_of_registered_callbacks(
        self,
    ) -> CallbackListResult:
        """
        Returns a list of all registered callbacks (observer & notifies) to the current user


        :return: CallbackListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getListOfRegisteredCallbacks
        response_model = CallbackListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_company_code_list(
        self,
    ) -> CompanyCodeListResult:
        """
        Returns a list of all possible company-codes.


        :return: CompanyCodeListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getCompanyCodeList
        response_model = CompanyCodeListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_available_services(self, language_code: str) -> ServiceListResult:
        """
        Method returns an instance of ServiceListResult,
        which contains an array of the available services/job types in the system,
        returned in the language specified by the language code - Internal API user can
        access all services, customers only these that have been marked as available for customers.


        :param language_code: str
        :return: ServiceListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableServices
        response_model = ServiceListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=language_code,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_available_countries(self, language_code: str) -> CountryListResult:
        """
        Method returns an instance of CountryListResult,
        which contains an array of available countries in the system,
        returned in the language specified by the language code.


        :param language_code: str
        :return: CountryListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableCountries
        response_model = CountryListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=language_code,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_system_currencies(
        self,
    ) -> CurrencyList:
        """
        Returns a list of all currencies configured within the administration
        area


        :return: CurrencyList
        """

        proxy = self.__client.plunet_server.DataAdmin30.getSystemCurrencies
        response_model = CurrencyList

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_available_languages(self, language_code: str) -> LanguageListResult:
        """
        Method returns an instance of LanguageListResult,
        which contains an array of available languages in the system,
        returned in the language specified by the language code.


        :param language_code: str
        :return: LanguageListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableLanguages
        response_model = LanguageListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=language_code,
            response_model=response_model,
            unpack_dict=False,
        )
