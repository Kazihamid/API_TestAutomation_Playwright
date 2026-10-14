import allure
from apis.erp_API.staffdetail_api import StaffDetailAPI


@allure.feature("ERP API")
@allure.story("Staff detail")
def test_get_staff_detail_information(api_request):
    response = StaffDetailAPI(api_request).get_staff_detail_info()

    assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"
