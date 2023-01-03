from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import Customer

if TYPE_CHECKING:
    from ..client import PlunetClient


class CallbackCustomer30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def receive_notify_callback(
        self, authentication_code: str, customer_id: int, event_type: EventType
    ):
        """
        Callback function for notify events registered withDataCustomer30.registerCallback_Notify(String, String, String, int)Please call/reference to your implementation here.

        :param authentication_code: str
        :param customer_id: int
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackCustomer30.receiveNotifyCallback

        arg = {
            "authenticationCode": authentication_code,
            "customerID": customer_id,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def receive_observer_callback(
        self,
        authentication_code: str,
        customer: Union[Customer, dict],
        event_type: EventType,
    ):
        """
        Callback function for observer events registered withDataCustomer30.registerCallback_Observer(String, String, String, int)Please call/reference to your implementation here.

        :param authentication_code: str
        :param customer: Customer
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackCustomer30.receiveObserverCallback

        if type(customer) != Customer:
            customer = Customer(**customer).dict()
        else:
            customer = customer.dict()

        arg = {
            "authenticationCode": authentication_code,
            "customer": customer,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
