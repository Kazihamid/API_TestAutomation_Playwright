import pytest
import allure
from playwright.sync_api import sync_playwright
from apis.department_api import DepartmentAPI
from utils.auth import get_bearer_token


@allure.feature("With Allure Report")
@allure.story("Test Script 2: Create or Update Department")
@allure.title("Create or update department via bearer token auth")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(2)
def test_create_or_update_department():
    with sync_playwright() as p:
        req = p.request.new_context()

        with allure.step("Get bearer token (Test Script 1)"):
            token = get_bearer_token(req)

        with allure.step("Send POST request to createOrUpdateDepartment"):
            payload = {
                "code": "0106",
                "name": "Test API0908",
                "funcAreaCode": "01",
            }
            allure.attach(
                str(payload),
                name="Request Payload",
                attachment_type=allure.attachment_type.JSON,
            )

            api = DepartmentAPI(req)
            response = api.create_or_update_department(token, payload)

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

        req.dispose()
