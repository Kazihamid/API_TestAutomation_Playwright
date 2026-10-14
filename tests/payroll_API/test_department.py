import allure
from apis.payroll_API.department_api import DepartmentAPI


@allure.feature("Payroll API")
@allure.story("Create or update department")
def test_create_or_update_department(api_request, payroll_token):
    payload = {
        "code": "0106",
        "name": "Test API0908",
        "funcAreaCode": "01",
    }

    response = DepartmentAPI(api_request).create_or_update_department(payroll_token, payload)

    assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"
