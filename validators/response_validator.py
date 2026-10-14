import json


def assert_status(response, expected=200):
    assert response.status == expected, (
        f"Expected {expected}, got {response.status}: {response.text()}"
    )


def assert_payroll_success(response):
    """Payroll returns HTTP 200 even on failure; the real outcome is in body.valid / body.code."""
    assert_status(response)
    payload = response.json()
    body = payload.get("body") or {}
    assert payload.get("status") == "OK", f"Unexpected status: {payload}"
    assert body.get("valid") is True, f"Request not valid: {payload}"
    assert body.get("code") == "SUCCESS", f"Unexpected code: {payload}"
    return body


def get_erp_rows(response, required_keys):
    """ERP returns a JSON array with Content-Type text/plain, so parse the text ourselves."""
    assert_status(response)
    rows = json.loads(response.text())
    assert isinstance(rows, list) and rows, f"Expected a non-empty list, got: {response.text()[:200]}"
    missing = set(required_keys) - rows[0].keys()
    assert not missing, f"Missing fields {sorted(missing)} in first row"
    return rows
