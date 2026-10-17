import allure
import pytest
from apis.payroll_API.designation_api import DesignationAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(3)
@allure.feature("Payroll API")
@allure.story("Create or update designation")
def test_create_or_update_designation(api_request, payroll_token):
    payload = load_payload("payroll/create_Update_Designation.json")

    response = DesignationAPI(api_request).create_or_update_designation(payroll_token, payload)

    body = assert_payroll_success(response)
    assert "Designation" in body["message"], f"Unexpected message: {body}"
