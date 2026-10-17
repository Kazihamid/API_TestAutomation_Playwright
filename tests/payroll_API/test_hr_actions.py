import allure
import pytest
from apis.payroll_API.hr_service_api import HrServiceAPI
from utils.json_helper import load_json
from validators.response_validator import assert_payroll_success, assert_status

# (test case title, hr_InteaccHrRestServiceBean action) from HRMS_Payroll API sheet.
# Order matters: create_EmployeeSeparation must run before withdraw_EmployeeSeparation.
HR_ACTIONS = [
    ("create_EmployeeProfile", "createEmployeeProfile"),
    ("create_Update_Project", "createOrUpdateSection"),
    # Sheet shows "createEmployeeProf..." here, which looks like a copy-paste slip; confirm with API team
    ("create_Update_OperatingLocation", "createOrUpdateOperatingLocation"),
    ("create_EmployeeTransfer", "createEmployeeTransfer"),
    ("create_EmployeeSeparation", "createEmployeeSeparation"),
    ("create_WorkAwayOfficeInternationalVisit", "createWorkAwayOfficeInternationalVisit"),
    ("create_LeaveApplication", "createLeaveApplication"),
    ("create_JobConfirmation", "createJobConfirmation"),
    ("update_SupervisorChange", "updateSupervisorChange"),
    ("update_EmployeeContractDate", "updateContractDateEmployee"),
    ("withdraw_EmployeeSeparation", "withdrawSeparation"),
    ("create_Update_CostCentre", "createOrUpdateCostCentre"),
]


@pytest.fixture(scope="session")
def hr_service_methods(api_request, payroll_token):
    """{method name: [param names]} as published by the server for hr_InteaccHrRestServiceBean."""
    response = HrServiceAPI(api_request).describe(payroll_token)
    assert_status(response)
    return {m["name"]: [p["name"] for p in m.get("params", [])] for m in response.json()["methods"]}


@allure.feature("Payroll API")
@allure.story("Request body matches service signature")
@pytest.mark.parametrize("title, action", HR_ACTIONS, ids=[title for title, _ in HR_ACTIONS])
def test_hr_payload_matches_signature(hr_service_methods, title, action):
    """Read-only contract check: the server only matches a method when body keys equal its param names."""
    assert action in hr_service_methods, f"Server has no method '{action}'"

    payload = load_json(f"payroll/{title}.json")
    if "_incomplete" in payload:
        pytest.skip(payload["_incomplete"])

    expected = set(hr_service_methods[action])
    actual = set(payload)
    assert actual == expected, (
        f"{action}: missing {sorted(expected - actual)}, unexpected {sorted(actual - expected)}"
    )


@allure.feature("Payroll API")
@pytest.mark.parametrize("title, action", HR_ACTIONS, ids=[title for title, _ in HR_ACTIONS])
def test_hr_action(api_request, payroll_token, title, action):
    allure.dynamic.story(title)

    payload = load_json(f"payroll/{title}.json")
    if "_incomplete" in payload:
        pytest.skip(payload["_incomplete"])

    response = HrServiceAPI(api_request).call(action, payroll_token, payload)

    assert_payroll_success(response)
