from src.pyplunet import PlunetClient, RetryingPlunetClient
import os
from dotenv import load_dotenv
load_dotenv()
from zeep.cache import SqliteCache, InMemoryCache
from zeep import Transport

def get_test_client(logged_in: bool = True) -> PlunetClient:
    pc = PlunetClient(base_url=os.getenv("TEST_URL"))
    if logged_in:
        pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_client_no_caching(logged_in: bool = True) -> PlunetClient:
    pc = PlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False)
    if logged_in:
        pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_client_inmemory_cache(logged_in: bool = True) -> PlunetClient:
    transport = Transport(cache=InMemoryCache())
    pc = PlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False, transport_options={"transport": transport})
    if logged_in:
        pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_configured_sql_cache(logged_in: bool = True) -> PlunetClient:
    cache = SqliteCache(path="test_zeep.db")
    pc = PlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False, transport_options={"cache": cache})
    if logged_in:
        pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_retrying_client(logged_in: bool = True) -> PlunetClient:
    pc = RetryingPlunetClient(base_url=os.getenv("TEST_URL"))
    if logged_in:
        pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_retrying_client_no_caching(logged_in: bool = True) -> PlunetClient:
    pc = RetryingPlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False)
    if logged_in:
        pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_retrying_client_inmemory_cache(logged_in: bool = True) -> PlunetClient:
    transport = Transport(cache=InMemoryCache())
    pc = RetryingPlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False, transport_options={"transport": transport})
    if logged_in:
        pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_retrying_configured_sql_cache(logged_in: bool = True) -> PlunetClient:
    cache = SqliteCache(path="test_zeep.db")
    pc = RetryingPlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False, transport_options={"cache": cache})
    if logged_in:
        pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc
