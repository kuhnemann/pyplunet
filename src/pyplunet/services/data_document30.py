from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import FolderTypes
from ..models import FileResult, Result, StringArrayResult

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataDocument30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def download_document(
        self, main_id: int, folder_type: Union[FolderTypes, int], file_path_name: str
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

        if type(folder_type) == FolderTypes:
            folder_type = folder_type.value
        elif type(folder_type) == int:
            folder_type = folder_type
        else:
            folder_type = int(folder_type)

        arg = {
            "MainID": main_id,
            "FolderType": folder_type,
            "FilePathName": file_path_name,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def upload_document(
        self,
        main_id: int,
        folder_type: Union[FolderTypes, int],
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


        To upload file into a subfolder "test" within the source folder of the order (id=500)


        MainID = 500
        FolderType = 6
        FilePathName = "test\my_file.txt"


        :param main_id: int
        :param folder_type: FolderTypes
        :param file_byte_stream: bytes
        :param file_path_name: str
        :param file_size: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataDocument30.upload_Document
        response_model = Result

        if type(folder_type) == FolderTypes:
            folder_type = folder_type.value
        elif type(folder_type) == int:
            folder_type = folder_type
        else:
            folder_type = int(folder_type)

        arg = {
            "MainID": main_id,
            "FolderType": folder_type,
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
        self, main_id: int, folder_type: Union[FolderTypes, int]
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

        if type(folder_type) == FolderTypes:
            folder_type = folder_type.value
        elif type(folder_type) == int:
            folder_type = folder_type
        else:
            folder_type = int(folder_type)

        arg = {"MainID": main_id, "FolderType": folder_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )
