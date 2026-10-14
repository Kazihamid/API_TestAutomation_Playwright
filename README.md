# API Test Automation (Playwright + pytest)

API tests for the ERP and Payroll staging services, built on Playwright's
`APIRequestContext` and pytest, with Allure reporting.

## Layout

```
apis/            API client classes (one per endpoint group)
  base_api.py      shared GET/POST + bearer header helper
  erp_API/         ERP staff endpoints (x-api-key auth)
  payroll_API/     Payroll endpoints (OAuth2 bearer token)
config/config.py loads settings from .env
conftest.py      session fixtures: api_request, payroll_token
tests/           pytest tests, mirroring apis/
utils/auth.py    get_bearer_token() helper
```

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # then fill in the values
```

## Run

```bash
pytest -v                          # all tests
pytest tests/payroll_API -v        # one suite
allure serve reports/allure-results
```

## Fixtures

- `api_request`: one Playwright request context for the whole session.
- `payroll_token`: Payroll bearer token, generated once and reused by every
  Payroll test. Request it as a test argument; no ordering is needed.
