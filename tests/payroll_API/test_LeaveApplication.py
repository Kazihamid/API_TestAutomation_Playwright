import allure
from apis.payroll_API.create_LeaveApplication_API import LeaveApplicationAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@allure.feature("Payroll API")
@allure.story("Create leave application")
def test_create_leave_application(api_request, payroll_token):
    payload = load_payload("payroll/create_LeaveApplication.json")

    response = LeaveApplicationAPI(api_request).create_leave_application(payroll_token, payload)

    assert_payroll_success(response)
