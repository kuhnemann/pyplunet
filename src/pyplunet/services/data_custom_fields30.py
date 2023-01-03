from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import IntegerList, TextmoduleIN

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataCustomFields30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_property(
        self, property_name_english: str, property_usage_area: int, main_id: int
    ):
        """
        Returns a PropertyResult  depending on the usage area and object related ID.

        :param property_name_english: str
        :param property_usage_area: int
        :param main_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomFields30.getProperty

        arg = {
            "PropertyNameEnglish": property_name_english,
            "PropertyUsageArea": property_usage_area,
            "MainID": main_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_property_value_text(
        self, property_name_english: str, property_value_id: int, language_code: str
    ):
        """
        Returns the value text dependent on the language-code and propertyValueID.

        :param property_name_english: str
        :param property_value_id: int
        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomFields30.getPropertyValueText

        arg = {
            "PropertyNameEnglish": property_name_english,
            "PropertyValueID": property_value_id,
            "languageCode": language_code,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_textmodule(
        self, flag: str, text_module_usage_area: int, main_id: int, language_code: str
    ):
        """
        Returns a text-module depending on the flag and transfered parameters.

        :param flag: str
        :param text_module_usage_area: int
        :param main_id: int
        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomFields30.getTextmodule

        arg = {
            "Flag": flag,
            "TextModuleUsageArea": text_module_usage_area,
            "ID": main_id,
            "languageCode": language_code,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_property_value(
        self,
        property_name_english: str,
        property_usage_area: int,
        property_value_id: int,
        main_id: int,
    ):
        """
        Deprecated.

        :param property_name_english: str
        :param property_usage_area: int
        :param property_value_id: int
        :param main_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomFields30.setPropertyValue

        arg = {
            "PropertyNameEnglish": property_name_english,
            "PropertyUsageArea": property_usage_area,
            "PropertyValueID": property_value_id,
            "MainID": main_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_property_value_list(
        self,
        property_name_english: str,
        property_usage_area: int,
        property_value_list: Union[IntegerList, dict],
        main_id: int,
    ):
        """
        Changes the current selected property value for the specific object(mainID) to the specified property value ID.

        :param property_name_english: str
        :param property_usage_area: int
        :param property_value_list: IntegerList
        :param main_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomFields30.setPropertyValueList

        if type(property_value_list) != IntegerList:
            property_value_list = IntegerList(**property_value_list).dict()
        else:
            property_value_list = property_value_list.dict()

        arg = {
            "PropertyNameEnglish": property_name_english,
            "PropertyUsageArea": property_usage_area,
            "PropertyValueList": property_value_list,
            "MainID": main_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_textmodule(
        self, textmodule_in: Union[TextmoduleIN, dict], main_id: int, language_code: str
    ):
        """
        Allows to change the selected value/s of the object (MainID) related text-module.

        :param textmodule_in: TextmoduleIN
        :param main_id: int
        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCustomFields30.setTextmodule

        if type(textmodule_in) != TextmoduleIN:
            textmodule_in = TextmoduleIN(**textmodule_in).dict()
        else:
            textmodule_in = textmodule_in.dict()

        arg = {
            "TextmoduleIN": textmodule_in,
            "ID": main_id,
            "languageCode": language_code,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
