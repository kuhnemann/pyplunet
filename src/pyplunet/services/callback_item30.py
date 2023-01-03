from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType, ProjectType
from ..models import Item

if TYPE_CHECKING:
    from ..client import PlunetClient


class CallbackItem30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def receive_notify_callback(
        self,
        authentication_code: str,
        item_id: int,
        project_type: ProjectType,
        event_type: EventType,
    ):
        """
        Callback function for notify events registered withDataItem30.registerCallback_Notify(String, String, String, int)Please call/reference to your implementation here.

        :param authentication_code: str
        :param item_id: int
        :param project_type: ProjectType
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackItem30.receiveNotifyCallback

        arg = {
            "authenticationCode": authentication_code,
            "itemID": item_id,
            "projectType": project_type.value,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def receive_observer_callback(
        self, authentication_code: str, item: Union[Item, dict], event_type: EventType
    ):
        """
        Callback function for observer events registered withDataItem30.registerCallback_Observer(String, String, String, int, int)Please call/reference to your implementation here.

        :param authentication_code: str
        :param item: Item
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackItem30.receiveObserverCallback

        if type(item) != Item:
            item = Item(**item).dict()
        else:
            item = item.dict()

        arg = {
            "authenticationCode": authentication_code,
            "item": item,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
