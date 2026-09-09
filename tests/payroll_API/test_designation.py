import pytest, allure
from playwright.sync_api import sync_playwright
from apis.department_api import DepartmentAPI
from apis.payroll_API.designation_api import DesignationAPI
from utils.auth import get_bearer_token

@pytest.mark.order(3)
# For 'Features by Stories' view we can use feature and story:
@allure.feature("Login & Download Excel Sheet")
@allure.story("Verify Login and Excel Download")

def test_create_or_update_designation():
    with sync_playwright() as p:
        req = p.request.new_context()

        # Step 1: get bearer token (Test Script 1)
        token = get_bearer_token(req)

        # Step 2: create/update designation using the token (Test Script 2)
        payload = {
            "code": "D5693",
            "name": "QA_Test_Designation",
        }

        api = DesignationAPI(req)
        response = api.create_or_update_designation(token, payload)

        print(response.status)
        print(response.text())

        assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"

        req.dispose()
