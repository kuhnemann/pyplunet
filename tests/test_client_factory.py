from src.pyplunet import PlunetClient
import os
from

def get_test_client() -> PlunetClient:
    pc = PlunetClient(base_url=os.getenv("TEST_URL"))
    pc.login(os.getenv("TEST_USER"), os.getenv("TEST_PW"))
    return pc