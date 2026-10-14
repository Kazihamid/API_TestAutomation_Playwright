import allure
from apis.erp_API.staffsalary_api import StaffSalaryAPI


@allure.feature("ERP API")
@allure.story("Staff salary")
def test_get_staff_salary_information(api_request):
    response = StaffSalaryAPI(api_request).get_staff_salary_info()

    assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"
