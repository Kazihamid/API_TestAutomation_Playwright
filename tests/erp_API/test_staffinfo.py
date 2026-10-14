import allure
import pytest
from apis.erp_API.staffinfo_api import StaffInfoAPI


@allure.feature("ERP API")
@allure.story("Staff info")
@pytest.mark.xfail(reason="API key lacks access: 'Table or procedure call dbo.staffinfo is not allowed'", strict=True)
def test_get_staff_information(api_request):
    response = StaffInfoAPI(api_request).get_staff_info()

    assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"
