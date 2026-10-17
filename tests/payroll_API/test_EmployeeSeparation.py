import allure
import pytest
from apis.payroll_API.create_EmployeeSeparation_API import EmployeeSeparationAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(8)
@allure.feature("Payroll API")
@allure.story("Create employee separation")
def test_create_employee_separation(api_request, payroll_token):
    payload = load_payload("payroll/create_EmployeeSeparation.json")

    response = EmployeeSeparationAPI(api_request).create_employee_separation(payroll_token, payload)

    assert_payroll_success(response)
