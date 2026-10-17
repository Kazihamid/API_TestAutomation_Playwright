import allure
import pytest
from apis.payroll_API.create_Update_OperatingLocation_API import OperatingLocationAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(6)
@allure.feature("Payroll API")
@allure.story("Create or update operating location")
def test_create_or_update_operating_location(api_request, payroll_token):
    payload = load_payload("payroll/create_Update_OperatingLocation.json")

    response = OperatingLocationAPI(api_request).create_or_update_operating_location(payroll_token, payload)

    assert_payroll_success(response)
