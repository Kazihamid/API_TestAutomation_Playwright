import allure
import pytest
from apis.payroll_API.token_api import TokenAPI
from validators.response_validator import assert_status


@pytest.mark.order(1)
@allure.feature("Payroll API")
@allure.story("Bearer token generation")
def test_token_generation(api_request):
    response = TokenAPI(api_request).generate_token()

    assert_status(response)
    body = response.json()
    assert body.get("access_token"), f"'access_token' missing or empty in response: {body}"
    assert body.get("token_type", "").lower() == "bearer", f"Unexpected token_type: {body.get('token_type')}"
