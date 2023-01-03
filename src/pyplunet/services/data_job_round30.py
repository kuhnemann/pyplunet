from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import ProjectType
from ..models import JobRoundIN, JobRoundRankingMethodList, JobRoundSearchCriteriaIN

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataJobRound30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def add_round(
        self,
        job_id: int,
        project_type: ProjectType,
        job_round_in: Union[JobRoundIN, dict],
    ):
        """
        Adds a new round to the job.

        :param job_id: int
        :param project_type: ProjectType
        :param job_round_in: JobRoundIN

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.addRound

        if type(job_round_in) != JobRoundIN:
            job_round_in = JobRoundIN(**job_round_in).dict()
        else:
            job_round_in = job_round_in.dict()

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "jobRoundIN": job_round_in,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def assign_resource_in_review(self, round_id: int):
        """
        Assigns the job to a preselected resource.

        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.assignResource_InReview

        return self.__client.make_request(proxy, round_id, unpack_dict=False)

    def assign_resource(
        self, resource_id: int, resource_contact_id: int, round_id: int
    ):
        """
        Assigns the job to a resource.

        :param resource_id: int
        :param resource_contact_id: int
        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.assignResource

        arg = {
            "resourceId": resource_id,
            "resourceContactId": resource_contact_id,
            "roundId": round_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete(self, round_id: int):
        """
        Deletes a round.

        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.delete

        return self.__client.make_request(proxy, round_id, unpack_dict=False)

    def get_all_round_i_ds(self, job_id: int, project_type: ProjectType):
        """
        Returns all roundIDs corresponding to the job.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.getAllRoundIDs

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_assigned_round_id(self, job_id: int, project_type: ProjectType):
        """
        Returns the roundId of the assigned round of the job.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.getAssignedRoundID

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_ranking_methods(self, round_id: int):
        """
        Returns the ranking methods set for a round.

        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.getRankingMethods

        return self.__client.make_request(proxy, round_id, unpack_dict=False)

    def get_resources_for_round(self, round_id: int):
        """
        Returns the IDs of all resources matching the round criteria.

        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.getResourcesForRound

        return self.__client.make_request(proxy, round_id, unpack_dict=False)

    def get_round_object(self, round_id: int):
        """
        Returns a job round object.

        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.getRoundObject

        return self.__client.make_request(proxy, round_id, unpack_dict=False)

    def get_search_criteria(self, round_id: int):
        """
        Returns the search criteria of a round.

        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.getSearchCriteria

        return self.__client.make_request(proxy, round_id, unpack_dict=False)

    def set_ranking_methods(
        self, method_list: Union[JobRoundRankingMethodList, dict], round_id: int
    ):
        """
        Sets the rankings methods of a round.

        :param method_list: JobRoundRankingMethodList
        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.setRankingMethods

        if type(method_list) != JobRoundRankingMethodList:
            method_list = JobRoundRankingMethodList(**method_list).dict()
        else:
            method_list = method_list.dict()

        arg = {"methodList": method_list, "roundId": round_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_resource_for_review(
        self, resource_id: int, resource_contact_id: int, round_id: int
    ):
        """
        Sets the resource of a job.

        :param resource_id: int
        :param resource_contact_id: int
        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.setResourceForReview

        arg = {
            "resourceId": resource_id,
            "resourceContactId": resource_contact_id,
            "roundId": round_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_search_criteria(
        self, search_criteria: Union[JobRoundSearchCriteriaIN, dict], round_id: int
    ):
        """
        Sets the search criteria of a round.

        :param search_criteria: JobRoundSearchCriteriaIN
        :param round_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.setSearchCriteria

        if type(search_criteria) != JobRoundSearchCriteriaIN:
            search_criteria = JobRoundSearchCriteriaIN(**search_criteria).dict()
        else:
            search_criteria = search_criteria.dict()

        arg = {"searchCriteria": search_criteria, "roundId": round_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_round(self, round_in: Union[JobRoundIN, dict]):
        """
        Updates a round.

        :param round_in: JobRoundIN

        :return:
        """

        proxy = self.__client.plunet_server.DataJobRound30.updateRound

        if type(round_in) != JobRoundIN:
            round_in = JobRoundIN(**round_in).dict()
        else:
            round_in = round_in.dict()

        return self.__client.make_request(proxy, round_in, unpack_dict=False)
