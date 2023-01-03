from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import Request

if TYPE_CHECKING:
    from ..client import PlunetClient


class CallbackRequest30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def receive_notify_callback(
        self, authentication_code: str, request_id: int, event_type: EventType
    ):
        """
        Callback function for notify events registered withDataRequest30.registerCallback_Notify(String, String, String, int).

        :param authentication_code: str
        :param request_id: int
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackRequest30.ReceiveNotifyCallback

        arg = {
            "authenticationCode": authentication_code,
            "RequestID": request_id,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def receive_observer_callback(
        self,
        authentication_code: str,
        request: Union[Request, dict],
        event_type: EventType,
    ):
        """
        Callback function for observer events registered withDataRequest30.registerCallback_Observer(String, String, String, int).

        :param authentication_code: str
        :param request: Request
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackRequest30.receiveObserverCallback

        if type(request) != Request:
            request = Request(**request).dict()
        else:
            request = request.dict()

        arg = {
            "authenticationCode": authentication_code,
            "request": request,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
