from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import Order

if TYPE_CHECKING:
    from ..client import PlunetClient


class CallbackOrder30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def receive_notify_callback(
        self, authentication_code: str, order_id: int, event_type: EventType
    ):
        """
        Callback function for notify events registered withDataOrder30.registerCallback_Notify(String, String, String, int).

        :param authentication_code: str
        :param order_id: int
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackOrder30.ReceiveNotifyCallback

        arg = {
            "authenticationCode": authentication_code,
            "OrderID": order_id,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def receive_observer_callback(
        self, authentication_code: str, order: Union[Order, dict], event_type: EventType
    ):
        """
        Callback function for observer events registered withDataOrder30.registerCallback_Observer(String, String, String, int).

        :param authentication_code: str
        :param order: Order
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackOrder30.receiveObserverCallback

        if type(order) != Order:
            order = Order(**order).dict()
        else:
            order = order.dict()

        arg = {
            "authenticationCode": authentication_code,
            "order": order,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
