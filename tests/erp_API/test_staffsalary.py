from playwright.sync_api import sync_playwright
from apis.staffinfo_api import StaffInfoAPI
from apis.staffsalary_api import StaffSalaryAPI

def test_get_staff_salary_information():
    with sync_playwright() as p:
        req=p.request.new_context()
        api=StaffSalaryAPI(req)
        response=api.get_staff_salary_info()
        print(response.status)
        assert response.status==200
        req.dispose()
