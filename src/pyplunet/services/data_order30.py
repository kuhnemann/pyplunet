from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType, JobActionLink, ProjectType
from ..models import IntegerList, OrderIN, SearchFilter_Order

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataOrder30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def add_language_combination(
        self, source_language: str, target_language: str, order_id: int
    ):
        """
        Adds a language combination to the specified order.

        :param source_language: str
        :param target_language: str
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.addLanguageCombination

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "orderID": order_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def check_en15038(self, order_id: int):
        """
        Method returns an instance of BooleanResult, which contains the information,whether a project corresponds the EN15038 standard or not.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.checkEN15038

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def create_link(
        self,
        source_order_id: int,
        target_id: int,
        project_type: ProjectType,
        is_bidirectional: bool,
        memo: str,
    ):
        """
        Creates a link between two orders.

        :param source_order_id: int
        :param target_id: int
        :param project_type: ProjectType
        :param is_bidirectional: bool
        :param memo: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.createLink

        arg = {
            "sourceOrderId": source_order_id,
            "targetId": target_id,
            "projectType": project_type.value,
            "isBidirectional": is_bidirectional,
            "memo": memo,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def create_order_confirmation(self, template: str, format_id: int, order_id: int):
        """
        Method creates the order confirmation as rtf-file and returns an instance of StringResult,which contains the network path where the file is located.

        :param template: str
        :param format_id: int
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.createOrderConfirmation

        arg = {"template": template, "formatId": format_id, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete(self, order_id: int):
        """
        Method to delete an order via ID.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.delete

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def deregister_callback_notify(self, event_type: EventType):
        """
        Deletes an registered notify request.

        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.deregisterCallback_Notify

        return self.__client.make_request(proxy, event_type.value, unpack_dict=False)

    def deregister_callback_observer(self, order_id: int):
        """
        Deletes an observer.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.deregisterCallback_Observer

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_action_link(
        self, order_id: int, user_id: int, action_link_type: JobActionLink
    ):
        """
        Method to obtain any kind of order related action link.

        :param order_id: int
        :param user_id: int
        :param action_link_type: JobActionLink

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getActionLink

        arg = {
            "orderID": order_id,
            "userID": user_id,
            "actionLinkType": action_link_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_creation_date(self, order_id: int):
        """
        Returns an instance of DateResult, which contains the creation date.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getCreationDate

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_currency(self, order_id: int):
        """
        Returns an instance of StringResult, which contains the currency.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getCurrency

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_customer_contact_id(self, order_id: int):
        """
        Returns an instance of IntegerResult, which contains the customer contact id.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getCustomerContactID

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_customer_id(self, order_id: int):
        """
        Returns an instance of IntegerResult, which contains the customer id.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getCustomerID

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_delivery_comment(self, order_id: int):
        """
        Method returns an instance of StringResult, which contains the delivery comment.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getDeliveryComment

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_delivery_deadline(self, order_id: int):
        """
        Returns an instance of DateResult, which contains the delivery deadline.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getDeliveryDeadline

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_documents_within_final_folder(self, order_id: int):
        """
        Deprecated.Please use DataDocument30.getFileList(String, int, int) with Folder Type = 12 insteadfor compatibility reasons with DataDocument30.Returns an instance of StringArrayResult, which contains a list of networkpaths to all documents located in the final folder.Info: For content based file up/download please use DataDocument30

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getDocuments_Within_FinalFolder

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_documents_within_reference_folder_by_language(
        self, language: str, order_id: int
    ):
        """
        Deprecated.Please use DataDocument30.getFileList(String, int, int) with Folder Type = 5 insteadfor compatibility reasons with DataDocument30.Returns an instance of StringArrayResult, which contains a list of networkpaths to the reference files, which are connected to a specific language.Info: For content based file up/download please use DataDocument30

        :param language: str
        :param order_id: int

        :return:
        """

        proxy = (
            self.__client.plunet_server.DataOrder30.getDocuments_Within_ReferenceFolder_ByLanguage
        )

        arg = {"language": language, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_documents_within_reference_folder(self, order_id: int):
        """
        Deprecated.Please use DataDocument30.getFileList(String, int, int) with Folder Type = 5 insteadfor compatibility reasons with DataDocument30.Returns an instance of StringArrayResult, which contains a list of networkpaths to the reference files.Info: For content based file up/download please use DataDocument30

        :param order_id: int

        :return:
        """

        proxy = (
            self.__client.plunet_server.DataOrder30.getDocuments_Within_ReferenceFolder
        )

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_documents_within_source_folder_by_language(
        self, language: str, order_id: int
    ):
        """
        Deprecated.Please use DataDocument30.getFileList(String, int, int) with Folder Type = 6 insteadfor compatibility reasons with DataDocument30.Returns an instance of StringArrayResult, which contains a list of networkpaths to source files, connected to a specific language.Info: For content based file up/download please use DataDocument30

        :param language: str
        :param order_id: int

        :return:
        """

        proxy = (
            self.__client.plunet_server.DataOrder30.getDocuments_Within_SourceFolder_ByLanguage
        )

        arg = {"language": language, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_documents_within_source_folder(self, order_id: int):
        """
        Deprecated.Please use DataDocument30.getFileList(String, int, int) with Folder Type = 6 insteadfor compatibility reasons with DataDocument30.Returns an instance of StringArrayResult, which contains a listof network paths to source files.Info: For content based file up/download please use DataDocument30

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getDocuments_Within_SourceFolder

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_en15038_requested(self, order_id: int):
        """
        Method returns an instance of BooleanResult, which contains the information,whether the client requests the EN15038 standard.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getEN15038Requested

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_external_id(self, order_id: int):
        """
        Method returns the ExternalID by orderID

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getExternalID

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_item_status(
        self, source_language: str, target_language: str, order_id: int
    ):
        """
        Method returns the status of a project item associated to a specific language combination.

        :param source_language: str
        :param target_language: str
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getItemStatus

        arg = {
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
            "orderID": order_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_language_combination(self, order_id: int):
        """
        Returns an instance of StringArrayResult which contains a list.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getLanguageCombination

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_links(self, order_id: int, project_type: ProjectType):
        """
        Outputs all incoming and outgoing links for an order.

        :param order_id: int
        :param project_type: ProjectType

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getLinks

        arg = {"orderId": order_id, "projectType": project_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_master_project_id(self, order_id: int):
        """
        Method to get the MasterProjectID of the specified order.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getMasterProjectID

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_order_closing_date(self, order_id: int):
        """
        Method returns an instance of DateResult, which contains the order closing date.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderClosingDate

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_order_confirmations(self, order_id: int):
        """
        Returns an instance of StringArrayResult, which contains a list of relativenetwork paths to all existing order confirmation documents.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderConfirmations

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_order_date(self, order_id: int):
        """
        Get the order date.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderDate

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_order_id(self, display_no: str):
        """
        Method returns an instance of IntegerResult, which contains an order ID.

        :param display_no: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderID

        return self.__client.make_request(proxy, display_no, unpack_dict=False)

    def get_order_no_for_view(self, order_id: int):
        """
        Returns an instance of StringResult, which contains the formatted order number.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderNo_for_View

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_order_object(self, order_id: int):
        """
        Method returns an instance of OrderResult, which contains an instance of Order.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderObject

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_order_object2(self, order_number: str):
        """
        Method returns an instance of OrderResult, which contains an instance of Order.

        :param order_number: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderObject2

        return self.__client.make_request(proxy, order_number, unpack_dict=False)

    def get_order_object_list(self, order_id_list: Union[IntegerList, dict]):
        """
        Method returns an instance of OrderListResult, which contains a list of order objects.

        :param order_id_list: IntegerList

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getOrderObjectList

        if type(order_id_list) != IntegerList:
            order_id_list = IntegerList(**order_id_list).dict()
        else:
            order_id_list = order_id_list.dict()

        return self.__client.make_request(proxy, order_id_list, unpack_dict=False)

    def get_project_category(self, system_language_code: str, order_id: int):
        """
        Get the name (in the language specified) of the project category ofthe order.

        :param system_language_code: str
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectCategory

        arg = {"systemLanguageCode": system_language_code, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_projectmanager_id(self, order_id: int):
        """
        Returns an instance of IntegerResult, which contains the resource id.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectmanagerID

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_project_manager_memo(self, order_id: int):
        """
        Method returns project-manager memo for order by orderID.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectManagerMemo

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_project_name(self, order_id: int):
        """
        Returns an instance of String Result, which contains the project name.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectName

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_project_status(self, order_id: int):
        """
        Returns an instance of IntegerResult, which contains the ArchivStatus.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getProjectStatus

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_property(self, order_id: int, property_name_english: str):
        """
        Deprecated.

        :param order_id: int
        :param property_name_english: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getProperty

        arg = {"orderID": order_id, "propertyNameEnglish": property_name_english}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_rate(self, order_id: int):
        """
        Returns an instance of DoubleResult, which contains the rate.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getRate

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_reference_number(self, order_id: int):
        """
        Method returns the reference number by order ID.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getReferenceNumber

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_request_id(self, order_id: int):
        """
        Returns an instance of IntegerResult, which contains the requestId.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getRequestId

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_subject(self, order_id: int):
        """
        Returns an instance of StringResult, which contains the subject.

        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getSubject

        return self.__client.make_request(proxy, order_id, unpack_dict=False)

    def get_template_list(
        self,
    ):
        """
        Method returns an instance of TemplateListResult, which contains a listof template objects which can be accessed by the user.


        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.getTemplateList

    def insert_by_template(self, order: Union[OrderIN, dict], template_id: int):
        """
        Method to create a order depending on the transfered templateID and OrderIN object.

        :param order: OrderIN
        :param template_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.insert_byTemplate

        if type(order) != OrderIN:
            order = OrderIN(**order).dict()
        else:
            order = order.dict()

        arg = {"order": order, "templateID": template_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def insert(
        self,
    ):
        """
        Method to create a new, empty order.


        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.insert

    def insert2(self, order: Union[OrderIN, dict]):
        """
        Method to create a order depending on the transfered object.

        :param order: OrderIN

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.insert2

        if type(order) != OrderIN:
            order = OrderIN(**order).dict()
        else:
            order = order.dict()

        return self.__client.make_request(proxy, order, unpack_dict=False)

    def register_callback_notify(
        self,
        server_authentication_string: str,
        server_address: str,
        event_type: EventType,
    ):
        """
        Register to get notified when the specified EventType occursfor any order.

        :param server_authentication_string: str
        :param server_address: str
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.registerCallback_Notify

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "EventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def register_callback_observer(
        self, server_authentication_string: str, server_address: str, order_id: int
    ):
        """
        Register to observe a specific object for any supportedEventType.

        :param server_authentication_string: str
        :param server_address: str
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.registerCallback_Observer

        arg = {
            "ServerAuthenticationString": server_authentication_string,
            "ServerAddress": server_address,
            "OrderID": order_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def search(self, search_filter: Union[SearchFilter_Order, dict]):
        """
        Search implementation to filter for any existing order based onspecific criteria.

        :param search_filter: SearchFilter_Order

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.search

        if type(search_filter) != SearchFilter_Order:
            search_filter = SearchFilter_Order(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(proxy, search_filter, unpack_dict=False)

    def set_creation_date(self, creation_date: datetime, order_id: int):
        """
        Sets the creation date for the currently selected project.

        :param creation_date: datetime
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setCreationDate

        arg = {"creationDate": creation_date, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_currency_and_rate(self, order_id: int, currency_iso_code: str, rate: float):
        """
        Method to change the currency and rate for the current project.

        :param order_id: int
        :param currency_iso_code: str
        :param rate: float

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setCurrencyAndRate

        arg = {"orderID": order_id, "currencyIsoCode": currency_iso_code, "rate": rate}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_contact_id(self, customer_contact_id: int, order_id: int):
        """
        Sets the customer contact ID for the currently selected project.

        :param customer_contact_id: int
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setCustomerContactID

        arg = {"customerContactID": customer_contact_id, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_id(self, customer_id: int, order_id: int):
        """
        Sets the customerID for the currently selected project.

        :param customer_id: int
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setCustomerID

        arg = {"customerID": customer_id, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_delivery_deadline(self, delivery_deadline: datetime, order_id: int):
        """
        Sets the delivery deadline for the currently selected project.

        :param delivery_deadline: datetime
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setDeliveryDeadline

        arg = {"deliveryDeadline": delivery_deadline, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_en15038_requested(self, is_en15038: bool, order_id: int):
        """
        Method to mark a project, that the clients wants the project to correspond to the EN 10538 standard.

        :param is_en15038: bool
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setEN15038Requested

        arg = {"isEN15038": is_en15038, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_external_id(self, order_id: int, external_id: str):
        """
        Method set ExternalID of Order by orderID

        :param order_id: int
        :param external_id: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setExternalID

        arg = {"orderID": order_id, "externalID": external_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_master_project_id(self, order_id: int, master_project_id: int):
        """
        Method to set the MasterProjectID of the specified order.

        :param order_id: int
        :param master_project_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setMasterProjectID

        arg = {"orderID": order_id, "MasterProjectID": master_project_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_order_date(self, order_date: datetime, order_id: int):
        """
        Set the order date.

        :param order_date: datetime
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setOrderDate

        arg = {"orderDate": order_date, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_category(
        self, project_category: str, system_language_code: str, order_id: int
    ):
        """
        Set the the project category of the order, specified by its name.

        :param project_category: str
        :param system_language_code: str
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectCategory

        arg = {
            "projectCategory": project_category,
            "systemLanguageCode": system_language_code,
            "orderID": order_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_projectmanager_id(self, resource_id: int, order_id: int):
        """
        Sets the resourceID of the project manager for defined order.

        :param resource_id: int
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectmanagerID

        arg = {"resourceID": resource_id, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_manager_memo(self, order_id: int, memo: str):
        """
        Method set the project-manager Memo for order by orderID.

        :param order_id: int
        :param memo: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectManagerMemo

        arg = {"orderID": order_id, "memo": memo}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_name(self, name: str, order_id: int):
        """
        Sets the project name for the currently selected project.

        :param name: str
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectName

        arg = {"name": name, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_project_status(self, order_id: int, status: int):
        """
        Method allows to set the ArchivStatus to ARCHIVED(3).

        :param order_id: int
        :param status: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setProjectStatus

        arg = {"orderID": order_id, "status": status}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_property(
        self, order_id: int, property_name_english: str, property_value_english: str
    ):
        """
        Deprecated.

        :param order_id: int
        :param property_name_english: str
        :param property_value_english: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setProperty

        arg = {
            "orderID": order_id,
            "propertyNameEnglish": property_name_english,
            "propertyValueEnglish": property_value_english,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_reference_number(self, order_id: int, reference: str):
        """
        Method set reference number for order by orderID.

        :param order_id: int
        :param reference: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setReferenceNumber

        arg = {"orderID": order_id, "reference": reference}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_request_id(self, order_id: int, request_id: int):
        """
        Method to set the project related request ID.

        :param order_id: int
        :param request_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setRequestID

        arg = {"orderID": order_id, "requestID": request_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_subject(self, subject: str, order_id: int):
        """
        Sets the subject for the currently selected project.

        :param subject: str
        :param order_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.setSubject

        arg = {"subject": subject, "orderID": order_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update(self, order: Union[OrderIN, dict], enabled: bool):
        """
        Updates the Order by the transfered object.

        :param order: OrderIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataOrder30.update

        if type(order) != OrderIN:
            order = OrderIN(**order).dict()
        else:
            order = order.dict()

        arg = {"order": order, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
