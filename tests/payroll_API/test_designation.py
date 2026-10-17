import allure
import pytest
from apis.payroll_API.designation_api import DesignationAPI
from validators.response_validator import assert_payroll_success


@pytest.mark.order(3)
@allure.feature("Payroll API")
@allure.story("Create or update designation")
def test_create_or_update_designation(api_request, payroll_token):
    payload = {
        "code": "D5693",
        "name": "QA_Test_Designation",
    }

    response = DesignationAPI(api_request).create_or_update_designation(payroll_token, payload)

    body = assert_payroll_success(response)
    assert "Designation" in body["message"], f"Unexpected message: {body}"
