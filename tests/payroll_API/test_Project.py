import allure
import pytest
from apis.payroll_API.create_Update_Project_API import ProjectAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(5)
@allure.feature("Payroll API")
@allure.story("Create or update project (section)")
def test_create_or_update_project(api_request, payroll_token):
    payload = load_payload("payroll/create_Update_Project.json")

    response = ProjectAPI(api_request).create_or_update_project(payroll_token, payload)

    assert_payroll_success(response)
