import allure
import pytest
from apis.erp_API.staffinfo_api import StaffInfoAPI
from validators.response_validator import assert_status


@allure.feature("ERP API")
@allure.story("Staff info")
@pytest.mark.xfail(reason="API key lacks access: 'Table or procedure call dbo.staffinfo is not allowed'", strict=True)
def test_get_staff_information(api_request):
    response = StaffInfoAPI(api_request).get_staff_info()

    assert_status(response)
