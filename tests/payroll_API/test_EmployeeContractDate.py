import allure
import pytest
from apis.payroll_API.update_EmployeeContractDate_API import EmployeeContractDateAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(13)
@allure.feature("Payroll API")
@allure.story("Update employee contract date")
def test_update_employee_contract_date(api_request, payroll_token):
    payload = load_payload("payroll/update_EmployeeContractDate.json")

    response = EmployeeContractDateAPI(api_request).update_employee_contract_date(payroll_token, payload)

    assert_payroll_success(response)
