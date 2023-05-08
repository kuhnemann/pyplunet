from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..models import UserListResult, UserResult

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataUser30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def get_user_by_login_name(self, user_login_name: str) -> UserResult:
        """
        Returns a UserResult if a user can be found
        depending on the transfered login-name


        :param user_login_name: str
        :return: UserResult
        """

        proxy = self.__client.plunet_server.DataUser30.getUserByLoginName
        response_model = UserResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=user_login_name,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_user_list_by_resource_id(self, resource_id: int) -> UserListResult:
        """
        Returns a List of all resource related userÂ´s


        :param resource_id: int
        :return: UserListResult
        """

        proxy = self.__client.plunet_server.DataUser30.getUserListByResourceID
        response_model = UserListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=resource_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_user_by_id(self, user_id: int) -> UserResult:
        """
        Returns a UserResult if a user can be found
        depending on the transfered user id


        :param user_id: int
        :return: UserResult
        """

        proxy = self.__client.plunet_server.DataUser30.getUserByID
        response_model = UserResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=user_id,
            response_model=response_model,
            unpack_dict=False,
        )
