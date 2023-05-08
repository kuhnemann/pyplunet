from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import PropertyUsageArea, TextModuleUsageArea
from ..models import (
    IntegerList,
    PropertyResult,
    Result,
    StringResult,
    TextmoduleIN,
    TextmoduleResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataCustomFields30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def get_property(
        self,
        property_name_english: str,
        property_usage_area: Union[PropertyUsageArea, int],
        main_id: int,
    ) -> PropertyResult:
        """
        Returns a PropertyResult  depending on the usage area and object related ID.
        Properties can be configured over admin/properties.
        The PropertyNameEnglish can be obtained there.
        The type of the MainID is related to the used PropertyUsageArea.
        e.g. Should the property be related to an order, the propertyusageArea
        must be set to PropertyUsageArea.ORDER


        :param property_name_english: str
        :param property_usage_area: PropertyUsageArea
        :param main_id: int
        :return: PropertyResult
        """

        proxy = self.__client.plunet_server.DataCustomFields30.getProperty
        response_model = PropertyResult

        if type(property_usage_area) == PropertyUsageArea:
            property_usage_area = property_usage_area.value
        elif type(property_usage_area) == int:
            property_usage_area = property_usage_area
        else:
            property_usage_area = int(property_usage_area)

        arg = {
            "PropertyNameEnglish": property_name_english,
            "PropertyUsageArea": property_usage_area,
            "MainID": main_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_property_value_list(
        self,
        property_name_english: str,
        property_usage_area: Union[PropertyUsageArea, int],
        property_value_list: Union[IntegerList, dict],
        main_id: int,
    ) -> Result:
        """
        Changes the current selected property value for the specific object
        (mainID) to the specified property value ID.
        Possible property values for the property can be obtained over
        getProperty(String, String, int, int).
        Properties can be configured over admin/properties.
        The PropertyNameEnglish can be obtained there.
        The type of the MainID is related to the used PropertyUsageArea.
        e.g. Should the property be related to an order, the propertyusageArea
        must be set to PropertyUsageArea.ORDER
        Note:
        Properties can also be modified over general plunet api calls. Please
        check PropertyUsageArea for more details, which call can affect
        which kind of properties.


        :param property_name_english: str
        :param property_usage_area: PropertyUsageArea
        :param property_value_list: IntegerList
        :param main_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomFields30.setPropertyValueList
        response_model = Result

        if type(property_value_list) != IntegerList:
            property_value_list = IntegerList(**property_value_list).dict()
        else:
            property_value_list = property_value_list.dict()

        if type(property_usage_area) == PropertyUsageArea:
            property_usage_area = property_usage_area.value
        elif type(property_usage_area) == int:
            property_usage_area = property_usage_area
        else:
            property_usage_area = int(property_usage_area)

        arg = {
            "PropertyNameEnglish": property_name_english,
            "PropertyUsageArea": property_usage_area,
            "PropertyValueList": property_value_list,
            "MainID": main_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_property_value_text(
        self, property_name_english: str, property_value_id: int, language_code: str
    ) -> StringResult:
        """
        Returns the value text dependent on the language-code and propertyValueID.
        Language-Codes can be configured over admin/languages
        Properties can be configured over admin/properties.
        The PropertyNameEnglish can be obtained there.


        :param property_name_english: str
        :param property_value_id: int
        :param language_code: str
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCustomFields30.getPropertyValueText
        response_model = StringResult

        arg = {
            "PropertyNameEnglish": property_name_english,
            "PropertyValueID": property_value_id,
            "languageCode": language_code,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_textmodule(
        self,
        flag: str,
        text_module_usage_area: Union[TextModuleUsageArea, int],
        id: int,
        language_code: str,
    ) -> TextmoduleResult:
        """
        Returns a text-module depending on the flag and transfered parameters.
        Text-modules can be configured over admin/template/template
        The language code represents the language abbreviation defined in the field "UI language" in Admin ->Document templates ->Languages.
        The Main ID is depending on the defined usage area within
        TextmoduleIN.getTextModuleUsageArea(). e.g. if
        TextModuleUsageArea.ORDER is specified you have to provide an valid OrderID as MainID.


        :param flag: str
        :param text_module_usage_area: TextModuleUsageArea
        :param id: int
        :param language_code: str
        :return: TextmoduleResult
        """

        proxy = self.__client.plunet_server.DataCustomFields30.getTextmodule
        response_model = TextmoduleResult

        if type(text_module_usage_area) == TextModuleUsageArea:
            text_module_usage_area = text_module_usage_area.value
        elif type(text_module_usage_area) == int:
            text_module_usage_area = text_module_usage_area
        else:
            text_module_usage_area = int(text_module_usage_area)

        arg = {
            "Flag": flag,
            "TextModuleUsageArea": text_module_usage_area,
            "ID": id,
            "languageCode": language_code,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_textmodule(
        self, textmodule_in: Union[TextmoduleIN, dict], id: int, language_code: str
    ) -> Result:
        """
        Allows to change the selected value/s of the object (MainID) related text-module.
        The language code represents the language abbreviation defined in the field "UI language" in Admin ->Document templates ->Languages.
        The Main ID is depending on the defined usage area within
        TextmoduleIN.getTextModuleUsageArea(). e.g. if
        TextModuleUsageArea.ORDER is specified you have to provide an valid OrderID as MainID.


        :param textmodule_in: TextmoduleIN
        :param id: int
        :param language_code: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomFields30.setTextmodule
        response_model = Result

        if type(textmodule_in) != TextmoduleIN:
            textmodule_in = TextmoduleIN(**textmodule_in).dict()
        else:
            textmodule_in = textmodule_in.dict()

        arg = {"TextmoduleIN": textmodule_in, "ID": id, "languageCode": language_code}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_property_value(
        self,
        property_name_english: str,
        property_usage_area: Union[PropertyUsageArea, int],
        property_value_id: int,
        main_id: int,
    ) -> Result:
        """
        Deprecated.


        :param property_name_english: str
        :param property_usage_area: PropertyUsageArea
        :param property_value_id: int
        :param main_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCustomFields30.setPropertyValue
        response_model = Result

        if type(property_usage_area) == PropertyUsageArea:
            property_usage_area = property_usage_area.value
        elif type(property_usage_area) == int:
            property_usage_area = property_usage_area
        else:
            property_usage_area = int(property_usage_area)

        arg = {
            "PropertyNameEnglish": property_name_english,
            "PropertyUsageArea": property_usage_area,
            "PropertyValueID": property_value_id,
            "MainID": main_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )
