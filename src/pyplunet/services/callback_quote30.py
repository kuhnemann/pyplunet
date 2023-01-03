from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType
from ..models import Quote

if TYPE_CHECKING:
    from ..client import PlunetClient


class CallbackQuote30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def receive_notify_callback(
        self, authentication_code: str, quote_id: int, event_type: EventType
    ):
        """
        Callback function for notify events registered withDataQuote30.registerCallback_Notify(String, String, String, int).

        :param authentication_code: str
        :param quote_id: int
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackQuote30.ReceiveNotifyCallback

        arg = {
            "authenticationCode": authentication_code,
            "QuoteID": quote_id,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def receive_observer_callback(
        self, authentication_code: str, quote: Union[Quote, dict], event_type: EventType
    ):
        """
        Callback function for observer events registered withDataQuote30.registerCallback_Observer(String, String, String, int).

        :param authentication_code: str
        :param quote: Quote
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackQuote30.receiveObserverCallback

        if type(quote) != Quote:
            quote = Quote(**quote).dict()
        else:
            quote = quote.dict()

        arg = {
            "authenticationCode": authentication_code,
            "quote": quote,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
