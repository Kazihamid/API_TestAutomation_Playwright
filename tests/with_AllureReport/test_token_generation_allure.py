import pytest
import allure
from playwright.sync_api import sync_playwright
from apis.token_api import TokenAPI


@allure.feature("With Allure Report")
@allure.story("Test Script 1: Bearer Token Generation")
@allure.title("Generate bearer token via oauth2/token")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(1)
def test_token_generation():
    with sync_playwright() as p:
        req = p.request.new_context()
        api = TokenAPI(req)

        with allure.step("Send POST request to oauth2/token"):
            response = api.generate_token()

        print(response.status)
        print(response.text())

        with allure.step("Attach response details"):
            allure.attach(
                str(response.status),
                name="Response Status",
                attachment_type=allure.attachment_type.TEXT,
            )
            allure.attach(
                response.text(),
                name="Response Body",
                attachment_type=allure.attachment_type.JSON,
            )

        with allure.step("Verify response status is 200"):
            assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"

        with allure.step("Verify access_token is present in response"):
            body = response.json()
            assert "access_token" in body, f"'access_token' missing in response: {body}"

        req.dispose()
