import allure
from apis.payroll_API.token_api import TokenAPI


@allure.feature("Payroll API")
@allure.story("Bearer token generation")
def test_token_generation(api_request):
    response = TokenAPI(api_request).generate_token()

    assert response.status == 200, f"Expected 200, got {response.status}: {response.text()}"

    body = response.json()
    assert "access_token" in body, f"'access_token' missing in response: {body}"
