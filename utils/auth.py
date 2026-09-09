from apis.token_api import TokenAPI


def get_bearer_token(request_context):
    """
    Runs Test Script 1 (token generation) and returns the access_token
    so it can be reused as the Bearer token in subsequent requests.
    """
    token_api = TokenAPI(request_context)
    response = token_api.generate_token()

    assert response.status == 200, (
        f"Token generation failed: {response.status} - {response.text()}"
    )

    body = response.json()
    token = body.get("access_token")
    assert token, f"'access_token' missing in token response: {body}"

    return token
