import allure
import pytest
from apis.payroll_API.hr_service_api import HrServiceAPI
from utils.json_helper import load_payload
from validators.response_validator import assert_status

# (data file, server action): read-only check that each request body matches
# the parameter names the server publishes for that action
SIGNATURES = [
    ("create_EmployeeProfile", "createEmployeeProfile"),
    ("create_Update_Project", "createOrUpdateSection"),
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
    ("create_EmployeeSuspension", "createEmployeeSuspension"),
]


@pytest.fixture(scope="session")
def hr_service_methods(api_request, payroll_token):
    """{method name: [param names]} as published by the server for hr_InteaccHrRestServiceBean."""
    response = HrServiceAPI(api_request).describe(payroll_token)
    assert_status(response)
    return {m["name"]: [p["name"] for p in m.get("params", [])] for m in response.json()["methods"]}


@allure.feature("Payroll API")
@allure.story("Request body matches service signature")
@pytest.mark.parametrize("data, action", SIGNATURES, ids=[data for data, _ in SIGNATURES])
def test_payload_matches_signature(hr_service_methods, data, action):
    assert action in hr_service_methods, f"Server has no method '{action}'"

    payload = load_payload(f"payroll/{data}.json")

    expected = set(hr_service_methods[action])
    actual = set(payload)
    assert actual == expected, (
        f"{action}: missing {sorted(expected - actual)}, unexpected {sorted(actual - expected)}"
    )
