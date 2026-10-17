import allure
from apis.payroll_API.create_Update_CostCentre_API import CostCentreAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@allure.feature("Payroll API")
@allure.story("Create or update cost centre")
def test_create_or_update_cost_centre(api_request, payroll_token):
    payload = load_payload("payroll/create_Update_CostCentre.json")

    response = CostCentreAPI(api_request).create_or_update_cost_centre(payroll_token, payload)

    assert_payroll_success(response)
