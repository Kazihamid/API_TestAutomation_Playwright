import allure
from apis.payroll_API.withdraw_EmployeeSeparation_API import WithdrawEmployeeSeparationAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@allure.feature("Payroll API")
@allure.story("Withdraw employee separation")
def test_withdraw_employee_separation(api_request, payroll_token):
    payload = load_payload("payroll/withdraw_EmployeeSeparation.json")

    response = WithdrawEmployeeSeparationAPI(api_request).withdraw_employee_separation(payroll_token, payload)

    assert_payroll_success(response)
