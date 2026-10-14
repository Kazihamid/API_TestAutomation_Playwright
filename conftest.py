import pytest
from playwright.sync_api import sync_playwright

from utils.auth import get_bearer_token


@pytest.fixture(scope="session")
def api_request():
    """One Playwright APIRequestContext shared by the whole test session."""
    with sync_playwright() as p:
        context = p.request.new_context()
        yield context
        context.dispose()


@pytest.fixture(scope="session")
def payroll_token(api_request):
    """Bearer token for the Payroll API, generated once per session."""
    return get_bearer_token(api_request)
