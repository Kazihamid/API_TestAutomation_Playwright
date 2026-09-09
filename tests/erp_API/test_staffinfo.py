from playwright.sync_api import sync_playwright
from apis.staffinfo_api import StaffInfoAPI

def test_get_staff_information():
    with sync_playwright() as p:
        req=p.request.new_context()
        api=StaffInfoAPI(req)
        response=api.get_staff_info()
        print(response.status)
        assert response.status==200
        req.dispose()
