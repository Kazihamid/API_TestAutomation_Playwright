from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class EmployeeSuspensionAPI(BaseAPI):
    """Create Employee Suspension"""

    def create_employee_suspension(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createEmployeeSuspension",
            headers=self.bearer_headers(token),
            data=payload,
        )
