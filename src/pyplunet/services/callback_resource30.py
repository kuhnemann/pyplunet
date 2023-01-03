from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import Resource

if TYPE_CHECKING:
    from ..client import PlunetClient


class CallbackResource30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def receive_notify_callback(
        self, authentication_code: str, resource_id: int, event_type: EventType
    ):
        """
        Callback function for notify events registered withDataResource30.registerCallback_Notify(String, String, String, int).

        :param authentication_code: str
        :param resource_id: int
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackResource30.receiveNotifyCallback

        arg = {
            "authenticationCode": authentication_code,
            "resourceID": resource_id,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def receive_observer_callback(
        self,
        authentication_code: str,
        resource: Union[Resource, dict],
        event_type: EventType,
    ):
        """
        Callback function for observer events registered withDataResource30.registerCallback_Observer(String, String, String, int).

        :param authentication_code: str
        :param resource: Resource
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackResource30.receiveObserverCallback

        if type(resource) != Resource:
            resource = Resource(**resource).dict()
        else:
            resource = resource.dict()

        arg = {
            "authenticationCode": authentication_code,
            "resource": resource,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
