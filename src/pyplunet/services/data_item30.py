from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CatType, CurrencyType, DocumentStatus, EventType, ProjectType
from ..models import (
    DateResult,
    DoubleResult,
    IntegerArrayResult,
    IntegerResult,
    ItemIN,
    ItemListResult,
    ItemResult,
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


class DataItem30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def get_items_by_status2(
        self, project_id: int, project_type: Union[ProjectType, int], status: int
    ) -> ItemListResult:
        """
        Method returns an instance of ItemListResult, which contains a list of item objects for a
        certain project.

        Items are filtered by the item status.


        :param project_id: int
        :param project_type: ProjectType
        :param status: int
        :return: ItemListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus2
        response_model = ItemListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectID": project_id, "projectType": project_type, "status": status}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def add_language_combination(
        self,
        source_language: str,
        target_language: str,
        project_type: Union[ProjectType, int],
        project_id: int,
        item_id: int,
    ) -> IntegerResult:
        """
        Deprecated. Please use {link addLanguageCombination2(String, String, String, int, int)
        instead the itemID is not required for this method.


        :param source_language: str
        :param target_language: str
        :param project_type: ProjectType
        :param project_id: int
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.addLanguageCombination
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "projectType": project_type,
            "projectID": project_id,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_items_by_status3(
        self,
        project_type: Union[ProjectType, int],
        status: int,
        document_status: Union[DocumentStatus, int],
    ) -> ItemListResult:
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.

        Items are filtered by the item status and the document status.


        :param project_type: ProjectType
        :param status: int
        :param document_status: DocumentStatus
        :return: ItemListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus3
        response_model = ItemListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        if type(document_status) == DocumentStatus:
            document_status = document_status.value
        elif type(document_status) == int:
            document_status = document_status
        else:
            document_status = int(document_status)

        arg = {
            "projectType": project_type,
            "status": status,
            "documentStatus": document_status,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_source_language(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> StringResult:
        """
        Method returns an instance of StringResult, the source language depending on the itemID


        :param project_type: ProjectType
        :param item_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataItem30.getSourceLanguage
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def seek_language_combination(
        self,
        source_language: str,
        target_language: str,
        project_type: Union[ProjectType, int],
        project_id: int,
        item_id: int,
    ) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains the ID of a specific language
        combination for the specified project.


        :param source_language: str
        :param target_language: str
        :param project_type: ProjectType
        :param project_id: int
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.seekLanguageCombination
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "projectType": project_type,
            "projectID": project_id,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_jobs_with_status(
        self, status: int, project_type: Union[ProjectType, int], item_id: int
    ) -> IntegerArrayResult:
        """
        Method returns an instance of IntegerArrayResult, which contains a list of IDs of job, which
        were linked to the currently selected item and have a specific status.


        :param status: int
        :param project_type: ProjectType
        :param item_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataItem30.getJobsWithStatus
        response_model = IntegerArrayResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"Status": status, "projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_item_objects(
        self, project_id: int, project_type: Union[ProjectType, int]
    ) -> ItemListResult:
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.


        :param project_id: int
        :param project_type: ProjectType
        :return: ItemListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getAllItemObjects
        response_model = ItemListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectID": project_id, "projectType": project_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_target_language(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> StringResult:
        """
        Method returns an instance of StringResult, which contains the target language depending on
        the itemID


        :param project_type: ProjectType
        :param item_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataItem30.getTargetLanguage
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_language_combination_id(
        self,
        language_combination_id: int,
        project_type: Union[ProjectType, int],
        item_id: int,
    ) -> Result:
        """
        Method sets the language combination ID for the specified item.


        :param language_combination_id: int
        :param project_type: ProjectType
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setLanguageCombinationID
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "languageCombinationID": language_combination_id,
            "projectType": project_type,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_items_by_status1(
        self, project_type: Union[ProjectType, int], status: int
    ) -> ItemListResult:
        """
        Method returns an instance of ItemListResult, which contains a list of item objects. Items are
        filtered by the item status.


        :param project_type: ProjectType
        :param status: int
        :return: ItemListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus1
        response_model = ItemListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "status": status}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_items_by_status4(
        self,
        project_id: int,
        project_type: Union[ProjectType, int],
        status: int,
        document_status: Union[DocumentStatus, int],
    ) -> ItemListResult:
        """
        Method returns an instance of ItemListResult, which contains a list of item objects for a
        certain project.

        Items are filtered by the item status and the document status.


        :param project_id: int
        :param project_type: ProjectType
        :param status: int
        :param document_status: DocumentStatus
        :return: ItemListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus4
        response_model = ItemListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        if type(document_status) == DocumentStatus:
            document_status = document_status.value
        elif type(document_status) == int:
            document_status = document_status
        else:
            document_status = int(document_status)

        arg = {
            "projectID": project_id,
            "projectType": project_type,
            "status": status,
            "documentStatus": document_status,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update(
        self, item_in: Union[ItemIN, dict], enable_null_or_empty_values: bool
    ) -> Result:
        """
        Updates the item by the transfered item object Use EnableNullOrEmptyValues to decide if Null
        or empty strings are saved into Plunet or ignored.


        :param item_in: ItemIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.update
        response_model = Result

        if type(item_in) != ItemIN:
            item_in = ItemIN(**item_in).dict()
        else:
            item_in = item_in.dict()

        arg = {
            "ItemIN": item_in,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete(self, item_id: int, project_type: Union[ProjectType, int]) -> Result:
        """
        Deletes the specified item.


        :param item_id: int
        :param project_type: ProjectType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.delete
        response_model = Result

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

    def insert(
        self, project_id: int, project_type: Union[ProjectType, int]
    ) -> IntegerResult:
        """
        Inserts a new item into the the specified project


        :param project_id: int
        :param project_type: ProjectType
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.insert
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectID": project_id, "projectType": project_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_comment(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> StringResult:
        """
        Method returns an instance of StringResult, which contains the comment depending on the
        itemID.


        :param project_type: ProjectType
        :param item_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataItem30.getComment
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_comment(
        self, comment: str, project_type: Union[ProjectType, int], item_id: int
    ) -> Result:
        """
        Method sets the comment depending on the itemID.


        :param comment: str
        :param project_type: ProjectType
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setComment
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"comment": comment, "projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def deregister_callback_observer(
        self, item_id: int, project_type: Union[ProjectType, int]
    ) -> Result:
        """
        Deletes an observer.

        Observer can only deleted by the user who has created them.


        :param item_id: int
        :param project_type: ProjectType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.deregisterCallback_Observer
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"ItemID": item_id, "ProjectType": project_type}

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
        Register to get notified when the specified EventType occurs for any item.

        If the EventType occurs PBM will call the callback web service, which is hosted within
        your environment. The notifier will only be notified if the event is triggered by a different
        user.


        Please check CallbackItem30 for the exact specification for this service.


        Info:Each user can only create one notifier per event


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl


        In the first two cases, the address will be autocompleted by appending the corresponding
        directory "CallbackItem30?wsdl".


        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.registerCallback_Notify
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

        proxy = self.__client.plunet_server.DataItem30.deregisterCallback_Notify
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
        item_id: int,
        project_type: Union[ProjectType, int],
    ) -> Result:
        """
        Register to observe a specific object for any supported EventType.

        As soon as any supported EventType occurs, PBM will call the callback web service, which
        is hosted within your environment. The observer will only be notified if the event is triggered
        by a different user.


        Please check CallbackItem30 for the exact specification for this service.


        Info:Each user can only create one observer per id


        The  must match one of the following formats:

        http://mypath
        http://mypath/
        http://mypath/subfolder?wsdl


        In the first two cases, the address will be autocompleted by appending the corresponding
        directory "CallbackItem30?wsdl".


        A list of all registered callbacks can be accessed with
        DataAdmin30.getListOfRegisteredCallbacks(String)


        :param server_authentication_string: str
        :param server_address: str
        :param item_id: int
        :param project_type: ProjectType
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.registerCallback_Observer
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
            "ItemID": item_id,
            "ProjectType": project_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def add_language_combination2(
        self,
        source_language: str,
        target_language: str,
        project_type: Union[ProjectType, int],
        project_id: int,
    ) -> IntegerResult:
        """
        Method adds a new language combination to the currently selected projected.

        This will be done without calling the update method. Returns an instance of IntegerResult, which
        contains the identifier of the new language combination.


        :param source_language: str
        :param target_language: str
        :param project_type: ProjectType
        :param project_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.addLanguageCombination2
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "projectType": project_type,
            "projectID": project_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def copy_jobs_from_workflow(
        self, workflow_id: int, project_type: Union[ProjectType, int], item_id: int
    ) -> Result:
        """
        Adds all jobs from the workflow jobs to the position.


        :param workflow_id: int
        :param project_type: ProjectType
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.copyJobsFromWorkflow
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "workflowID": workflow_id,
            "projectType": project_type,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_price_line_list(
        self, item_id: int, project_type: Union[ProjectType, int]
    ) -> PriceLineListResult:
        """
        Returns a list of all item related PriceLine


        :param item_id: int
        :param project_type: ProjectType
        :return: PriceLineListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getPriceLine_List
        response_model = PriceLineListResult

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

    def get_language_independent_item_object(
        self,
        project_type: Union[ProjectType, int],
        project_id: int,
        currency_type: Union[CurrencyType, int],
    ) -> ItemResult:
        """
        Method returns an instance of ItemResult.

        The total price will be displayed in the specified CurrencyType (default: project
        currency).


        :param project_type: ProjectType
        :param project_id: int
        :param currency_type: CurrencyType
        :return: ItemResult
        """

        proxy = self.__client.plunet_server.DataItem30.getLanguageIndependentItemObject
        response_model = ItemResult

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
            "projectType": project_type,
            "projectID": project_id,
            "currencyType": currency_type,
        }

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

        proxy = self.__client.plunet_server.DataItem30.getPriceUnit_List
        response_model = PriceUnitListResult

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert_language_independent_item(
        self, item_in: Union[ItemIN, dict]
    ) -> IntegerResult:
        """
        Inserts a new language indipendend item into the the specified project.

        There can only be one language independent item per project


        :param item_in: ItemIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.insertLanguageIndependentItem
        response_model = IntegerResult

        if type(item_in) != ItemIN:
            item_in = ItemIN(**item_in).dict()
        else:
            item_in = item_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=item_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_items_by_status3_by_currency_type(
        self,
        project_type: Union[ProjectType, int],
        status: int,
        document_status: Union[DocumentStatus, int],
        currency_type: Union[CurrencyType, int],
    ) -> ItemListResult:
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.

        Items are filtered by the item status and the document status. The total price of the items can
        be returned in the project or home currency.


        :param project_type: ProjectType
        :param status: int
        :param document_status: DocumentStatus
        :param currency_type: CurrencyType
        :return: ItemListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus3ByCurrencyType
        response_model = ItemListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        if type(document_status) == DocumentStatus:
            document_status = document_status.value
        elif type(document_status) == int:
            document_status = document_status
        else:
            document_status = int(document_status)

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {
            "projectType": project_type,
            "status": status,
            "documentStatus": document_status,
            "currencyType": currency_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_total_price_by_currency_type(
        self,
        project_type: Union[ProjectType, int],
        item_id: int,
        currency_type: Union[CurrencyType, int],
    ) -> DoubleResult:
        """
        Method returns total price for an item.

        By default, the price is returned in project currency.


        :param project_type: ProjectType
        :param item_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataItem30.getTotalPriceByCurrencyType
        response_model = DoubleResult

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
            "projectType": project_type,
            "itemID": item_id,
            "currencyType": currency_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_items_by_status4_by_currency_type(
        self,
        project_id: int,
        project_type: Union[ProjectType, int],
        status: int,
        document_status: Union[DocumentStatus, int],
        current_type: Union[CurrencyType, int],
    ) -> ItemListResult:
        """
        Method returns an instance of ItemListResult, which contains a list of item objects for a
        certain project.

        Items are filtered by the item status and the document status. The total price of the items can
        be returned in the project or home currency.


        :param project_id: int
        :param project_type: ProjectType
        :param status: int
        :param document_status: DocumentStatus
        :param current_type: CurrencyType
        :return: ItemListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus4ByCurrencyType
        response_model = ItemListResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        if type(document_status) == DocumentStatus:
            document_status = document_status.value
        elif type(document_status) == int:
            document_status = document_status
        else:
            document_status = int(document_status)

        if type(current_type) == CurrencyType:
            current_type = current_type.value
        elif type(current_type) == int:
            current_type = current_type
        else:
            current_type = int(current_type)

        arg = {
            "projectID": project_id,
            "projectType": project_type,
            "status": status,
            "documentStatus": document_status,
            "currentType": current_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_default_contact_person(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> IntegerResult:
        """
        Returns the resourceID of the default contact person set for the item.


        :param project_type: ProjectType
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.getDefaultContactPerson
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_item_objects_by_currency(
        self,
        project_id: int,
        project_type: Union[ProjectType, int],
        currency_type: Union[CurrencyType, int],
    ) -> ItemListResult:
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.

        The total prices will be displayed in the specified CurrencyType (default: project
        currency).


        :param project_id: int
        :param project_type: ProjectType
        :param currency_type: CurrencyType
        :return: ItemListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getAllItemObjectsByCurrency
        response_model = ItemListResult

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
            "projectID": project_id,
            "projectType": project_type,
            "currencyType": currency_type,
        }

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
        Provides all price entries which are related to the Pricelist regarding the transfered
        source and target language.


        :param pricelist_id: int
        :param source_language: str
        :param target_language: str
        :return: PricelistEntryList
        """

        proxy = self.__client.plunet_server.DataItem30.getPricelistEntry_List
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

    def get_item_object_by_currency_type(
        self,
        project_type: Union[ProjectType, int],
        item_id: int,
        currency_type: Union[CurrencyType, int],
    ) -> ItemResult:
        """
        Method returns an instance of ItemResult.

        The total price will be displayed in the specified CurrencyType (default: project
        currency).


        :param project_type: ProjectType
        :param item_id: int
        :param currency_type: CurrencyType
        :return: ItemResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemObjectByCurrencyType
        response_model = ItemResult

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
            "projectType": project_type,
            "itemID": item_id,
            "currencyType": currency_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelist_list(
        self, item_id: int, project_type: Union[ProjectType, int]
    ) -> PricelistListResult:
        """
        Returns all avaliable Pricelist for this item.

        Note: This is dependent on the related project and the selected customer


        :param item_id: int
        :param project_type: ProjectType
        :return: PricelistListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getPricelist_List
        response_model = PricelistListResult

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

    def get_price_line_list_by_currency(
        self,
        item_id: int,
        project_type: Union[ProjectType, int],
        currency_type: Union[CurrencyType, int],
    ) -> PriceLineListResult:
        """
        Returns a list of all item related PriceLine

        The PriceLine will be returned in the specified CurrencyType (default: project
        currency).


        :param item_id: int
        :param project_type: ProjectType
        :param currency_type: CurrencyType
        :return: PriceLineListResult
        """

        proxy = self.__client.plunet_server.DataItem30.getPriceLine_ListByCurrency
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
            "itemID": item_id,
            "projectType": project_type,
            "currencyType": currency_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_default_contact_person(
        self, project_type: Union[ProjectType, int], item_id: int, resource_id: int
    ) -> Result:
        """
        Sets the default job contact person for the item.


        :param project_type: ProjectType
        :param item_id: int
        :param resource_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setDefaultContactPerson
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "projectType": project_type,
            "itemId": item_id,
            "resourceId": resource_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_status(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains the ItemStatus depending
        on the itemID.


        :param project_type: ProjectType
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.getStatus
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_status(
        self, status: int, project_type: Union[ProjectType, int], item_id: int
    ) -> Result:
        """
        Method to set the ItemStatus for the specified item.


        :param status: int
        :param project_type: ProjectType
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setStatus
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"status": status, "projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_brief_description(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> StringResult:
        """
        Method returns an instance of StringResult, which contains the the brief description
        depending on the itemID.


        :param project_type: ProjectType
        :param item_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataItem30.getBriefDescription
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_document_status(
        self,
        document_status: Union[DocumentStatus, int],
        project_type: Union[ProjectType, int],
        item_id: int,
    ) -> Result:
        """
        Method to set the DocumentStatus for the specified item.


        :param document_status: DocumentStatus
        :param project_type: ProjectType
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setDocumentStatus
        response_model = Result

        if type(document_status) == DocumentStatus:
            document_status = document_status.value
        elif type(document_status) == int:
            document_status = document_status
        else:
            document_status = int(document_status)

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "documentStatus": document_status,
            "projectType": project_type,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_delivery_deadline(
        self, deadline: datetime, project_type: Union[ProjectType, int], item_id: int
    ) -> Result:
        """
        Method sets the delivery deadline for the specified item.


        :param deadline: datetime
        :param project_type: ProjectType
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setDeliveryDeadline
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"deadline": deadline, "projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_brief_description(
        self, description: str, project_type: Union[ProjectType, int], item_id: int
    ) -> Result:
        """
        Method sets the brief description for the currently selected item.


        :param description: str
        :param project_type: ProjectType
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setBriefDescription
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "description": description,
            "projectType": project_type,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_document_status(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains the DocumentStatus
        depending on the itemID.


        :param project_type: ProjectType
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.getDocumentStatus
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_delivery_deadline(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> DateResult:
        """
        Method returns an instance of DateResult, which contains the delivery deadline
        depending on the itemID.


        :param project_type: ProjectType
        :param item_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataItem30.getDeliveryDeadline
        response_model = DateResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_best_pricelist(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> IntegerResult:
        """
        Method returns the ID of the best fitting customer pricelist IntegerResult.


        :param project_type: ProjectType
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.getBestPricelist
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_item_reference(
        self, project_type: Union[ProjectType, int], item_id: int, reference: str
    ) -> Result:
        """
        Sets item reference.


        :param project_type: ProjectType
        :param item_id: int
        :param reference: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setItemReference
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id, "reference": reference}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update_price_line(
        self,
        item_id: int,
        project_type: Union[ProjectType, int],
        price_line_in: Union[PriceLineIN, dict],
    ) -> PriceLineResult:
        """
        Updates a existing PriceLine.


        :param item_id: int
        :param project_type: ProjectType
        :param price_line_in: PriceLineIN
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataItem30.updatePriceLine
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
            "itemID": item_id,
            "projectType": project_type,
            "priceLineIN": price_line_in,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelist(
        self, item_id: int, project_type: Union[ProjectType, int]
    ) -> PricelistResult:
        """
        Returns the current selected Pricelist for the specified item


        :param item_id: int
        :param project_type: ProjectType
        :return: PricelistResult
        """

        proxy = self.__client.plunet_server.DataItem30.getPricelist
        response_model = PricelistResult

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

    def set_pricelist(
        self, item_id: int, project_type: Union[ProjectType, int], price_list_id: int
    ) -> Result:
        """
        SetÂ´s the selected Pricelist for the specified item


        :param item_id: int
        :param project_type: ProjectType
        :param price_list_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setPricelist
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "itemID": item_id,
            "projectType": project_type,
            "priceListID": price_list_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_item_reference(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> StringResult:
        """
        Method returns item reference StringResult.


        :param project_type: ProjectType
        :param item_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemReference
        response_model = StringResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_services_list(self, language_code: str) -> StringArrayResult:
        """
        Deprecated. Please use DataAdmin30.getAvailableServices(String, String) instead.
        Returns a list of all available services.


        :param language_code: str
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataItem30.getServices_List
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

        Possible PriceUnitÂ´s can be obtained over getPriceUnit_List(java.lang.String, java.lang.String, java.lang.String)


        :param price_unit_id: int
        :param language_code: str
        :return: PriceUnitResult
        """

        proxy = self.__client.plunet_server.DataItem30.getPriceUnit
        response_model = PriceUnitResult

        arg = {"PriceUnitID": price_unit_id, "languageCode": language_code}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_by_language(
        self,
        project_type: Union[ProjectType, int],
        project_id: int,
        source_language: str,
        target_language: str,
    ) -> IntegerResult:
        """
        Returns the itemID for the Project with the specified source/target language.


        :param project_type: ProjectType
        :param project_id: int
        :param source_language: str
        :param target_language: str
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.get_ByLanguage
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "projectType": project_type,
            "projectID": project_id,
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert_price_line(
        self,
        item_id: int,
        project_type: Union[ProjectType, int],
        price_line_in: Union[PriceLineIN, dict],
        create_as_first_item: bool,
    ) -> PriceLineResult:
        """
        Inserts a new PriceLine to the specified item


        :param item_id: int
        :param project_type: ProjectType
        :param price_line_in: PriceLineIN
        :param create_as_first_item: bool
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataItem30.insertPriceLine
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
            "itemID": item_id,
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
        self, item_id: int, project_type: Union[ProjectType, int], price_line_id: int
    ) -> Result:
        """
        Deletes an existing PriceLine


        :param item_id: int
        :param project_type: ProjectType
        :param price_line_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.deletePriceLine
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "itemID": item_id,
            "projectType": project_type,
            "priceLineID": price_line_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_delivery_date(self, delivery_date: datetime, item_id: int) -> Result:
        """
        Method sets the delivery date for the specified item (order items only!).


        :param delivery_date: datetime
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setDeliveryDate
        response_model = Result

        arg = {"deliveryDate": delivery_date, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_delivery_date(self, item_id: int) -> DateResult:
        """
        Method returns an instance of DateResult, which contains the delivery date of the item
        (order items only!).


        :param item_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataItem30.getDeliveryDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=item_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert2(self, item_in: Union[ItemIN, dict]) -> IntegerResult:
        """
        Inserts a new item into the the specified project.


        :param item_in: ItemIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.insert2
        response_model = IntegerResult

        if type(item_in) != ItemIN:
            item_in = ItemIN(**item_in).dict()
        else:
            item_in = item_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=item_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_id(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> IntegerResult:
        """
        This method is only available for a quote items.

        The method returns an instance of IntegerResult, which contains the order ID, to which this item
        (quote) is linked with the order creation.


        :param project_type: ProjectType
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.getOrderID
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

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
        overwrite_existing_price_lines: bool,
        cat_type: Union[CatType, int],
        project_type: Union[ProjectType, int],
        copy_results_to_item: bool,
        item_id: int,
    ) -> Result:
        """
        Uploads a report file into the report folder of the specified item.

        Also allows to copy the results of the report into the item (optionally overwriting existing
        price lines)


        :param file_byte_stream: bytes
        :param file_path_name: str
        :param filesize: int
        :param overwrite_existing_price_lines: bool
        :param cat_type: CatType
        :param project_type: ProjectType
        :param copy_results_to_item: bool
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setCatReport2
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
            "overwriteExistingPriceLines": overwrite_existing_price_lines,
            "catType": cat_type,
            "projectType": project_type,
            "copyResultsToItem": copy_results_to_item,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_invoice_id(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> IntegerResult:
        """
        Method returns an instance of IntegerResult, which contains the ID of the invoice for the
        currently selected item.

        This method is only available for an order items.


        :param project_type: ProjectType
        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataItem30.getInvoiceID
        response_model = IntegerResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_total_price(
        self, project_type: Union[ProjectType, int], total_price: float, item_id: int
    ) -> Result:
        """
        Method sets total price for an item (project currency).


        :param project_type: ProjectType
        :param total_price: float
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setTotalPrice
        response_model = Result

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {
            "projectType": project_type,
            "totalPrice": total_price,
            "itemID": item_id,
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
        copy_results_to_item: bool,
        item_id: int,
    ) -> Result:
        """
        Deprecated. Please use
        setCatReport2(String, byte[], String, int, boolean, int, int, boolean, int)
        instead. Please note that this call is now deactivated by default. For Reactivation
        please contact Support@plunet.com.


        Uploads a report file into the report folder of the specified item.

        Also allows to copy the results of the report into the item (optionally overwriting
        existing price lines)


        :param path_or_url: str
        :param overwrite_existing_price_lines: bool
        :param cat_type: CatType
        :param project_type: ProjectType
        :param copy_results_to_item: bool
        :param item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataItem30.setCatReport
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
            "copyResultsToItem": copy_results_to_item,
            "itemID": item_id,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_item_object(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> ItemResult:
        """
        Method returns an instance of ItemResult.


        :param project_type: ProjectType
        :param item_id: int
        :return: ItemResult
        """

        proxy = self.__client.plunet_server.DataItem30.getItemObject
        response_model = ItemResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_jobs(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> IntegerArrayResult:
        """
        Method returns an instance of IntegerArrayResult, which contains all job IDs depending on the
        itemID.


        :param project_type: ProjectType
        :param item_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataItem30.getJobs
        response_model = IntegerArrayResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_total_price(
        self, project_type: Union[ProjectType, int], item_id: int
    ) -> DoubleResult:
        """
        Method returns total price for an item (project currency).


        :param project_type: ProjectType
        :param item_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataItem30.getTotalPrice
        response_model = DoubleResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "itemID": item_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_all_items(
        self, project_type: Union[ProjectType, int], project_id: int
    ) -> IntegerArrayResult:
        """
        Method returns an instance of IntegerArrayResult, which contains a list of all item
        ids for the specified project.


        :param project_type: ProjectType
        :param project_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataItem30.getAllItems
        response_model = IntegerArrayResult

        if type(project_type) == ProjectType:
            project_type = project_type.value
        elif type(project_type) == int:
            project_type = project_type
        else:
            project_type = int(project_type)

        arg = {"projectType": project_type, "projectID": project_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )
