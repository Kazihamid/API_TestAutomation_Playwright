import pytest
from config.config import BASE_URL, API_KEY, API_NAME


@pytest.fixture(autouse=True)
def require_erp_config():
    if not all([BASE_URL, API_KEY, API_NAME]):
        pytest.skip("ERP settings (BASE_URL, API_KEY, API_NAME) not set in .env")
