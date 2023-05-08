import logging
from typing import Callable, Optional, Union

from plunetapi import PlunetAPI
from zeep.helpers import serialize_object

from .exceptions import (
    PLUNET_ERRORS,
    NoPlunetSession,
    PlunetAuthFailed,
    PlunetClientError,
)
from .models import BooleanResult, StringResult
from .services import (
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

logger = logging.getLogger(__name__)


class PlunetClient:
    """
    Client for interacting with a Plunet instance. Initialized with the base url
    of the instance. Session needs a UUID, which either can be supplied in initialization
    or be obtained using the login() method.

    :param base_url: URL for a Plunet instance
    :type base_url: str
    :param uuid: Optional session UUID
    :type uuid: str, optional
    :param cache_wsdl: Boolean to turn on/off the zeep CachingClient
    :type cache_wsdl: bool
    :param transport_options: Dictionary with transport options that are passed to plunetapi and the underlying zeep client
    :type transport_options: dict, optional
    """

    def __init__(
        self,
        base_url,
        uuid: Optional[str] = None,
        cache_wsdl: bool = True,
        transport_options: Optional[dict] = None,
    ):
        self.plunet_server = PlunetAPI(
            base_url=base_url, cache_wsdl=cache_wsdl, options=transport_options
        )
        self.uuid = uuid
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

    def get_plunet_version(self) -> StringResult:
        result = self.plunet_server.PlunetAPI.getPlunetVersion()
        if result.statusCode != 0:
            raise PLUNET_ERRORS.get(
                result.statusCode,
                PlunetClientError(
                    f"Error calling Plunet (could not map status code to error type). Result: {result}"
                ),
            )
        else:
            try:
                return StringResult(**serialize_object(result))
            except Exception:
                raise PlunetClientError(f"Unable to parse result: {result}")

    def validate(self, username: str, password: str) -> BooleanResult:
        """
        Will return BooleanResult if credentials validated are correct,
        and throw InvalidCredentials error if not.
        :param username:
        :param password:
        :return:
        """
        operation_proxy = self.plunet_server.PlunetAPI.validate
        response_model = BooleanResult
        argument = {"Username": username, "Password": password}
        return self.make_request(
            operation_proxy, argument, response_model, unpack_dict=True
        )

    def get_version(self) -> float:
        return self.plunet_server.PlunetAPI.getVersion()

    def make_request(
        self,
        operation_proxy: Callable,
        argument: Union[dict, str, int, list, None],
        response_model: Callable,
        unpack_dict: bool = False,
    ):
        if self.uuid is None:
            raise NoPlunetSession("You have no active Plunet session. Please log in.")

        if unpack_dict is True and argument is not None:
            result = operation_proxy(self.uuid, **argument)
        elif unpack_dict is False and argument is not None:
            result = operation_proxy(self.uuid, argument)
        else:
            result = operation_proxy(self.uuid)

        if result.statusCode != 0:
            raise PLUNET_ERRORS.get(
                result.statusCode,
                PlunetClientError(
                    f"Error calling Plunet (could not map status code to error type). Result: {result}"
                ),
            )
        else:
            try:
                return response_model(**serialize_object(result))
            except Exception:
                raise PlunetClientError(f"Unable to parse result: {result}")
