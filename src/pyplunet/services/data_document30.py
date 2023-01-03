from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import FolderTypes

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataDocument30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def download_document(
        self, main_id: int, folder_type: FolderTypes, file_path_name: str
    ):
        """
        Returns a FileResult containing the specified file as byte-stream.

        :param main_id: int
        :param folder_type: FolderTypes
        :param file_path_name: str

        :return:
        """

        proxy = self.__client.plunet_server.DataDocument30.download_Document

        arg = {
            "MainID": main_id,
            "FolderType": folder_type.value,
            "FilePathName": file_path_name,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_file_list(self, main_id: int, folder_type: FolderTypes):
        """
        Returns a StringArrayResult containing all files with all sub folders after the,on the main and folder-type depending directory.

        :param main_id: int
        :param folder_type: FolderTypes

        :return:
        """

        proxy = self.__client.plunet_server.DataDocument30.getFileList

        arg = {"MainID": main_id, "FolderType": folder_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def upload_document(
        self,
        main_id: int,
        folder_type: FolderTypes,
        file_byte_stream: bytes,
        file_path_name: str,
        file_size: int,
    ):
        """
        Uploads a file to a specific directory.

        :param main_id: int
        :param folder_type: FolderTypes
        :param file_byte_stream: bytes
        :param file_path_name: str
        :param file_size: int

        :return:
        """

        proxy = self.__client.plunet_server.DataDocument30.upload_Document

        arg = {
            "MainID": main_id,
            "FolderType": folder_type.value,
            "FileByteStream": file_byte_stream,
            "FilePathName": file_path_name,
            "FileSize": file_size,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
