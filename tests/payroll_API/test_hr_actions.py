import allure
import pytest
from apis.payroll_API.hr_service_api import HrServiceAPI
from utils.json_helper import load_json
from validators.response_validator import assert_payroll_success

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


@allure.feature("Payroll API")
@pytest.mark.parametrize("title, action", HR_ACTIONS, ids=[title for title, _ in HR_ACTIONS])
def test_hr_action(api_request, payroll_token, title, action):
    allure.dynamic.story(title)

    payload = load_json(f"payroll/{title}.json")
    if "_incomplete" in payload:
        pytest.skip(payload["_incomplete"])

    response = HrServiceAPI(api_request).call(action, payroll_token, payload)

    assert_payroll_success(response)
