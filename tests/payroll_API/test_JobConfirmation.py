import allure
import pytest
from apis.payroll_API.create_JobConfirmation_API import JobConfirmationAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@pytest.mark.order(11)
@allure.feature("Payroll API")
@allure.story("Create job confirmation")
def test_create_job_confirmation(api_request, payroll_token):
    payload = load_payload("payroll/create_JobConfirmation.json")

    response = JobConfirmationAPI(api_request).create_job_confirmation(payroll_token, payload)

    assert_payroll_success(response)
