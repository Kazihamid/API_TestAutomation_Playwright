import allure
from apis.payroll_API.update_SupervisorChange_API import SupervisorChangeAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@allure.feature("Payroll API")
@allure.story("Update supervisor change")
def test_update_supervisor_change(api_request, payroll_token):
    payload = load_payload("payroll/update_SupervisorChange.json")

    response = SupervisorChangeAPI(api_request).update_supervisor_change(payroll_token, payload)

    assert_payroll_success(response)
