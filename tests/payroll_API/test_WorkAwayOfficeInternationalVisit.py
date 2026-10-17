import allure
from apis.payroll_API.create_WorkAwayOfficeInternationalVisit_API import WorkAwayOfficeInternationalVisitAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_payroll_success


@allure.feature("Payroll API")
@allure.story("Create work away office international visit")
def test_create_work_away_office_international_visit(api_request, payroll_token):
    payload = load_payload("payroll/create_WorkAwayOfficeInternationalVisit.json")

    response = WorkAwayOfficeInternationalVisitAPI(api_request).create_work_away_office_international_visit(payroll_token, payload)

    assert_payroll_success(response)
