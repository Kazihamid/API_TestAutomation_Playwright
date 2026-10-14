import allure
from apis.erp_API.staffsalary_api import StaffSalaryAPI
from validators.response_validator import get_erp_rows


@allure.feature("ERP API")
@allure.story("Staff salary")
def test_get_staff_salary_information(api_request):
    response = StaffSalaryAPI(api_request).get_staff_salary_info()

    rows = get_erp_rows(response, required_keys=["PIN", "Allowance", "AllowanceName", "GrossSalary"])
    for row in rows:
        assert isinstance(row["GrossSalary"], (int, float)), f"Non-numeric GrossSalary for PIN {row['PIN']}"
