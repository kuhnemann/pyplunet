from __future__ import annotations

from typing import TYPE_CHECKING, Union


from ..models import (
    PropertyValueListResult,
    CallbackListResult,
    CurrencyList,
    LanguageListResult,
    StringArrayResult,
    languageResult,
    CountryListResult,
    PriceUnitListResult,
    PropertyListResult,
    ServiceListResult,
    StringResult,
    WorkflowListResult,
    CompanyCodeListResult,
    TextmoduleListResult,
)


from ..enums import PropertyUsageArea, CatType, TextModuleUsageArea

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataAdmin30:
    def __init__(self, client: PlunetClient):
        self.__client = client

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

    def get_language_cat_code(
        self, language_name: str, cat_type: Union[CatType, int]
    ) -> StringResult:
        """
        Method returns the language cat code depending on the provided cat tool type and language


        :param language_name: str
        :param cat_type: CatType
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getLanguageCatCode
        response_model = StringResult

        if type(cat_type) is CatType:
            cat_type = cat_type.value
        elif type(cat_type) is int:
            cat_type = cat_type
        else:
            cat_type = int(cat_type)

        arg = {"languageName": language_name, "catType": cat_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_property_value_list(
        self, property_name_english: str, language_code: str
    ) -> PropertyValueListResult:
        """
        Returns a list of all possible Property Values


        :param property_name_english: str
        :param language_code: str
        :return: PropertyValueListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getPropertyValueList
        response_model = PropertyValueListResult

        arg = {
            "PropertyNameEnglish": property_name_english,
            "LanguageCode": language_code,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

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

    def get_available_countries(self, language_code: str) -> CountryListResult:
        """
        Method returns an instance of CountryListResult, which contains an array of available
        countries in the system, returned in the language specified by the language code.


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

    def get_available_properties(
        self, property_usage_area: Union[PropertyUsageArea, int], main_id: int
    ) -> PropertyListResult:
        """
        Returns a list of all available properties


        :param property_usage_area: PropertyUsageArea
        :param main_id: int
        :return: PropertyListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableProperties
        response_model = PropertyListResult

        if type(property_usage_area) is PropertyUsageArea:
            property_usage_area = property_usage_area.value
        elif type(property_usage_area) is int:
            property_usage_area = property_usage_area
        else:
            property_usage_area = int(property_usage_area)

        arg = {"PropertyUsageArea": property_usage_area, "MainID": main_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_available_price_units(
        self, language_code: str, service: str
    ) -> PriceUnitListResult:
        """
        Returns a list of priceUnit related to the specified service.
        Possible services can be obtained over getAvailableServices(String, String)


        :param language_code: str
        :param service: str
        :return: PriceUnitListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailablePriceUnits
        response_model = PriceUnitListResult

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_available_workflows(
        self,
    ) -> WorkflowListResult:
        """
        Returns a list of all available workflows.


        :return: WorkflowListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableWorkflows
        response_model = WorkflowListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=None,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_available_languages(self, language_code: str) -> LanguageListResult:
        """
        Method returns an instance of LanguageListResult, which contains an array of available
        languages in the system, returned in the language specified by the language code.


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

    def get_system_currencies(
        self,
    ) -> CurrencyList:
        """
        Returns a list of all currencies configured within the administration area


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

    def get_available_document_templates(
        self,
    ) -> StringArrayResult:
        """
        Method returns an instance of StringArrayResult, which contains an array of template
        names.


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

    def get_available_text_modules(
        self,
        language_code: str,
        text_module_usage_area: Union[TextModuleUsageArea, int],
        main_id: int,
    ) -> TextmoduleListResult:
        """
        Returns a list of all available text modules for the specified entity


        :param language_code: str
        :param text_module_usage_area: TextModuleUsageArea
        :param main_id: int
        :return: TextmoduleListResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.getAvailableTextModules
        response_model = TextmoduleListResult

        if type(text_module_usage_area) is TextModuleUsageArea:
            text_module_usage_area = text_module_usage_area.value
        elif type(text_module_usage_area) is int:
            text_module_usage_area = text_module_usage_area
        else:
            text_module_usage_area = int(text_module_usage_area)

        arg = {
            "languageCode": language_code,
            "textModuleUsageArea": text_module_usage_area,
            "MainID": main_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def seek_language_by_cat_code(
        self, cat_code: str, cat_type: Union[CatType, int]
    ) -> languageResult:
        """
        Returns the related language from a cat code


        :param cat_code: str
        :param cat_type: CatType
        :return: languageResult
        """

        proxy = self.__client.plunet_server.DataAdmin30.seekLanguageByCatCode
        response_model = languageResult

        if type(cat_type) is CatType:
            cat_type = cat_type.value
        elif type(cat_type) is int:
            cat_type = cat_type
        else:
            cat_type = int(cat_type)

        arg = {"catCode": cat_code, "catType": cat_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_available_services(self, language_code: str) -> ServiceListResult:
        """
        Method returns an instance of ServiceListResult, which contains an array of the
        available services/job types in the system, returned in the language specified by the language
        code - Internal API user can access all services, customers only these that have been marked as
        available for customers.


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
