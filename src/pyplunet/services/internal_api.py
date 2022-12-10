from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional, Union

from pydantic import BaseModel

if TYPE_CHECKING:
    from ..client import PlunetClient

from ..enums import FolderType, TextModuleType


class TextmoduleIN(BaseModel):
    dateValue: Optional[datetime]
    flag: Optional[str]
    selectedValues: Optional[List[str]]
    stringValue: Optional[str]
    textModuleUsageArea: TextModuleType

    class Config:
        use_enum_values = True


class DataCustomFields30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_property(
        self, PropertyNameEnglish: str, PropertyUsageArea: int, MainID: int
    ):
        """Returns a PropertyResult depending on the usage area and object related ID."""
        arg = {
            "PropertyNameEnglish": PropertyNameEnglish,
            "PropertyUsageArea": PropertyUsageArea,
            "MainID": MainID,
        }
        proxy = self.__client.plunet_server.DataCustomFields30.getProperty

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_property_value_text(
        self, PropertyNameEnglish: str, PropertyValueID: int, languageCode: str
    ):
        """Returns the value text dependent on the language-code and propertyValueID."""
        arg = {
            "PropertyNameEnglish": PropertyNameEnglish,
            "PropertyValueID": PropertyValueID,
            "languageCode": languageCode,
        }
        proxy = self.__client.plunet_server.DataCustomFields30.getPropertyValueText

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_textmodule(
        self, Flag: str, TextModuleUsageArea: int, MainID: int, languageCode: str
    ):
        """Returns a text-module depending on the flag and transfered parameters."""

        arg = {
            "Flag": Flag,
            "TextModuleUsageArea": TextModuleUsageArea,
            "MainID": MainID,
            "languageCode": languageCode,
        }
        proxy = self.__client.plunet_server.DataCustomFields30.getTextmodule

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def setPropertyValueList(
        self,
        PropertyNameEnglish: str,
        PropertyUsageArea: int,
        PropertyValueList: List[int],
        MainID: int,
    ):
        """
        Changes the current selected property value for the specific object (mainID) to the
        specified property value ID.
        """
        arg = {
            "PropertyNameEnglish": PropertyNameEnglish,
            "PropertyUsageArea": PropertyUsageArea,
            "PropertyValueList": PropertyValueList,
            "MainID": MainID,
        }
        proxy = self.__client.plunet_server.DataCustomFields30.setPropertyValueList

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_textmodule(
        self, textmodule_in: TextmoduleIN, main_id: int, language_code: str
    ):
        """Allows to change the selected value/s of the object (MainID) related text-module."""

        arg = {
            "TextmoduleIN": textmodule_in.dict(),
            "MainID": main_id,
            "LanguageCode": language_code,
        }
        proxy = self.__client.plunet_server.DataCustomFields30.setTextmodule

        return self.__client.make_request(proxy, arg, unpack_dict=True)


class DataUser30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_user_by_id(self, user_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataUser30.getUserByID, user_id
        )

    def get_user_by_login_name(self, login_name: str):
        return self.__client.make_request(
            self.__client.plunet_server.DataUser30.getUserByLoginName, login_name
        )

    def get_user_list_by_resource_id(self, resource_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataUser30.getUserListByResourceID, resource_id
        )


class DataDocument30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_file_list(self, main_id: int, folder_type: Union[FolderType, int]):
        """

        :param main_id: Int id for entity type: OrderID, JobID, RequestID, etc.
        :param folder_type:
        :return:
        """
        if type(folder_type) == int:
            arg = {"MainID": main_id, "FolderType": folder_type}
        else:
            arg = {"MainID": main_id, "FolderType": folder_type.value}
        return self.__client.make_request(
            self.__client.plunet_server.DataDocument30.getFileList,
            arg,
            unpack_dict=True,
        )

    def download_document(
        self, main_id: int, folder_type: Union[FolderType, int], file_path_name: str
    ):
        """

        :param main_id: Int id for entity type: OrderID, JobID, RequestID, etc.
        :param folder_type:
        :param file_path_name:
        :return:
        """
        arg = {"MainID": main_id, "FilePathName": file_path_name}
        if type(folder_type) == int:
            arg["FolderType"] = folder_type
        else:
            arg["FolderType"] = folder_type.value
        return self.__client.make_download(
            self.__client.plunet_server.DataDocument30.download_Document,
            arg,
            unpack_dict=True,
        )

    def upload_document(
        self,
        main_id: int,
        folder_type: Union[FolderType, int],
        file_path_name: str,
        file_size: int,
        byte_stream: bytes,
    ):

        arg = {
            "FileByteStream": byte_stream,
            "FilePathName": file_path_name,
            "FileSize": file_size,
            "MainID": main_id,
        }

        if type(folder_type) == int:
            arg["FolderType"] = folder_type
        else:
            arg["FolderType"] = folder_type.value

        return self.__client.make_request(
            self.__client.plunet_server.DataDocument30.upload_Document,
            arg,
            unpack_dict=True,
        )
