# Payroll API (Bearer Token) additions — merge instructions

These files are meant to be **merged into** your existing `API_PLAYWRIGHT_FRAMEWORK`
project (they don't replace your ERP-related files).

## 1. Update `.env`
Add the Payroll block from `.env.example` to your real `.env` (values already
match what's in the doc's screenshots):

```
# Payroll-Staging-API
PAYROLL_BASE_URL=https://aponstaging.brac.net/
PAYROLL_USERNAME=inteacc_payroll
PAYROLL_PASSWORD=my_inteacc
PAYROLL_GRANT_USERNAME=api
PAYROLL_GRANT_PASSWORD=123456
```

## 2. Update `config/config.py`
Add the 5 new `PAYROLL_*` variables (see this folder's `config/config.py` —
your existing `STAFF_ID` / `API_KEY_ERP_DATA` lines are untouched).

## 3. Update `apis/base_api.py`
Your current `BaseAPI` only has `.get()`. Both Payroll calls are POST
requests, so a `.post()` method was added — copy it in.

## 4. Add new files (drop in as-is)
- `apis/token_api.py` — `TokenAPI.generate_token()` → Test Script 1
- `apis/department_api.py` — `DepartmentAPI.create_or_update_department()` → Test Script 2
- `utils/auth.py` — `get_bearer_token()` helper: runs Script 1 and returns the
  `access_token` string, so Script 2 (and any future authenticated endpoint)
  can reuse it instead of duplicating token logic in every test.
- `tests/test_token_generation.py`
- `tests/test_department.py`

## Run

```bash
pytest tests/test_token_generation.py tests/test_department.py -v -s
```

## Notes / things to double check against the real API

- The token response is assumed to return JSON with an `access_token` field
  (standard OAuth2 password-grant shape). If the Payroll API names it
  differently, update `utils/auth.py` accordingly.
- `department_api.py` currently hardcodes the same sample payload shown in
  the doc (`code: "0106"`, etc.) inside the test — pull real test data out
  into `payloads/` (you already have that folder) as you add more cases.
- If `oauth2/token` or `createOrUpdateDepartment` return non-200 the first
  time you run this against staging, treat it the same way we debugged the
  ERP endpoint earlier: print `response.text()` and check status
  code/body/headers before assuming the code is wrong.
