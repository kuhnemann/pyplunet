from typing import Callable, Union

from plunetapi import PlunetAPI

from .services import (
    DataAdmin30,
    DataCustomer30,
    DataCustomerContact30,
    DataDocument30,
    DataItem30,
    DataJob30,
    DataOrder30,
    DataOutgoingInvoice30,
    DataQuote30,
    DataRequest30,
    DataUser30,
    ReportCustomer30,
    ReportJob30,
)

from .exceptions import NoPlunetSession, PlunetAuthFailed, PlunetException


class PlunetClient:
    def __init__(self, base_url=None):
        self.plunet_server = PlunetAPI(base_url=base_url)
        self.uuid = None
        self.document = DataDocument30(self)
        self.user = DataUser30(self)
        self.item = DataItem30(self)
        self.order = DataOrder30(self)
        self.request = DataRequest30(self)
        self.quote = DataQuote30(self)
        self.admin = DataAdmin30(self)
        self.job = DataJob30(self)
        self.customer = DataCustomer30(self)
        self.customer_contact = DataCustomerContact30(self)
        self.outgoing_invoice = DataOutgoingInvoice30(self)
        self.report_customer = ReportCustomer30(self)
        self.report_job = ReportJob30(self)

    def login(self, username, password) -> None:
        uuid = self.plunet_server.PlunetAPI.login(username, password)
        if uuid == "refused":
            raise PlunetAuthFailed("Plunet authentication failed.")
        else:
            self.uuid = uuid

    def logout(self) -> None:
        if self.uuid is not None:
            self.plunet_server.PlunetAPI.logout(self.uuid)
            self.uuid = None
        return

    def make_request(
        self,
        operation_proxy: Callable,
        argument: Union[dict, str, int, list, None],
        unpack_dict: bool = False,
    ):
        if self.uuid is None:
            raise NoPlunetSession("You have no active Plunet session. Please log in.")

        if unpack_dict is True:
            result = operation_proxy(self.uuid, **argument)
        elif argument is not None:
            result = operation_proxy(self.uuid, argument)
        else:
            result = operation_proxy(self.uuid)

        if result.statusCode != 0:
            raise PlunetException(result.statusMessage)
        else:
            try:
                return result.data
            except:
                return result

    def make_download(
        self,
        operation_proxy: Callable,
        argument: Union[dict, str, int, list],
        unpack_dict: bool = False,
    ):
        if self.uuid is None:
            raise NoPlunetSession("You have no active Plunet session. Please log in.")

        if unpack_dict is True:
            result = operation_proxy(self.uuid, **argument)
        else:
            result = operation_proxy(self.uuid, argument)
        if result.statusCode != 0:
            raise Exception(result.statusMessage)
        else:
            try:
                return result.fileContent
            except:
                return result
