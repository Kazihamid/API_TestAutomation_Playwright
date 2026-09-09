import pytest, allure
from playwright.sync_api import sync_playwright
from apis.token_api import TokenAPI

@pytest.mark.order(1)
# For 'Features by Stories' view we can use feature and story:
@allure.feature("Login & Download Excel Sheet")
@allure.story("Verify Login and Excel Download")

def test_token_generation():
    with sync_playwright() as p:
        req = p.request.new_context()
        api = TokenAPI(req)
        response = api.generate_token()

        print(response.status)
        print(response.text())

        assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"

        body = response.json()
        assert "access_token" in body, f"'access_token' missing in response: {body}"

        req.dispose()
