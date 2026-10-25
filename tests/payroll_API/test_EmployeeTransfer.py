import allure
import pytest
from apis.payroll_API.create_EmployeeTransfer_API import EmployeeTransferAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(7)
@allure.feature("Payroll API")
@allure.story("Create employee transfer")
def test_create_employee_transfer(api_request, payroll_token):
    payload = load_payload("payroll/create_EmployeeTransfer.json")

    response = EmployeeTransferAPI(api_request).create_employee_transfer(payroll_token, payload)

    assert_payroll_success(response)
