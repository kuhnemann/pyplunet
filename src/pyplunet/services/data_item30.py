from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CatType, CurrencyType, EventType, ProjectType
from ..models import ItemIN, PriceLineIN

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataItem30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def add_language_combination(
        self,
        source_language: str,
        target_language: str,
        project_type: ProjectType,
        project_id: int,
        item_id: int,
    ):
        """
        Deprecated.Please use {link addLanguageCombination2(String, String, String, int, int)instead the itemID is not required for this method.

        :param source_language: str
        :param target_language: str
        :param project_type: ProjectType
        :param project_id: int
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.addLanguageCombination

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "projectType": project_type.value,
            "projectID": project_id,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def add_language_combination2(
        self,
        source_language: str,
        target_language: str,
        project_type: ProjectType,
        project_id: int,
    ):
        """
        Method adds a new language combination to the currently selected projected.

        :param source_language: str
        :param target_language: str
        :param project_type: ProjectType
        :param project_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.addLanguageCombination2

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "projectType": project_type.value,
            "projectID": project_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def copy_jobs_from_workflow(
        self, workflow_id: int, project_type: ProjectType, item_id: int
    ):
        """
        Adds all jobs from the workflow jobs to the position.

        :param workflow_id: int
        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.copyJobsFromWorkflow

        arg = {
            "workflowID": workflow_id,
            "projectType": project_type.value,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete(self, item_id: int, project_type: ProjectType):
        """
        Deletes the specified item.

        :param item_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.delete

        arg = {"itemID": item_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete_price_line(
        self, item_id: int, project_type: ProjectType, price_line: int
    ):
        """
        Deletes an existing PriceLine

        :param item_id: int
        :param project_type: ProjectType
        :param price_line: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.deletePriceLine

        arg = {
            "itemID": item_id,
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

        proxy = self.__client.plunet_server.DataItem30.deregisterCallback_Notify

        return self.__client.make_request(proxy, event_type.value, unpack_dict=False)

    def deregister_callback_observer(self, item_id: int, project_type: ProjectType):
        """
        Deletes an observer.

        :param item_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.deregisterCallback_Observer

        arg = {"ItemID": item_id, "ProjectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_by_language(
        self,
        project_type: ProjectType,
        project_id: int,
        source_language: str,
        target_language: str,
    ):
        """
        Returns the itemID for the Project with the specified source/target language.

        :param project_type: ProjectType
        :param project_id: int
        :param source_language: str
        :param target_language: str

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.get_ByLanguage

        arg = {
            "projectType": project_type.value,
            "projectID": project_id,
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_all_item_objects(self, project_id: int, project_type: ProjectType):
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.

        :param project_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getAllItemObjects

        arg = {"projectID": project_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_all_item_objects_by_currency(
        self, project_id: int, project_type: ProjectType, currency_type: CurrencyType
    ):
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.

        :param project_id: int
        :param project_type: ProjectType
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getAllItemObjectsByCurrency

        arg = {
            "projectID": project_id,
            "projectType": project_type.value,
            "currencyType": currency_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_all_items(self, project_type: ProjectType, project_id: int):
        """
        Method returns an instance of IntegerArrayResult, which contains a list of all itemids for the specified project.

        :param project_type: ProjectType
        :param project_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getAllItems

        arg = {"projectType": project_type.value, "projectID": project_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_best_pricelist(self, project_type: ProjectType, item_id: int):
        """
        Method returns the ID of the best fitting customer pricelist IntegerResult.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getBestPricelist

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_brief_description(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of StringResult, which contains the the brief descriptiondepending on the itemID.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getBriefDescription

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_comment(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of StringResult, which contains the comment depending on theitemID.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getComment

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_default_contact_person(self, project_type: ProjectType, item_id: int):
        """
        Returns the resourceID of the default contact person set for the item.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getDefaultContactPerson

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_delivery_date(self, item_id: int):
        """
        Method returns an instance of DateResult, which contains the delivery date of the item(order items only!).

        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getDeliveryDate

        return self.__client.make_request(proxy, item_id, unpack_dict=False)

    def get_delivery_deadline(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of DateResult, which contains the delivery deadlinedepending on the itemID.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getDeliveryDeadline

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_document_status(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of IntegerResult, which contains the DocumentStatusdepending on the itemID.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getDocumentStatus

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_invoice_id(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of IntegerResult, which contains the ID of the invoice for thecurrently selected item.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getInvoiceID

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_item_object(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of ItemResult.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemObject

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_item_object_by_currency_type(
        self, project_type: ProjectType, item_id: int, currency_type: CurrencyType
    ):
        """
        Method returns an instance of ItemResult.

        :param project_type: ProjectType
        :param item_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemObjectByCurrencyType

        arg = {
            "projectType": project_type.value,
            "itemID": item_id,
            "currencyType": currency_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_item_reference(self, project_type: ProjectType, item_id: int):
        """
        Method returns item reference StringResult.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemReference

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_items_by_status1(self, project_type: ProjectType, status: int):
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.

        :param project_type: ProjectType
        :param status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus1

        arg = {"projectType": project_type.value, "status": status}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_items_by_status2(
        self, project_id: int, project_type: ProjectType, status: int
    ):
        """
        Method returns an instance of ItemListResult, which contains a list of item objects for acertain project.

        :param project_id: int
        :param project_type: ProjectType
        :param status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus2

        arg = {
            "projectID": project_id,
            "projectType": project_type.value,
            "status": status,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_items_by_status3(
        self, project_type: ProjectType, status: int, document_status: int
    ):
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.

        :param project_type: ProjectType
        :param status: int
        :param document_status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus3

        arg = {
            "projectType": project_type.value,
            "status": status,
            "documentStatus": document_status,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_items_by_status3_by_currency_type(
        self,
        project_type: ProjectType,
        status: int,
        document_status: int,
        currency_type: CurrencyType,
    ):
        """
        Method returns an instance of ItemListResult, which contains a list of item objects.

        :param project_type: ProjectType
        :param status: int
        :param document_status: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus3ByCurrencyType

        arg = {
            "projectType": project_type.value,
            "status": status,
            "documentStatus": document_status,
            "currencyType": currency_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_items_by_status4(
        self,
        project_id: int,
        project_type: ProjectType,
        status: int,
        document_status: int,
    ):
        """
        Method returns an instance of ItemListResult, which contains a list of item objects for acertain project.

        :param project_id: int
        :param project_type: ProjectType
        :param status: int
        :param document_status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus4

        arg = {
            "projectID": project_id,
            "projectType": project_type.value,
            "status": status,
            "documentStatus": document_status,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_items_by_status4_by_currency_type(
        self,
        project_id: int,
        project_type: ProjectType,
        status: int,
        document_status: int,
        currency_type: CurrencyType,
    ):
        """
        Method returns an instance of ItemListResult, which contains a list of item objects for acertain project.

        :param project_id: int
        :param project_type: ProjectType
        :param status: int
        :param document_status: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getItemsByStatus4ByCurrencyType

        arg = {
            "projectID": project_id,
            "projectType": project_type.value,
            "status": status,
            "documentStatus": document_status,
            "currentType": currency_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_jobs(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of IntegerArrayResult, which contains all job IDs depending on theitemID.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getJobs

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_jobs_with_status(
        self, status: int, project_type: ProjectType, item_id: int
    ):
        """
        Method returns an instance of IntegerArrayResult, which contains a list of IDs of job, whichwere linked to the currently selected item and have a specific status.

        :param status: int
        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getJobsWithStatus

        arg = {"Status": status, "projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_language_independent_item_object(
        self, project_type: ProjectType, project_id: int, currency_type: CurrencyType
    ):
        """
        Method returns an instance of ItemResult.

        :param project_type: ProjectType
        :param project_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getLanguageIndependentItemObject

        arg = {
            "projectType": project_type.value,
            "projectID": project_id,
            "currencyType": currency_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_order_id(self, project_type: ProjectType, item_id: int):
        """
        This method is only available for a quote items.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getOrderID

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_line_list(self, item_id: int, project_type: ProjectType):
        """
        Returns a list of all item related PriceLine

        :param item_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getPriceLine_List

        arg = {"itemID": item_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_line_list_by_currency(
        self, item_id: int, project_type: ProjectType, currency_type: CurrencyType
    ):
        """
        Returns a list of all item related PriceLineThe PriceLine will be returned in the specified CurrencyType (default: projectcurrency).

        :param item_id: int
        :param project_type: ProjectType
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getPriceLine_ListByCurrency

        arg = {
            "itemID": item_id,
            "projectType": project_type.value,
            "currencyType": currency_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_pricelist_list(self, item_id: int, project_type: ProjectType):
        """
        Returns all avaliable Pricelist for this item.

        :param item_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getPricelist_List

        arg = {"itemID": item_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_pricelist(self, item_id: int, project_type: ProjectType):
        """
        Returns the current selected Pricelist for the specified item

        :param item_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getPricelist

        arg = {"itemID": item_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_pricelist_entry_list(
        self, pricelist_id: int, source_language: str, target_language: str
    ):
        """
        Provides all price entries which are related to the Pricelist regarding the transferedsource and target language.

        :param pricelist_id: int
        :param source_language: str
        :param target_language: str

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getPricelistEntry_List

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

        proxy = self.__client.plunet_server.DataItem30.getPriceUnit_List

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_unit(self, price_unit_id: int, language_code: str):
        """
        Returns a PriceUnitResult object.

        :param price_unit_id: int
        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getPriceUnit

        arg = {"PriceUnitID": price_unit_id, "languageCode": language_code}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_services_list(self, language_code: str):
        """
        Deprecated.Please use DataAdmin30.getAvailableServices(String, String) instead.Returns a list of all available services.

        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getServices_List

        return self.__client.make_request(proxy, language_code, unpack_dict=False)

    def get_source_language(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of StringResult, the source language depending on the itemID

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getSourceLanguage

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_status(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of IntegerResult, which contains the ItemStatus dependingon the itemID.

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getStatus

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_target_language(self, project_type: ProjectType, item_id: int):
        """
        Method returns an instance of StringResult, which contains the target language depending onthe itemID

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getTargetLanguage

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_total_price(self, project_type: ProjectType, item_id: int):
        """
        Method returns total price for an item (project currency).

        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getTotalPrice

        arg = {"projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_total_price_by_currency_type(
        self, project_type: ProjectType, item_id: int, currency_type: CurrencyType
    ):
        """
        Method returns total price for an item.

        :param project_type: ProjectType
        :param item_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.getTotalPriceByCurrencyType

        arg = {
            "projectType": project_type.value,
            "itemID": item_id,
            "currencyType": currency_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def insert(self, project_id: int, project_type: ProjectType):
        """
        Inserts a new item into the the specified project

        :param project_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.insert

        arg = {"projectID": project_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def insert2(self, item: Union[ItemIN, dict]):
        """
        Inserts a new item into the the specified project.

        :param item: ItemIN

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.insert2

        if type(item) != ItemIN:
            item = ItemIN(**item).dict()
        else:
            item = item.dict()

        return self.__client.make_request(proxy, item, unpack_dict=False)

    def insert_language_independent_item(self, item: Union[ItemIN, dict]):
        """
        Inserts a new language indipendend item into the the specified project.

        :param item: ItemIN

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.insertLanguageIndependentItem

        if type(item) != ItemIN:
            item = ItemIN(**item).dict()
        else:
            item = item.dict()

        return self.__client.make_request(proxy, item, unpack_dict=False)

    def insert_price_line(
        self,
        item_id: int,
        project_type: ProjectType,
        price_line: Union[PriceLineIN, dict],
        create_as_first_item: bool,
    ):
        """
        Inserts a new PriceLine to the specified item

        :param item_id: int
        :param project_type: ProjectType
        :param price_line: PriceLineIN
        :param create_as_first_item: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.insertPriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {
            "itemID": item_id,
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
        Register to get notified when the specified EventType occurs for any item.

        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.registerCallback_Notify

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
        item_id: int,
        project_type: ProjectType,
    ):
        """
        Register to observe a specific object for any supported EventType.

        :param server_authentication_string: str
        :param server_address: str
        :param item_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.registerCallback_Observer

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "ItemID": item_id,
            "ProjectType": project_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def seek_language_combination(
        self,
        source_language: str,
        target_language: str,
        project_type: ProjectType,
        project_id: int,
        item_id: int,
    ):
        """
        Method returns an instance of IntegerResult, which contains the ID of a specific languagecombination for the specified project.

        :param source_language: str
        :param target_language: str
        :param project_type: ProjectType
        :param project_id: int
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.seekLanguageCombination

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "projectType": project_type.value,
            "projectID": project_id,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_brief_description(
        self, description: str, project_type: ProjectType, item_id: int
    ):
        """
        Method sets the brief description for the currently selected item.

        :param description: str
        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setBriefDescription

        arg = {
            "description": description,
            "projectType": project_type.value,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_cat_report(
        self,
        path_or_url: str,
        overwrite_existing_price_lines: bool,
        cat_type: CatType,
        project_type: ProjectType,
        copy_results_to_item: bool,
        item_id: int,
    ):
        """
        Deprecated.Please usesetCatReport2(String, byte[], String, int, boolean, int, int, boolean, int)instead. Please note that this call is now deactivated by default. For Reactivationplease contact Support@plunet.com.Uploads a report file into the report folder of the specified item.Also allows to copy the results of the report into the item (optionally overwritingexisting price lines)

        :param path_or_url: str
        :param overwrite_existing_price_lines: bool
        :param cat_type: CatType
        :param project_type: ProjectType
        :param copy_results_to_item: bool
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setCatReport

        arg = {
            "pathOrUrl": path_or_url,
            "overwriteExistingPriceLines": overwrite_existing_price_lines,
            "CatType": cat_type.value,
            "projectType": project_type.value,
            "copyResultsToItem": copy_results_to_item,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_cat_report2(
        self,
        file_byte_stream: bytes,
        file_path_name: str,
        filesize: int,
        overwrite_existing_price_lines: bool,
        cat_type: CatType,
        project_type: ProjectType,
        copy_results_to_item: bool,
        item_id: int,
    ):
        """
        Uploads a report file into the report folder of the specified item.

        :param file_byte_stream: bytes
        :param file_path_name: str
        :param filesize: int
        :param overwrite_existing_price_lines: bool
        :param cat_type: CatType
        :param project_type: ProjectType
        :param copy_results_to_item: bool
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setCatReport2

        arg = {
            "FileByteStream": file_byte_stream,
            "FilePathName": file_path_name,
            "Filesize": filesize,
            "overwriteExistingPriceLines": overwrite_existing_price_lines,
            "CatType": cat_type.value,
            "projectType": project_type.value,
            "copyResultsToItem": copy_results_to_item,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_comment(self, comment: str, project_type: ProjectType, item_id: int):
        """
        Method sets the comment depending on the itemID.

        :param comment: str
        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setComment

        arg = {"comment": comment, "projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_default_contact_person(
        self, project_type: ProjectType, item_id: int, resource_id: int
    ):
        """
        Sets the default job contact person for the item.

        :param project_type: ProjectType
        :param item_id: int
        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setDefaultContactPerson

        arg = {
            "projectType": project_type.value,
            "itemId": item_id,
            "resourceId": resource_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_delivery_date(self, delivery_date: datetime, item_id: int):
        """
        Method sets the delivery date for the specified item (order items only!).

        :param delivery_date: datetime
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setDeliveryDate

        arg = {"deliveryDate": delivery_date, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_delivery_deadline(
        self, deadline: datetime, project_type: ProjectType, item_id: int
    ):
        """
        Method sets the delivery deadline for the specified item.

        :param deadline: datetime
        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setDeliveryDeadline

        arg = {
            "deadline": deadline,
            "projectType": project_type.value,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_document_status(
        self, document_status: int, project_type: ProjectType, item_id: int
    ):
        """
        Method to set the DocumentStatus for the specified item.

        :param document_status: int
        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setDocumentStatus

        arg = {
            "documentStatus": document_status,
            "projectType": project_type.value,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_item_reference(
        self, project_type: ProjectType, item_id: int, reference: str
    ):
        """
        Sets item reference.

        :param project_type: ProjectType
        :param item_id: int
        :param reference: str

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setItemReference

        arg = {
            "projectType": project_type.value,
            "itemID": item_id,
            "reference": reference,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_language_combination_id(
        self, language_combination_id: int, project_type: ProjectType, item_id: int
    ):
        """
        Method sets the language combination ID for the specified item.

        :param language_combination_id: int
        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setLanguageCombinationID

        arg = {
            "languageCombinationID": language_combination_id,
            "projectType": project_type.value,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_pricelist(
        self, item_id: int, project_type: ProjectType, price_list_id: int
    ):
        """
        Set´s the selected Pricelist for the specified item

        :param item_id: int
        :param project_type: ProjectType
        :param price_list_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setPricelist

        arg = {
            "itemID": item_id,
            "projectType": project_type.value,
            "priceListID": price_list_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, project_type: ProjectType, item_id: int):
        """
        Method to set the ItemStatus for the specified item.

        :param status: int
        :param project_type: ProjectType
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setStatus

        arg = {"status": status, "projectType": project_type.value, "itemID": item_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_total_price(
        self, project_type: ProjectType, total_price: float, item_id: int
    ):
        """
        Method sets total price for an item (project currency).

        :param project_type: ProjectType
        :param total_price: float
        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.setTotalPrice

        arg = {
            "projectType": project_type.value,
            "totalPrice": total_price,
            "itemID": item_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, item: Union[ItemIN, dict], enabled: bool):
        """
        Updates the item by the transfered item object Use EnableNullOrEmptyValues to decide if Nullor empty strings are saved into Plunet or ignored.

        :param item: ItemIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.update

        if type(item) != ItemIN:
            item = ItemIN(**item).dict()
        else:
            item = item.dict()

        arg = {"item": item, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_price_line(
        self,
        item_id: int,
        project_type: ProjectType,
        price_line: Union[PriceLineIN, dict],
    ):
        """
        Updates a existing PriceLine.

        :param item_id: int
        :param project_type: ProjectType
        :param price_line: PriceLineIN

        :return:
        """

        proxy = self.__client.plunet_server.DataItem30.updatePriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {
            "itemID": item_id,
            "projectType": project_type.value,
            "priceLine": price_line,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
