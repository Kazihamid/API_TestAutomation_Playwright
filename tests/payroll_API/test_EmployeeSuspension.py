import allure
import pytest
from apis.payroll_API.create_EmployeeSuspension_API import EmployeeSuspensionAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(16)
@allure.feature("Payroll API")
@allure.story("Create employee suspension")
def test_create_employee_suspension(api_request, payroll_token):
    payload = load_payload("payroll/create_EmployeeSuspension.json")

    response = EmployeeSuspensionAPI(api_request).create_employee_suspension(payroll_token, payload)

    assert_payroll_success(response)
