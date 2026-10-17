import allure
import pytest
from apis.payroll_API.department_api import DepartmentAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(2)
@allure.feature("Payroll API")
@allure.story("Create or update department")
def test_create_or_update_department(api_request, payroll_token):
    payload = load_payload("payroll/create_Update_Department.json")

    response = DepartmentAPI(api_request).create_or_update_department(payroll_token, payload)

    body = assert_payroll_success(response)
    assert "Department" in body["message"], f"Unexpected message: {body}"
