from __future__ import annotations
from tests import get_test_client
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        StringArrayResult,
        FileResult,
        Result
)


from src.pyplunet.enums import (
        FolderTypes
)


class test_set_DataDocument30(BaseModel):
    main_id: int
    folder_type: FolderTypes
    file_byte_stream: bytes
    file_path_name: str
    file_size: int

def get_test_set() -> test_set_DataDocument30:
    return test_set_DataDocument30(
            main_id= ,
            folder_type= ,
            file_byte_stream= ,
            file_path_name= ,
            file_size= 
    )


def test_DataDocument30_upload_document(pc: PlunetClient, test_set: test_set_DataDocument30):
    try:
        resp = pc.document.upload_document(
                main_id=test_set.main_id,
                folder_type=test_set.folder_type,
                file_byte_stream=test_set.file_byte_stream,
                file_path_name=test_set.file_path_name,
                file_size=test_set.file_size
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataDocument30_upload_document failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataDocument30_upload_document was successful.")




def test_DataDocument30_get_file_list(pc: PlunetClient, test_set: test_set_DataDocument30):
    try:
        resp = pc.document.get_file_list(
                main_id=test_set.main_id,
                folder_type=test_set.folder_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataDocument30_get_file_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataDocument30_get_file_list was successful.")




def test_DataDocument30_download_document(pc: PlunetClient, test_set: test_set_DataDocument30):
    try:
        resp = pc.document.download_document(
                main_id=test_set.main_id,
                folder_type=test_set.folder_type,
                file_path_name=test_set.file_path_name
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataDocument30_download_document failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == FileResult
    print(f"test_DataDocument30_download_document was successful.")



if __name__ == '__main__':
    pc = get_test_client()
    test_set = get_test_set()
    test_DataDocument30_upload_document(pc, test_set)
    test_DataDocument30_get_file_list(pc, test_set)
    test_DataDocument30_download_document(pc, test_set)