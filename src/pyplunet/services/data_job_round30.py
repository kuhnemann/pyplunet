from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import ProjectType
from ..models import (
    IntegerArrayResult,
    IntegerResult,
    JobRoundIN,
    JobRoundRankingMethodList,
    JobRoundRankingMethodListResult,
    JobRoundResult,
    JobRoundSearchCriteriaIN,
    JobRoundSearchcriteriaResult,
    Result,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataJobRound30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def delete(self, round_id: int) -> Result:
        """
        Deletes a round.

        Note: You cannot remove all rounds from a job! One round always has to exist.


        :param round_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJobRound30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=round_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_ranking_methods(self, round_id: int) -> JobRoundRankingMethodListResult:
        """
        Returns the ranking methods set for a round.


        :param round_id: int
        :return: JobRoundRankingMethodListResult
        """

        proxy = self.__client.plunet_server.DataJobRound30.getRankingMethods
        response_model = JobRoundRankingMethodListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=round_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_resources_for_round(self, round_id: int) -> IntegerArrayResult:
        """
        Returns the IDs of all resources matching the round criteria.


        :param round_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataJobRound30.getResourcesForRound
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=round_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_resource_for_review(
        self, resource_id: int, resource_contact_id: int, round_id: int
    ) -> Result:
        """
        Sets the resource of a job.

        The resource is not confirmed yet, but awaits confirmation.


        :param resource_id: int
        :param resource_contact_id: int
        :param round_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJobRound30.setResourceForReview
        response_model = Result

        arg = {
            "resourceID": resource_id,
            "resourceContactID": resource_contact_id,
            "roundID": round_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def assign_resource_in_review(self, round_id: int) -> Result:
        """
        Assigns the job to a preselected resource.

        The resource in review is assigned to the job.


        :param round_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJobRound30.assignResource_InReview
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=round_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_search_criteria(self, round_id: int) -> JobRoundSearchcriteriaResult:
        """
        Returns the search criteria of a round.


        :param round_id: int
        :return: JobRoundSearchcriteriaResult
        """

        proxy = self.__client.plunet_server.DataJobRound30.getSearchCriteria
        response_model = JobRoundSearchcriteriaResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=round_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_search_criteria(
        self,
        job_round_search_criteria_in: Union[JobRoundSearchCriteriaIN, dict],
        round_id: int,
    ) -> Result:
        """
        Sets the search criteria of a round.


        :param job_round_search_criteria_in: JobRoundSearchCriteriaIN
        :param round_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJobRound30.setSearchCriteria
        response_model = Result

        if type(job_round_search_criteria_in) != JobRoundSearchCriteriaIN:
            job_round_search_criteria_in = JobRoundSearchCriteriaIN(
                **job_round_search_criteria_in
            ).dict()
        else:
            job_round_search_criteria_in = job_round_search_criteria_in.dict()

        arg = {
            "JobRoundSearchCriteriaIN": job_round_search_criteria_in,
            "roundID": round_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_ranking_methods(
        self,
        job_round_ranking_method_list: Union[JobRoundRankingMethodList, dict],
        round_id: int,
    ) -> Result:
        """
        Sets the rankings methods of a round.

        If no value is selected, the ranking will be performed by resourceId.


        :param job_round_ranking_method_list: JobRoundRankingMethodList
        :param round_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJobRound30.setRankingMethods
        response_model = Result

        if type(job_round_ranking_method_list) != JobRoundRankingMethodList:
            job_round_ranking_method_list = JobRoundRankingMethodList(
                **job_round_ranking_method_list
            ).dict()
        else:
            job_round_ranking_method_list = job_round_ranking_method_list.dict()

        arg = {
            "JobRoundRankingMethodList": job_round_ranking_method_list,
            "roundID": round_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_assigned_round_id(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> IntegerResult:
        """
        Returns the roundId of the assigned round of the job.


        :param job_id: int
        :param project_type: ProjectType
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJobRound30.getAssignedRoundID
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"jobID": job_id, "projectType": project_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_round_object(self, round_id: int) -> JobRoundResult:
        """
        Returns a job round object.


        :param round_id: int
        :return: JobRoundResult
        """

        proxy = self.__client.plunet_server.DataJobRound30.getRoundObject
        response_model = JobRoundResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=round_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def assign_resource(
        self, resource_id: int, resource_contact_id: int, round_id: int
    ) -> Result:
        """
        Assigns the job to a resource.

        The resource is assigned to the job. If a valid resourceContactId is submitted, the contact
        person will be set instead. Please ensure the contactPersonId corresponds to the resourceId
        submitted.


        :param resource_id: int
        :param resource_contact_id: int
        :param round_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJobRound30.assignResource
        response_model = Result

        arg = {
            "resourceID": resource_id,
            "resourceContactID": resource_contact_id,
            "roundID": round_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update_round(self, round_in: Union[JobRoundIN, dict]) -> Result:
        """
        Updates a round.


        :param round_in: JobRoundIN
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJobRound30.updateRound
        response_model = Result

        if type(round_in) != JobRoundIN:
            round_in = JobRoundIN(**round_in).dict()
        else:
            round_in = round_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=round_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def add_round(
        self,
        job_id: int,
        project_type: Union[ProjectType, int],
        job_round_in: Union[JobRoundIN, dict],
    ) -> IntegerResult:
        """
        Adds a new round to the job.

        Note: Inserting a job will already create a round for this job. You can only add additional
        rounds if you either have the Vendor Search Manager PRO module enabled or no more active rounds
        in the job.


        :param job_id: int
        :param project_type: ProjectType
        :param job_round_in: JobRoundIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJobRound30.addRound
        response_model = IntegerResult

        if type(job_round_in) != JobRoundIN:
            job_round_in = JobRoundIN(**job_round_in).dict()
        else:
            job_round_in = job_round_in.dict()

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"jobID": job_id, "projectType": project_type, "jobRoundIN": job_round_in}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_round_i_ds(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> IntegerArrayResult:
        """
        Returns all roundIDs corresponding to the job.


        :param job_id: int
        :param project_type: ProjectType
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataJobRound30.getAllRoundIDs
        response_model = IntegerArrayResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"jobID": job_id, "projectType": project_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )
