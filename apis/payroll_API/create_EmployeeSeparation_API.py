from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class EmployeeSeparationAPI(BaseAPI):
    """Create Employee Separation"""

    def create_employee_separation(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createEmployeeSeparation",
            headers=self.bearer_headers(token),
            data=payload,
        )
