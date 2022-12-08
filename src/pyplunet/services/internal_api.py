from __future__ import annotations
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import PlunetClient
from ..enums import FolderType


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
