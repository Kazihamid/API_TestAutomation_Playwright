from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class WithdrawEmployeeSeparationAPI(BaseAPI):
    """Withdraw Employee Separation"""

    def withdraw_employee_separation(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/withdrawSeparation",
            headers=self.bearer_headers(token),
            data=payload,
        )
