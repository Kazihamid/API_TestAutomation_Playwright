import allure
from apis.erp_API.staffdetail_api import StaffDetailAPI
from config.config import STAFF_ID
from validators.response_validator import get_erp_rows


@allure.feature("ERP API")
@allure.story("Staff detail")
def test_get_staff_detail_information(api_request):
    response = StaffDetailAPI(api_request).get_staff_detail_info()

    rows = get_erp_rows(response, required_keys=["PIN", "UserName"])
    assert len(rows) == 1, f"Expected 1 staff record, got {len(rows)}"
    # API zero-pads PINs to 8 digits; STAFF_ID in .env may not be padded
    assert rows[0]["PIN"].lstrip("0") == STAFF_ID.lstrip("0"), "Returned PIN does not match STAFF_ID"
