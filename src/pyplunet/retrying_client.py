import logging
from typing import Callable, Union

from requests.exceptions import ConnectionError as RequestsConnectionError

from .client import PlunetClient

try:
    import tenacity
except ImportError:
    print(
        "You need to install 'tenacity' to use the RetryingPlunetClient. Install using 'pip install tenacity' and try again!"
    )
    raise ImportError(
        "You need to install 'tenacity' to use the RetryingPlunetClient. Install using 'pip install tenacity' and try again!"
    )


logger = logging.getLogger(__name__)


class RetryingPlunetClient(PlunetClient):
    """
    Retrying Client for interacting with a Plunet instance
    Will use tenacity to retry 10 times with jitter on requests.exceptions.ConnectionError.


    :param base_url: URL for a Plunet instance
    :type base_url: str
    :param uuid: Optional session UUID
    :type uuid: str, optional
    :param cache_wsdl: Boolean to turn on/off the zeep CachingClient
    :type cache_wsdl: bool
    :param transport_options: Dictionary with transport options that are passed to plunetapi and the underlying zeep client
    :type transport_options: dict, optional
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @tenacity.retry(
        wait=tenacity.wait_random_exponential(multiplier=1, max=60),
        retry=tenacity.retry_if_exception_type(RequestsConnectionError),
        stop=tenacity.stop_after_attempt(10),
        reraise=True,
        after=tenacity.after_log(logger, logging.DEBUG),
    )
    def make_request(
        self,
        operation_proxy: Callable,
        argument: Union[dict, str, int, list, None],
        response_model: Callable,
        unpack_dict: bool = False,
    ):
        return super().make_request(
            operation_proxy, argument, response_model, unpack_dict
        )
