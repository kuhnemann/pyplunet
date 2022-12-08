from __future__ import annotations
from typing import List, Union

from ..models import SearchFilter_Job

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import PlunetClient

from ..enums import CatType, ProjectType


class DataJob30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_jobtype_shortname(
        self, job_id: int, project_type: ProjectType = ProjectType.ORDER
    ):
        arg = {"jobID": job_id, "projectType": project_type.value}
        return self.__client.make_request(
            self.__client.plunet_server.DataJob30.getJobType_ShortName,
            arg,
            unpack_dict=True,
        )

    def get_job_list_of_item_for_view(
        self, item_id: int, project_type: ProjectType = ProjectType.ORDER
    ):
        arg = {"projectType": project_type.value, "itemID": item_id}
        return self.__client.make_request(
            self.__client.plunet_server.DataJob30.getJobListOfItem_ForView,
            arg,
            unpack_dict=True,
        )

    def set_cat_report_to_job(
        self,
        job_id: int,
        byte_stream: bytes,
        file_name: str,
        file_size: int,
        analyze_copy: bool,
        cat_type: CatType = CatType.MEMSOURCE,
        project_type: ProjectType = ProjectType.ORDER,
    ):

        arg = {
            "FileByteStream": byte_stream,
            "FilePathName": file_name,
            "Filesize": file_size,
            "catType": cat_type.value,
            "analyzeAndCopyResultToJob": analyze_copy,
            "projectType": project_type.value,
            "jobID": job_id,
        }

        return self.__client.make_request(
            self.__client.plunet_server.DataJob30.setCatReport2, arg, unpack_dict=True
        )


class ReportJob30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def search_for_jobs(
        self, search_filter: Union[SearchFilter_Job, dict]
    ) -> List[int]:
        if type(search_filter) != SearchFilter_Job:
            arg = SearchFilter_Job(**search_filter).dict()
        else:
            arg = search_filter.dict()

        return self.__client.make_request(
            self.__client.plunet_server.ReportJob30.search, arg
        )
