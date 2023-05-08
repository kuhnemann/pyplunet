from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CatType, CurrencyType, EventType, ProjectType
from ..models import (
    DateResult,
    IntegerResult,
    JobIN,
    JobListResult,
    JobMetricResult,
    JobResult,
    JobTrackingTimeIN,
    JobTrackingTimeListIN,
    JobTrackingTimeResult,
    PriceLineIN,
    PriceLineListResult,
    PriceLineResult,
    PricelistEntryList,
    PricelistListResult,
    PricelistResult,
    PriceUnitListResult,
    PriceUnitResult,
    Result,
    StringArrayResult,
    StringResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataJob30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def get_creation_date(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> DateResult:
        """
        Returns an instance of IntegerResult containing the creation date of the job


        :param project_type: ProjectType
        :param job_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataJob30.getCreationDate
        response_model = DateResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_item_id(
        self, project_type: Union[ProjectType, int], item_id: int, job_id: int
    ) -> Result:
        """
        Method to set the item id for the specified job.


        :param project_type: ProjectType
        :param item_id: int
        :param job_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setItemID
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update(
        self, job_in: Union[JobIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        Updates a job depending on the transfered job object.
        Use the parameter "enabled" to decide if Null or empty Strings are saved
        into Plunet or ignored.


        :param job_in: JobIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.update
        response_model = Result

        if type(job_in) != JobIN:
            job_in = JobIN(**job_in).dict()
        else:
            job_in = job_in.dict()

        arg = {"JobIN": job_in, "enableNullOrEmptyValues": enable_null_or_empty_values}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert(
        self,
        project_id: int,
        project_type: Union[ProjectType, int],
        job_type_abbrevation: str,
    ) -> IntegerResult:
        """
        Inserts a empty Job.
        Possible abbreviations for services can be obtained over DataAdmin30.getAvailableServices(String, String)


        :param project_id: int
        :param project_type: ProjectType
        :param job_type_abbrevation: str
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJob30.insert
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "projectID": project_id,
            "projectType": project_type,
            "jobTypeAbbrevation": job_type_abbrevation,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_comment(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> StringResult:
        """
        Method to get the work instruction comment of the job.


        :param project_type: ProjectType
        :param job_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getComment
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_comment(
        self, project_type: Union[ProjectType, int], job_id: int, comment: str
    ) -> Result:
        """
        Method to set the work instruction comment of the job.


        :param project_type: ProjectType
        :param job_id: int
        :param comment: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setComment
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id, "comment": comment}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_currency(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> StringResult:
        """
        Returns the currency of the job represented by its ISO value.


        :param job_id: int
        :param project_type: ProjectType
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getCurrency
        response_model = StringResult

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

    def set_resource_id(
        self, project_type: Union[ProjectType, int], resource_id: int, job_id: int
    ) -> Result:
        """
        Deprecated. This method is no longer supported. Please use the new Endpoint DataJobRound30 for resource assignment.
        For further information, please refer to the release notes.
        Method to set the resource id for the specified Job.


        :param project_type: ProjectType
        :param resource_id: int
        :param job_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setResourceID
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "resourceID": resource_id, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_description(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> StringResult:
        """
        Method to get the description of the job.


        :param project_type: ProjectType
        :param job_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getDescription
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_description(
        self, project_type: Union[ProjectType, int], job_id: int, description: str
    ) -> Result:
        """
        Method to set the description of the job.


        :param project_type: ProjectType
        :param job_id: int
        :param description: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setDescription
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id, "description": description}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def deregister_callback_observer(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> Result:
        """
        Deletes an observer.
        Observer can only deleted by the user who has created them.


        :param job_id: int
        :param project_type: ProjectType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.deregisterCallback_Observer
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"JobID": job_id, "ProjectType": project_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def register_callback_notify(
        self,
        server_authentication_string: str,
        server_address: str,
        event_type: Union[EventType, int],
    ) -> Result:
        """
        Register to get notified when the specified EventType occurs
        for any job.

        If the EventType occurs PBM will call the callback web service,
        which is hosted within your environment.


        Please check CallbackCustomer30 for the exact specification for
        this service.


        Info:Each user can only create one notifier per event


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackJob30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.registerCallback_Notify
        response_model = Result

        if type(event_type) == EventType:
            event_type = event_type.value
        elif type(event_type) == int:
            event_type = event_type
        else:
            event_type = int(event_type)

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "EventType": event_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def deregister_callback_notify(self, event_type: Union[EventType, int]) -> Result:
        """
        Deletes an registered notify request.
        Info:Notify requests can only be deleted by the user who has created them


        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.deregisterCallback_Notify
        response_model = Result

        if type(event_type) == EventType:
            event_type = event_type.value
        elif type(event_type) == int:
            event_type = event_type
        else:
            event_type = int(event_type)

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=event_type,
            response_model=response_model,
            unpack_dict=False,
        )

    def register_callback_observer(
        self,
        server_authentication_string: str,
        server_address: str,
        job_id: int,
        project_type: Union[ProjectType, int],
    ) -> Result:
        """
        Register to observe a specific object for any supported
        EventType.

        As soon as any supported EventType occurs, PBM will call the
        callback web service, which is hosted within your environment.


        Please check CallbackCustomer30 for the exact specification for
        this service.


        Info:Each user can only create one observer per id


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl

        In the first two cases, the address will be autocompleted by appending
        the corresponding directory "CallbackJob30?wsdl".

        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param job_id: int
        :param project_type: ProjectType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.registerCallback_Observer
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "JobID": job_id,
            "ProjectType": project_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_price_line_list(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> PriceLineListResult:
        """
        Returns a list of all job related PriceLine


        :param job_id: int
        :param project_type: ProjectType
        :return: PriceLineListResult
        """

        proxy = self.__client.plunet_server.DataJob30.getPriceLine_List
        response_model = PriceLineListResult

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

    def get_price_unit_list(
        self, language_code: str, service: str
    ) -> PriceUnitListResult:
        """
        Returns a list of priceUnit related to the specified service.
        Possible services can be obtained over DataAdmin30.getAvailableServices(String, String)


        :param language_code: str
        :param service: str
        :return: PriceUnitListResult
        """

        proxy = self.__client.plunet_server.DataJob30.getPriceUnit_List
        response_model = PriceUnitListResult

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelist_entry_list(
        self, pricelist_id: int, source_language: str, target_language: str
    ) -> PricelistEntryList:
        """
        Provides all price entries which are related to the Pricelist
        regarding the transfered source and target language.


        :param pricelist_id: int
        :param source_language: str
        :param target_language: str
        :return: PricelistEntryList
        """

        proxy = self.__client.plunet_server.DataJob30.getPricelistEntry_List
        response_model = PricelistEntryList

        arg = {
            "PricelistID": pricelist_id,
            "SourceLanguage": source_language,
            "TargetLanguage": target_language,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelist_list(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> PricelistListResult:
        """
        Returns all avaliable Pricelist for this job.
        Note: This is dependent on the related project and the selected customer


        :param job_id: int
        :param project_type: ProjectType
        :return: PricelistListResult
        """

        proxy = self.__client.plunet_server.DataJob30.getPricelist_List
        response_model = PricelistListResult

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

    def get_contact_person_id(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> IntegerResult:
        """
        Returns an instance of IntegerResult containing the resource ID
        of the jobs contact person.
        Refers to the field Job -> "Contact person for job" in the Plunet BM.


        :param project_type: ProjectType
        :param job_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJob30.getContactPersonID
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_job_type_long_name(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> StringResult:
        """
        Returns an instance of StringResult containing the full name (English)
        of the job type for the specified job. â e.g. Translation.


        :param project_type: ProjectType
        :param job_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getJobType_LongName
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def add_job_tracking_time(
        self,
        job_id: int,
        project_type: Union[ProjectType, int],
        job_tracking_time_in: Union[JobTrackingTimeIN, dict],
    ) -> Result:
        """
        Add a JobTrackingTimeIN to the specified job.
        Please note that the tracking time will not be added if one of the following conditions is violated:

        The overall completed percentage of a job must not exceed 100%.
        A Tracking time can only be added if the resource has access to the job.
        The current (API) user must own the proper rights to set the tracking times (see Admin -> Rights -> Resources -> [API user] -> Time sheet).


        :param job_id: int
        :param project_type: ProjectType
        :param job_tracking_time_in: JobTrackingTimeIN
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.addJobTrackingTime
        response_model = Result

        if type(job_tracking_time_in) != JobTrackingTimeIN:
            job_tracking_time_in = JobTrackingTimeIN(**job_tracking_time_in).dict()
        else:
            job_tracking_time_in = job_tracking_time_in.dict()

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "jobID": job_id,
            "projectType": project_type,
            "JobTrackingTimeIN": job_tracking_time_in,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_contact_person_id(
        self, project_type: Union[ProjectType, int], job_id: int, resource_id: int
    ) -> Result:
        """
        Method to set the resourceID of the contact-person for the specified job.
        Refers to the field Job -> "Contact person for job" in the Plunet BM.


        :param project_type: ProjectType
        :param job_id: int
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setContactPersonID
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_job_list_for_view(
        self, job_i_ds: str, project_type: Union[ProjectType, int]
    ) -> JobListResult:
        """
        Method returns an instance of JobListResult, containing a list of Job objects.
        This method only returns a set of information about a set of jobs, e.g. to
        display this information in your application.


        :param job_i_ds: str
        :param project_type: ProjectType
        :return: JobListResult
        """

        proxy = self.__client.plunet_server.DataJob30.getJobList_ForView
        response_model = JobListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"jobIDs": job_i_ds, "projectType": project_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_resource_contact_person_id(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> IntegerResult:
        """
        Returns an instance of IntegerResult containing the resource ID
        of the contact person.
        Refers to the field Job -> "Contact persons" in the Plunet BM.


        :param project_type: ProjectType
        :param job_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJob30.getResourceContactPersonID
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_item_independent_jobs(
        self, project_type: Union[ProjectType, int], project_id: int
    ) -> JobListResult:
        """
        Returns an instance of JobListResult, which contains a list of all language
        independent jobs .


        :param project_type: ProjectType
        :param project_id: int
        :return: JobListResult
        """

        proxy = self.__client.plunet_server.DataJob30.getItemIndependentJobs
        response_model = JobListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "projectId": project_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_job_tracking_times_list(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> JobTrackingTimeResult:
        """
        Returns a list of all job tracking times.


        :param job_id: int
        :param project_type: ProjectType
        :return: JobTrackingTimeResult
        """

        proxy = self.__client.plunet_server.DataJob30.getJobTrackingTimesList
        response_model = JobTrackingTimeResult

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

    def get_job_list_of_item_for_view(
        self, item_id: int, project_type: Union[ProjectType, int]
    ) -> JobListResult:
        """
        Method returns an instance of JobListResult, containing a list of Job objects.
        All available job for a specific itemID will be returned.
        This method only returns a set of information about a set of jobs, e.g.
        to display this information in your application.


        :param item_id: int
        :param project_type: ProjectType
        :return: JobListResult
        """

        proxy = self.__client.plunet_server.DataJob30.getJobListOfItem_ForView
        response_model = JobListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"itemID": item_id, "projectType": project_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_job_type_short_name(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> StringResult:
        """
        Returns an instance of StringResult containing the abbreviated name (English)
        of the job type for the specified job. â e.g. TRA.


        :param project_type: ProjectType
        :param job_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getJobType_ShortName
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_resource_contact_person_id(
        self, project_type: Union[ProjectType, int], job_id: int, contact_id: int
    ) -> Result:
        """
        Method to set the resourceID of the contact-person.

        Refers to the field Job -> "Contact persons" in the Plunet BM.


        :param project_type: ProjectType
        :param job_id: int
        :param contact_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setResourceContactPersonID
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id, "contactID": contact_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def add_job_tracking_times_list(
        self,
        job_id: int,
        project_type: Union[ProjectType, int],
        job_tracking_time_list_in: Union[JobTrackingTimeListIN, dict],
    ) -> Result:
        """
        Add a JobTrackingTimeListIN to the specified job.
        Please note that the tracking times will not be added if one of the following conditions is violated:

        The overall completed percentage of a job must not exceed 100%.
        A tracking time can only be added if the resource has access to the job.
        The current (API) user must own the proper rights to set the tracking times (see Admin -> Rights -> Resources -> [API user] -> Time sheet).


        If one of the conditions is violated for at least one tracking time, none of the tracking times will be added.


        :param job_id: int
        :param project_type: ProjectType
        :param job_tracking_time_list_in: JobTrackingTimeListIN
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.addJobTrackingTimesList
        response_model = Result

        if type(job_tracking_time_list_in) != JobTrackingTimeListIN:
            job_tracking_time_list_in = JobTrackingTimeListIN(
                **job_tracking_time_list_in
            ).dict()
        else:
            job_tracking_time_list_in = job_tracking_time_list_in.dict()

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "jobID": job_id,
            "projectType": project_type,
            "JobTrackingTimeListIN": job_tracking_time_list_in,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_price_line_list_by_currency_type(
        self,
        job_id: int,
        project_type: Union[ProjectType, int],
        currency_type: Union[CurrencyType, int],
    ) -> PriceLineListResult:
        """
        Returns a list of all job related PriceLine
        The PriceLine will be returned in the specified CurrencyType (default: project currency).


        :param job_id: int
        :param project_type: ProjectType
        :param currency_type: CurrencyType
        :return: PriceLineListResult
        """

        proxy = self.__client.plunet_server.DataJob30.getPriceLine_ListByCurrencyType
        response_model = PriceLineListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {
            "jobID": job_id,
            "projectType": project_type,
            "currencyType": currency_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_download_url_source_data(
        self, target_file_name: str, project_type: Union[ProjectType, int], job_id: int
    ) -> StringResult:
        """
        Returns an instance of StringResult containing an url
        This can be used for downloading the source files as zip archive from
        the specified job. The url is only available for the current api session.
        Info:
        For content based file up/download please use DataDocument30


        :param target_file_name: str
        :param project_type: ProjectType
        :param job_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getDownloadUrl_SourceData
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "targetFileName": target_file_name,
            "projectType": project_type,
            "jobID": job_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update_price_line(
        self,
        job_id: int,
        project_type: Union[ProjectType, int],
        price_line_in: Union[PriceLineIN, dict],
    ) -> PriceLineResult:
        """
        Updates a existing PriceLine.


        :param job_id: int
        :param project_type: ProjectType
        :param price_line_in: PriceLineIN
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataJob30.updatePriceLine
        response_model = PriceLineResult

        if type(price_line_in) != PriceLineIN:
            price_line_in = PriceLineIN(**price_line_in).dict()
        else:
            price_line_in = price_line_in.dict()

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "jobID": job_id,
            "projectType": project_type,
            "priceLineIN": price_line_in,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_action_link(
        self,
        project_type: Union[ProjectType, int],
        job_id: int,
        user_id: int,
        action_link_type: int,
    ) -> StringResult:
        """
        Method to obtain any kind of job related action link.


        :param project_type: ProjectType
        :param job_id: int
        :param user_id: int
        :param action_link_type: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getActionLink
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "projectType": project_type,
            "jobID": job_id,
            "userID": user_id,
            "actionLinkType": action_link_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelist(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> PricelistResult:
        """
        Returns the current selected Pricelist for the specified job


        :param job_id: int
        :param project_type: ProjectType
        :return: PricelistResult
        """

        proxy = self.__client.plunet_server.DataJob30.getPricelist
        response_model = PricelistResult

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

    def set_pricelist(
        self, job_id: int, project_type: Union[ProjectType, int], price_list_id: int
    ) -> Result:
        """
        SetÂ´s the selected Pricelist for the specified job


        :param job_id: int
        :param project_type: ProjectType
        :param price_list_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setPricelist
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "jobID": job_id,
            "projectType": project_type,
            "priceListID": price_list_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_services_list(self, language_code: str) -> StringArrayResult:
        """
        Deprecated. Please use DataAdmin30.getAvailableServices(String, String) instead.
        Returns a list of all avaliable services.


        :param language_code: str
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataJob30.getServices_List
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=language_code,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_price_unit(self, price_unit_id: int, language_code: str) -> PriceUnitResult:
        """
        Returns a PriceUnitResult object.
        Possible PriceUnitÂ´s can be obtained over DataItem30.getPriceUnit_List(java.lang.String, java.lang.String, java.lang.String)


        :param price_unit_id: int
        :param language_code: str
        :return: PriceUnitResult
        """

        proxy = self.__client.plunet_server.DataJob30.getPriceUnit
        response_model = PriceUnitResult

        arg = {"PriceUnitID": price_unit_id, "languageCode": language_code}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert_price_line(
        self,
        job_id: int,
        project_type: Union[ProjectType, int],
        price_line_in: Union[PriceLineIN, dict],
        create_as_first_item: bool,
    ) -> PriceLineResult:
        """
        Inserts a new PriceLine to the specified job
        Warning: Job-Price lines do not support the price-line memo value.
        This value will be ignored by this specific implementation.


        :param job_id: int
        :param project_type: ProjectType
        :param price_line_in: PriceLineIN
        :param create_as_first_item: bool
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataJob30.insertPriceLine
        response_model = PriceLineResult

        if type(price_line_in) != PriceLineIN:
            price_line_in = PriceLineIN(**price_line_in).dict()
        else:
            price_line_in = price_line_in.dict()

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "jobID": job_id,
            "projectType": project_type,
            "priceLineIN": price_line_in,
            "createAsFirstItem": create_as_first_item,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete_price_line(
        self, job_id: int, project_type: Union[ProjectType, int], price_line_id: int
    ) -> Result:
        """
        Deletes an existing PriceLine


        :param job_id: int
        :param project_type: ProjectType
        :param price_line_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.deletePriceLine
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "jobID": job_id,
            "projectType": project_type,
            "priceLineID": price_line_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_delivery_date(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> DateResult:
        """
        Returns an instance of DateResult representing the delivery
        date of the job using the default time zone.


        :param project_type: ProjectType
        :param job_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataJob30.getDeliveryDate
        response_model = DateResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_delivery_note(
        self, project_type: Union[ProjectType, int], job_id: int, note: str
    ) -> Result:
        """
        Method to set the delivery note for the specified job


        :param project_type: ProjectType
        :param job_id: int
        :param note: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setDeliveryNote
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id, "note": note}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_payable_id(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> IntegerResult:
        """
        Returns the referenced payable ID


        :param job_id: int
        :param project_type: ProjectType
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJob30.getPayableID
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

    def get_job_number(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> StringResult:
        """
        Returns the job number, e.g. '001' for the job 'TRA-001'


        :param project_type: ProjectType
        :param job_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getJobNumber
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def run_automatic_job(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> Result:
        """
        Start or restart an automatic job.

        Please note that a job can only be started in its initial job status (as
        defined in the admin settings). This does not apply for restarting jobs.


        :param job_id: int
        :param project_type: ProjectType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.runAutomaticJob
        response_model = Result

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

    def insert3(self, job_in: Union[JobIN, dict], job_type_short: str) -> IntegerResult:
        """
        Inserts a new Job.


        :param job_in: JobIN
        :param job_type_short: str
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJob30.insert3
        response_model = IntegerResult

        if type(job_in) != JobIN:
            job_in = JobIN(**job_in).dict()
        else:
            job_in = job_in.dict()

        arg = {"JobIN": job_in, "JobTypeShort": job_type_short}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete_job(self, job_id: int, project_type: Union[ProjectType, int]) -> Result:
        """
        Deletes a job.


        :param job_id: int
        :param project_type: ProjectType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.deleteJob
        response_model = Result

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

    def set_price_liste_id(
        self, project_type: Union[ProjectType, int], price_list_id: int, job_id: int
    ) -> Result:
        """
        Deprecated. This call is deprecated and may be removed in future api versions.
        Please use setPricelist(String, int, int, int) instead.


        :param project_type: ProjectType
        :param price_list_id: int
        :param job_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setPriceListeID
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "projectType": project_type,
            "priceListID": price_list_id,
            "jobID": job_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def assign_job(
        self, project_type: Union[ProjectType, int], job_id: int, resource_id: int
    ) -> Result:
        """
        Deprecated. This method is no longer supported. Please use the new Endpoint DataJobRound30 for resource assignment.
        For further information, please refer to the release notes.
        Assigns a job to a resource.


        :param project_type: ProjectType
        :param job_id: int
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.assignJob
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id, "resourceID": resource_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_start_date(
        self, project_type: Union[ProjectType, int], start_date: datetime, job_id: int
    ) -> Result:
        """
        Method to set the start-date for the specified job.


        :param project_type: ProjectType
        :param start_date: datetime
        :param job_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setStartDate
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "startDate": start_date, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_due_date(
        self, project_type: Union[ProjectType, int], due_date: datetime, job_id: int
    ) -> Result:
        """
        Method to set the due-date for the specified job.


        :param project_type: ProjectType
        :param due_date: datetime
        :param job_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setDueDate
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "dueDate": due_date, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_job_for_view(
        self, job_id: int, project_type: Union[ProjectType, int]
    ) -> JobResult:
        """
        This method returns a single instance of job.
        This method only returns a set of information about a job, e.g. to display
        this information in your application.


        :param job_id: int
        :param project_type: ProjectType
        :return: JobResult
        """

        proxy = self.__client.plunet_server.DataJob30.getJob_ForView
        response_model = JobResult

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

    def set_job_status(
        self, project_type: Union[ProjectType, int], job_id: int, status: int
    ) -> Result:
        """
        Method to set the status for the specified job.


        :param project_type: ProjectType
        :param job_id: int
        :param status: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setJobStatus
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id, "status": status}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_delivery_note(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> StringResult:
        """
        Method to access the delivery note for the specified job


        :param project_type: ProjectType
        :param job_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataJob30.getDeliveryNote
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_due_date(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> DateResult:
        """
        Returns an instance of DateResult representing the due date of the job.


        :param project_type: ProjectType
        :param job_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataJob30.getDueDate
        response_model = DateResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_job_metrics(
        self, job_id: int, project_type: Union[ProjectType, int], language_code: str
    ) -> JobMetricResult:
        """
        Retrieves the job's total price and amounts.


        :param job_id: int
        :param project_type: ProjectType
        :param language_code: str
        :return: JobMetricResult
        """

        proxy = self.__client.plunet_server.DataJob30.getJobMetrics
        response_model = JobMetricResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "jobID": job_id,
            "projectType": project_type,
            "languageCode": language_code,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert2(
        self,
        project_id: int,
        project_type: Union[ProjectType, int],
        job_type_abbrevation: str,
        item_id: int,
    ) -> IntegerResult:
        """
        Inserts a Job.


        :param project_id: int
        :param project_type: ProjectType
        :param job_type_abbrevation: str
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJob30.insert2
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "projectID": project_id,
            "projectType": project_type,
            "jobTypeAbbrevation": job_type_abbrevation,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_resource_id(
        self, project_type: Union[ProjectType, int], job_id: int
    ) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the resource id
        of the specified job.


        :param project_type: ProjectType
        :param job_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataJob30.getResourceID
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "jobID": job_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_cat_report2(
        self,
        file_byte_stream: bytes,
        file_path_name: str,
        filesize: int,
        cat_type: Union[CatType, int],
        project_type: Union[ProjectType, int],
        analyze_and_copy_result_to_job: bool,
        job_id: int,
    ) -> Result:
        """
        Uploads a report file into the report folder of the specified job.
        Specify by value to copy the results of the report into the job and
        if they should overwrite already existing price lines.


        :param file_byte_stream: bytes
        :param file_path_name: str
        :param filesize: int
        :param cat_type: CatType
        :param project_type: ProjectType
        :param analyze_and_copy_result_to_job: bool
        :param job_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setCatReport2
        response_model = Result

        if type(cat_type) == CatType:
            cat_type = cat_type.value
        elif type(cat_type) == int:
            cat_type = cat_type
        else:
            cat_type = int(cat_type)

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "FileByteStream": file_byte_stream,
            "FilePathName": file_path_name,
            "Filesize": filesize,
            "catType": cat_type,
            "projectType": project_type,
            "analyzeAndCopyResultToJob": analyze_and_copy_result_to_job,
            "jobID": job_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_cat_report(
        self,
        path_or_url: str,
        overwrite_existing_price_lines: bool,
        cat_type: Union[CatType, int],
        project_type: Union[ProjectType, int],
        analyze_and_copy_result_to_job: bool,
        job_id: int,
    ) -> Result:
        """
        Deprecated. Please use setCatReport2(String, byte[], String, int, int, int, boolean, int) instead.
        Please note that this call is now deactivated by default. For Reactivation please contact Support@plunet.com.

        Uploads a report file into the report folder of the specified job.
        Specify by value to copy the results of the report into the job and
        if they should overwrite already existing price lines.


        :param path_or_url: str
        :param overwrite_existing_price_lines: bool
        :param cat_type: CatType
        :param project_type: ProjectType
        :param analyze_and_copy_result_to_job: bool
        :param job_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataJob30.setCatReport
        response_model = Result

        if type(cat_type) == CatType:
            cat_type = cat_type.value
        elif type(cat_type) == int:
            cat_type = cat_type
        else:
            cat_type = int(cat_type)

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "pathOrUrl": path_or_url,
            "overwriteExistingPriceLines": overwrite_existing_price_lines,
            "catType": cat_type,
            "projectType": project_type,
            "analyzeAndCopyResultToJob": analyze_and_copy_result_to_job,
            "jobID": job_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )
