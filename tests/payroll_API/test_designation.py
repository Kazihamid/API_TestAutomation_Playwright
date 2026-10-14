import allure
from apis.payroll_API.designation_api import DesignationAPI


@allure.feature("Payroll API")
@allure.story("Create or update designation")
def test_create_or_update_designation(api_request, payroll_token):
    payload = {
        "code": "D5693",
        "name": "QA_Test_Designation",
    }

    response = DesignationAPI(api_request).create_or_update_designation(payroll_token, payload)

    assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"
