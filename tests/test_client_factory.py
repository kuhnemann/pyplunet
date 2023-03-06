from src.pyplunet import PlunetClient
import os
from dotenv import load_dotenv
load_dotenv()
from zeep.cache import SqliteCache, InMemoryCache
from zeep import Transport

def get_test_client() -> PlunetClient:
    pc = PlunetClient(base_url=os.getenv("TEST_URL"))
    pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_client_no_caching() -> PlunetClient:
    pc = PlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False)
    pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_client_inmemory_cache() -> PlunetClient:
    transport = Transport(cache=InMemoryCache())
    pc = PlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False, transport_options={"transport": transport})
    pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc

def get_test_configured_sql_cache() -> PlunetClient:
    cache = SqliteCache(path="test_zeep.db")
    pc = PlunetClient(base_url=os.getenv("TEST_URL"), cache_wsdl=False, transport_options={"cache": cache})
    pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc
