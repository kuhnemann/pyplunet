from typing import Callable, Union

from plunetapi import PlunetAPI

from .exceptions import NoPlunetSession, PlunetAuthFailed, PlunetException
from .services import (
    CallbackCustomer30,
    CallbackItem30,
    CallbackJob30,
    CallbackOrder30,
    CallbackQuote30,
    CallbackRequest30,
    CallbackResource30,
    DataAdmin30,
    DataCreditNote30,
    DataCustomer30,
    DataCustomerAddress30,
    DataCustomerContact30,
    DataCustomFields30,
    DataDocument30,
    DataItem30,
    DataJob30,
    DataJobRound30,
    DataOrder30,
    DataOutgoingInvoice30,
    DataPayable30,
    DataQuote30,
    DataRequest30,
    DataResource30,
    DataResourceAddress30,
    DataResourceContact30,
    DataUser30,
    ReportCustomer30,
    ReportJob30,
    RequestDocText30,
)


class PlunetClient:
    def __init__(self, base_url=None):
        self.plunet_server = PlunetAPI(base_url=base_url)
        self.uuid = None
        self.payable = DataPayable30(self)
        self.resource_contact = DataResourceContact30(self)
        self.customer_address = DataCustomerAddress30(self)
        self.resource_address = DataResourceAddress30(self)
        self.resource = DataResource30(self)
        self.credit_note = DataCreditNote30(self)
        self.job_round = DataJobRound30(self)
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
        self.custom_fields = DataCustomFields30(self)
        self.outgoing_invoice = DataOutgoingInvoice30(self)
        self.report_customer = ReportCustomer30(self)
        self.report_job = ReportJob30(self)
        self.request_doc_text = RequestDocText30(self)
        self.callback_item = CallbackItem30(self)
        self.callback_quote = CallbackQuote30(self)
        self.callback_order = CallbackOrder30(self)
        self.callback_request = CallbackRequest30(self)
        self.callback_resource = CallbackResource30(self)
        self.callback_customer = CallbackCustomer30(self)
        self.callback_job = CallbackJob30(self)

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
                return

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
