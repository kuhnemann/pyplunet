from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CatType, CurrencyType, EventType, JobActionLink, ProjectType
from ..models import JobIN, JobTrackingTimeIN, JobTrackingTimeListIN, PriceLineIN

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataJob30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def add_job_tracking_time(
        self,
        job_id: int,
        project_type: ProjectType,
        tracking_time: Union[JobTrackingTimeIN, dict],
    ):
        """
        Add a JobTrackingTimeIN to the specified job.

        :param job_id: int
        :param project_type: ProjectType
        :param tracking_time: JobTrackingTimeIN

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.addJobTrackingTime

        if type(tracking_time) != JobTrackingTimeIN:
            tracking_time = JobTrackingTimeIN(**tracking_time).dict()
        else:
            tracking_time = tracking_time.dict()

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "trackingTime": tracking_time,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def add_job_tracking_times_list(
        self,
        job_id: int,
        project_type: ProjectType,
        tracking_time_list: Union[JobTrackingTimeListIN, dict],
    ):
        """
        Add a JobTrackingTimeListIN to the specified job.

        :param job_id: int
        :param project_type: ProjectType
        :param tracking_time_list: JobTrackingTimeListIN

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.addJobTrackingTimesList

        if type(tracking_time_list) != JobTrackingTimeListIN:
            tracking_time_list = JobTrackingTimeListIN(**tracking_time_list).dict()
        else:
            tracking_time_list = tracking_time_list.dict()

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "trackingTimeList": tracking_time_list,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def assign_job(self, project_type: ProjectType, job_id: int, resource_id: int):
        """
        Deprecated.This method is no longer supported. Please use the new Endpoint DataJobRound30 for resource assignment.For further information, please refer to the release notes.Assigns a job to a resource.

        :param project_type: ProjectType
        :param job_id: int
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.assignJob

        arg = {
            "projectType": project_type.value,
            "jobID": job_id,
            "resourceID": resource_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete_job(self, job_id: int, project_type: ProjectType):
        """
        Deletes a job.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.deleteJob

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete_price_line(
        self, job_id: int, project_type: ProjectType, price_line: int
    ):
        """
        Deletes an existing PriceLine

        :param job_id: int
        :param project_type: ProjectType
        :param price_line: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.deletePriceLine

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "priceLine": price_line,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def deregister_callback_notify(self, event_type: EventType):
        """
        Deletes an registered notify request.

        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.deregisterCallback_Notify

        return self.__client.make_request(proxy, event_type.value, unpack_dict=False)

    def deregister_callback_observer(self, job_id: int, project_type: ProjectType):
        """
        Deletes an observer.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.deregisterCallback_Observer

        arg = {"JobID": job_id, "ProjectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_action_link(
        self,
        project_type: ProjectType,
        job_id: int,
        user_id: int,
        action_link_type: JobActionLink,
    ):
        """
        Method to obtain any kind of job related action link.

        :param project_type: ProjectType
        :param job_id: int
        :param user_id: int
        :param action_link_type: JobActionLink

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getActionLink

        arg = {
            "projectType": project_type.value,
            "jobID": job_id,
            "userID": user_id,
            "actionLinkType": action_link_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_comment(self, project_type: ProjectType, job_id: int):
        """
        Method to get the work instruction comment of the job.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getComment

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_contact_person_id(self, project_type: ProjectType, job_id: int):
        """
        Returns an instance of IntegerResult containing the resource IDof the jobs contact person.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getContactPersonID

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_creation_date(self, project_type: ProjectType, job_id: int):
        """
        Returns an instance of IntegerResult containing the creation date of the job

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getCreationDate

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_currency(self, job_id: int, project_type: ProjectType):
        """
        Returns the currency of the job represented by its ISO value.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getCurrency

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_delivery_date(self, project_type: ProjectType, job_id: int):
        """
        Returns an instance of DateResult representing the deliverydate of the job using the default time zone.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getDeliveryDate

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_delivery_note(self, project_type: ProjectType, job_id: int):
        """
        Method to access the delivery note for the specified job

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getDeliveryNote

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_description(self, project_type: ProjectType, job_id: int):
        """
        Method to get the description of the job.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getDescription

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_download_url_source_data(
        self, target_file_name: str, project_type: ProjectType, job_id: int
    ):
        """
        Returns an instance of StringResult containing an urlThis can be used for downloading the source files as zip archive fromthe specified job.

        :param target_file_name: str
        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getDownloadUrl_SourceData

        arg = {
            "targetFileName": target_file_name,
            "projectType": project_type.value,
            "jobID": job_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_due_date(self, project_type: ProjectType, job_id: int):
        """
        Returns an instance of DateResult representing the due date of the job.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getDueDate

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_item_independent_jobs(self, project_type: ProjectType, project_id: int):
        """
        Returns an instance of JobListResult, which contains a list of all languageindependent jobs .

        :param project_type: ProjectType
        :param project_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getItemIndependentJobs

        arg = {"projectType": project_type.value, "projectId": project_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_job_for_view(self, job_id: int, project_type: ProjectType):
        """
        This method returns a single instance of job.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getJob_ForView

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_job_list_for_view(self, job_i_ds: str, project_type: ProjectType):
        """
        Method returns an instance of JobListResult, containing a list of Job objects.

        :param job_i_ds: str
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getJobList_ForView

        arg = {"jobIDs": job_i_ds, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_job_list_of_item_for_view(self, item_id: int, project_type: ProjectType):
        """
        Method returns an instance of JobListResult, containing a list of Job objects.

        :param item_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getJobListOfItem_ForView

        arg = {"itemID": item_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_job_metrics(
        self, job_id: int, project_type: ProjectType, language_code: str
    ):
        """
        Retrieves the job&#39;s total price and amounts.

        :param job_id: int
        :param project_type: ProjectType
        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getJobMetrics

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "languageCode": language_code,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_job_number(self, project_type: ProjectType, job_id: int):
        """
        Returns the job number, e.g. &#39;001&#39; for the job &#39;TRA-001&#39;

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getJobNumber

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_job_tracking_times_list(self, job_id: int, project_type: ProjectType):
        """
        Returns a list of all job tracking times.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getJobTrackingTimesList

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_job_type_long_name(self, project_type: ProjectType, job_id: int):
        """
        Returns an instance of StringResult containing the full name (English)of the job type for the specified job. – e.g.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getJobType_LongName

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_job_type_short_name(self, project_type: ProjectType, job_id: int):
        """
        Returns an instance of StringResult containing the abbreviated name (English)of the job type for the specified job. – e.g.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getJobType_ShortName

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_payable_id(self, job_id: int, project_type: ProjectType):
        """
        Returns the referenced payable ID

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getPayableID

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_line_list(self, job_id: int, project_type: ProjectType):
        """
        Returns a list of all job related PriceLine

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getPriceLine_List

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_line_list_by_currency_type(
        self, job_id: int, project_type: ProjectType, currency_type: CurrencyType
    ):
        """
        Returns a list of all job related PriceLineThe PriceLine will be returned in the specified CurrencyType (default: project currency).

        :param job_id: int
        :param project_type: ProjectType
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getPriceLine_ListByCurrencyType

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "currencyType": currency_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_pricelist_list(self, job_id: int, project_type: ProjectType):
        """
        Returns all avaliable Pricelist for this job.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getPricelist_List

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_pricelist(self, job_id: int, project_type: ProjectType):
        """
        Returns the current selected Pricelist for the specified job

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getPricelist

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_pricelist_entry_list(
        self, pricelist_id: int, source_language: str, target_language: str
    ):
        """
        Provides all price entries which are related to the Pricelistregarding the transfered source and target language.

        :param pricelist_id: int
        :param source_language: str
        :param target_language: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getPricelistEntry_List

        arg = {
            "pricelistID": pricelist_id,
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_unit_list(self, language_code: str, service: str):
        """
        Returns a list of priceUnit related to the specified service.

        :param language_code: str
        :param service: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getPriceUnit_List

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_unit(self, price_unit_id: int, language_code: str):
        """
        Returns a PriceUnitResult object.

        :param price_unit_id: int
        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getPriceUnit

        arg = {"PriceUnitID": price_unit_id, "languageCode": language_code}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_resource_contact_person_id(self, project_type: ProjectType, job_id: int):
        """
        Returns an instance of IntegerResult containing the resource IDof the contact person.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getResourceContactPersonID

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_resource_id(self, project_type: ProjectType, job_id: int):
        """
        Returns an instance of IntegerResult, which contains the resource idof the specified job.

        :param project_type: ProjectType
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getResourceID

        arg = {"projectType": project_type.value, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_services_list(self, language_code: str):
        """
        Deprecated.Please use DataAdmin30.getAvailableServices(String, String) instead.Returns a list of all avaliable services.

        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.getServices_List

        return self.__client.make_request(proxy, language_code, unpack_dict=False)

    def insert(
        self, project_id: int, project_type: ProjectType, job_type_abbrevation: str
    ):
        """
        Inserts a empty Job.

        :param project_id: int
        :param project_type: ProjectType
        :param job_type_abbrevation: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.insert

        arg = {
            "projectID": project_id,
            "projectType": project_type.value,
            "jobTypeAbbrevation": job_type_abbrevation,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def insert2(
        self,
        project_id: int,
        project_type: ProjectType,
        job_type_abbrevation: str,
        item_id: int,
    ):
        """
        Inserts a Job.

        :param project_id: int
        :param project_type: ProjectType
        :param job_type_abbrevation: str
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.insert2

        arg = {
            "projectID": project_id,
            "projectType": project_type.value,
            "jobTypeAbbrevation": job_type_abbrevation,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def insert3(self, job: Union[JobIN, dict], job_type_s_hort: str):
        """
        Inserts a new Job.

        :param job: JobIN
        :param job_type_s_hort: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.insert3

        if type(job) != JobIN:
            job = JobIN(**job).dict()
        else:
            job = job.dict()

        arg = {"job": job, "jobTypeSHort": job_type_s_hort}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def insert_price_line(
        self,
        job_id: int,
        project_type: ProjectType,
        price_line: Union[PriceLineIN, dict],
        create_as_first_item: bool,
    ):
        """
        Inserts a new PriceLine to the specified jobWarning: Job-Price lines do not support the price-line memo value.

        :param job_id: int
        :param project_type: ProjectType
        :param price_line: PriceLineIN
        :param create_as_first_item: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.insertPriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "priceLine": price_line,
            "createAsFirstItem": create_as_first_item,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def register_callback_notify(
        self,
        server_authentication_string: str,
        server_address: str,
        event_type: EventType,
    ):
        """
        Register to get notified when the specified EventType occursfor any job.

        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.registerCallback_Notify

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "EventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def register_callback_observer(
        self,
        server_authentication_string: str,
        server_address: str,
        job_id: int,
        project_type: ProjectType,
    ):
        """
        Register to observe a specific object for any supportedEventType.

        :param server_authentication_string: str
        :param server_address: str
        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.registerCallback_Observer

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "JobID": job_id,
            "ProjectType": project_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def run_automatic_job(self, job_id: int, project_type: ProjectType):
        """
        Start or restart an automatic job.

        :param job_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.runAutomaticJob

        arg = {"jobID": job_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_cat_report(
        self,
        path_or_url: str,
        overwrite_existing_price_lines: bool,
        cat_type: CatType,
        project_type: ProjectType,
        analyze_and_copy_result_to_job: bool,
        job_id: int,
    ):
        """
        Deprecated.Please use setCatReport2(String, byte[], String, int, int, int, boolean, int) instead.Please note that this call is now deactivated by default. For Reactivation please contact Support@plunet.com.Uploads a report file into the report folder of the specified job.Specify by value to copy the results of the report into the job andif they should overwrite already existing price lines.

        :param path_or_url: str
        :param overwrite_existing_price_lines: bool
        :param cat_type: CatType
        :param project_type: ProjectType
        :param analyze_and_copy_result_to_job: bool
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setCatReport

        arg = {
            "pathOrUrl": path_or_url,
            "overwriteExistingPriceLines": overwrite_existing_price_lines,
            "CatType": cat_type.value,
            "projectType": project_type.value,
            "analyzeAndCopyResultToJob": analyze_and_copy_result_to_job,
            "jobID": job_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_cat_report2(
        self,
        file_byte_stream: bytes,
        file_path_name: str,
        filesize: int,
        cat_type: CatType,
        project_type: ProjectType,
        analyze_and_copy_result_to_job: bool,
        job_id: int,
    ):
        """
        Uploads a report file into the report folder of the specified job.

        :param file_byte_stream: bytes
        :param file_path_name: str
        :param filesize: int
        :param cat_type: CatType
        :param project_type: ProjectType
        :param analyze_and_copy_result_to_job: bool
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setCatReport2

        arg = {
            "FileByteStream": file_byte_stream,
            "FilePathName": file_path_name,
            "Filesize": filesize,
            "CatType": cat_type.value,
            "projectType": project_type.value,
            "analyzeAndCopyResultToJob": analyze_and_copy_result_to_job,
            "jobID": job_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_comment(self, project_type: ProjectType, job_id: int, comment: str):
        """
        Method to set the work instruction comment of the job.

        :param project_type: ProjectType
        :param job_id: int
        :param comment: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setComment

        arg = {"projectType": project_type.value, "jobID": job_id, "comment": comment}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_contact_person_id(
        self, project_type: ProjectType, job_id: int, resource_id: int
    ):
        """
        Method to set the resourceID of the contact-person for the specified job.

        :param project_type: ProjectType
        :param job_id: int
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setContactPersonID

        arg = {
            "projectType": project_type.value,
            "jobID": job_id,
            "resourceID": resource_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_delivery_note(
        self, project_type: ProjectType, job_id: int, delivery_note: str
    ):
        """
        Method to set the delivery note for the specified job

        :param project_type: ProjectType
        :param job_id: int
        :param delivery_note: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setDeliveryNote

        arg = {
            "projectType": project_type.value,
            "jobID": job_id,
            "deliveryNote": delivery_note,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_description(self, project_type: ProjectType, job_id: int, description: str):
        """
        Method to set the description of the job.

        :param project_type: ProjectType
        :param job_id: int
        :param description: str

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setDescription

        arg = {
            "projectType": project_type.value,
            "jobID": job_id,
            "description": description,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_due_date(self, project_type: ProjectType, due_date: datetime, job_id: int):
        """
        Method to set the due-date for the specified job.

        :param project_type: ProjectType
        :param due_date: datetime
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setDueDate

        arg = {"projectType": project_type.value, "dueDate": due_date, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_item_id(self, project_type: ProjectType, item_id: int, job_id: int):
        """
        Method to set the item id for the specified job.

        :param project_type: ProjectType
        :param item_id: int
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setItemID

        arg = {"projectType": project_type.value, "itemID": item_id, "jobID": job_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_job_status(self, project_type: ProjectType, job_id: int, status: int):
        """
        Method to set the status for the specified job.

        :param project_type: ProjectType
        :param job_id: int
        :param status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setJobStatus

        arg = {"projectType": project_type.value, "jobID": job_id, "status": status}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_pricelist(self, job_id: int, project_type: ProjectType, price_list_id: int):
        """
        Set´s the selected Pricelist for the specified job

        :param job_id: int
        :param project_type: ProjectType
        :param price_list_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setPricelist

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "priceListID": price_list_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_price_liste_id(
        self, project_type: ProjectType, price_list_id: int, job_id: int
    ):
        """
        Deprecated.This call is deprecated and may be removed in future api versions.Please use setPricelist(String, int, int, int) instead.

        :param project_type: ProjectType
        :param price_list_id: int
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setPriceListeID

        arg = {
            "projectType": project_type.value,
            "priceListID": price_list_id,
            "jobID": job_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_resource_contact_person_id(
        self, project_type: ProjectType, job_id: int, contact_id: int
    ):
        """
        Method to set the resourceID of the contact-person.

        :param project_type: ProjectType
        :param job_id: int
        :param contact_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setResourceContactPersonID

        arg = {
            "projectType": project_type.value,
            "jobID": job_id,
            "contactID": contact_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_resource_id(self, project_type: ProjectType, resource_id: int, job_id: int):
        """
        Deprecated.This method is no longer supported. Please use the new Endpoint DataJobRound30 for resource assignment.For further information, please refer to the release notes.Method to set the resource id for the specified Job.

        :param project_type: ProjectType
        :param resource_id: int
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setResourceID

        arg = {
            "projectType": project_type.value,
            "resourceID": resource_id,
            "jobID": job_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_start_date(
        self, project_type: ProjectType, start_date: datetime, job_id: int
    ):
        """
        Method to set the start-date for the specified job.

        :param project_type: ProjectType
        :param start_date: datetime
        :param job_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.setStartDate

        arg = {
            "projectType": project_type.value,
            "startDate": start_date,
            "jobID": job_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, job: Union[JobIN, dict], enabled: bool):
        """
        Updates a job depending on the transfered job object.

        :param job: JobIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.update

        if type(job) != JobIN:
            job = JobIN(**job).dict()
        else:
            job = job.dict()

        arg = {"job": job, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_price_line(
        self,
        job_id: int,
        project_type: ProjectType,
        price_line: Union[PriceLineIN, dict],
    ):
        """
        Updates a existing PriceLine.

        :param job_id: int
        :param project_type: ProjectType
        :param price_line: PriceLineIN

        :return:
        """

        proxy = self.__client.plunet_server.DataJob30.updatePriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {
            "jobID": job_id,
            "projectType": project_type.value,
            "priceLine": price_line,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
