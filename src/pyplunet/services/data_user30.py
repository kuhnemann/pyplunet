from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataUser30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def get_user_by_id(self, user_id: int):
        """
        Returns a UserResult if a user can be founddepending on the transfered user id

        :param user_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataUser30.getUserByID

        return self.__client.make_request(proxy, user_id, unpack_dict=False)

    def get_user_by_login_name(self, user_login_name: str):
        """
        Returns a UserResult if a user can be founddepending on the transfered login-name

        :param user_login_name: str

        :return:
        """

        proxy = self.__client.plunet_server.DataUser30.getUserByLoginName

        return self.__client.make_request(proxy, user_login_name, unpack_dict=False)

    def get_user_list_by_resource_id(self, resource_id: int):
        """
        Returns a List of all resource related user´s

        :param resource_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataUser30.getUserListByResourceID

        return self.__client.make_request(proxy, resource_id, unpack_dict=False)
