from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import EventType, ProjectType
from ..models import Job

if TYPE_CHECKING:
    from ..client import PlunetClient


class CallbackJob30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def receive_notify_callback(
        self,
        authentication_code: str,
        job_id: int,
        project_type: ProjectType,
        event_type: EventType,
    ):
        """
        Callback function for notify events registered withDataJob30.registerCallback_Notify(String, String, String, int).

        :param authentication_code: str
        :param job_id: int
        :param project_type: ProjectType
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackJob30.ReceiveNotifyCallback

        arg = {
            "authenticationCode": authentication_code,
            "jobID": job_id,
            "projectType": project_type.value,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def receive_observer_callback(
        self, authentication_code: str, job: Union[Job, dict], event_type: EventType
    ):
        """
        Callback function for observer events registered withDataJob30.registerCallback_Observer(String, String, String, int, int).

        :param authentication_code: str
        :param job: Job
        :param event_type: EventType

        :return:
        """

        proxy = self.__client.plunet_server.CallbackJob30.receiveObserverCallback

        if type(job) != Job:
            job = Job(**job).dict()
        else:
            job = job.dict()

        arg = {
            "authenticationCode": authentication_code,
            "job": job,
            "eventType": event_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)
