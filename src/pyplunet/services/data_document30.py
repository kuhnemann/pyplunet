from __future__ import annotations

from typing import TYPE_CHECKING

from ..enums import FolderTypes
from ..models import FileResult, Result, StringArrayResult

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataDocument30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def upload_document(
        self,
        main_id: int,
        folder_type: FolderTypes,
        file_byte_stream: bytes,
        file_path_name: str,
        file_size: int,
    ) -> Result:
        """
        Uploads a file to a specific directory.

        The file should to be read as (big-endian).


        The upload is verified by ensuring the supplied file size matches the size of the uploaded
        file. It is possible to provide 0 as filesize to exclude the size check.


        Example:


        To upload file into a subfolder &#34;test&#34; within the source folder of the order (id=500)


        MainID = 500
        FolderType = 6
        FilePathName = &#34;test\my_file.txt&#34;


        :param main_id: int
        :param folder_type: FolderTypes
        :param file_byte_stream: bytes
        :param file_path_name: str
        :param file_size: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataDocument30.upload_Document
        response_model = Result

        arg = {
            "MainID": main_id,
            "FolderType": folder_type.value,
            "FileByteStream": file_byte_stream,
            "FilePathName": file_path_name,
            "FileSize": file_size,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_file_list(
        self, main_id: int, folder_type: FolderTypes
    ) -> StringArrayResult:
        """
        Returns a StringArrayResult containing all files with all sub folders after the,
        on the main and folder-type depending directory.

        Example: MainID = 500 (OrderID) and FolderTypes.ORDER_REFERENCE


        Returns:


        de-de/examplefile_1.txt
        de-de/examplefile_2.txt
        testfiles5.csv
        en/testfiles6.pdf


        :param main_id: int
        :param folder_type: FolderTypes
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataDocument30.getFileList
        response_model = StringArrayResult

        arg = {"MainID": main_id, "FolderType": folder_type.value}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def download_document(
        self, main_id: int, folder_type: FolderTypes, file_path_name: str
    ) -> FileResult:
        """
        Returns a FileResult containing the specified file as byte-stream.

        The FilePathName can be obtained over getFileList(String, int, int)


        :param main_id: int
        :param folder_type: FolderTypes
        :param file_path_name: str
        :return: FileResult
        """

        proxy = self.__client.plunet_server.DataDocument30.download_Document
        response_model = FileResult

        arg = {
            "MainID": main_id,
            "FolderType": folder_type.value,
            "FilePathName": file_path_name,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )
