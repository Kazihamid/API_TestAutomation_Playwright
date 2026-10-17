import allure
from apis.payroll_API.create_EmployeeProfile_API import EmployeeProfileAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@allure.feature("Payroll API")
@allure.story("Create employee profile")
def test_create_employee_profile(api_request, payroll_token):
    payload = load_payload("payroll/create_EmployeeProfile.json")

    response = EmployeeProfileAPI(api_request).create_employee_profile(payroll_token, payload)

    assert_payroll_success(response)
