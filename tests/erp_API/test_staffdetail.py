from playwright.sync_api import sync_playwright
from apis.staffdetail_api import StaffDetailAPI
from apis.staffinfo_api import StaffInfoAPI
from apis.staffsalary_api import StaffSalaryAPI

def test_get_staff_detail_information():
    with sync_playwright() as p:
        req=p.request.new_context()
        api=StaffDetailAPI(req)
        response=api.get_staff_detail_info()
        print(response.status)
        print(response.text())  # full body, not truncated
        assert response.status==200, f"Expected 200, got {response.status}: {response.text()}" # That last line means when it fails again, your pytest output will show you the actual error message instead of just the status code — much faster to diagnose.
        req.dispose()   