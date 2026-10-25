from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class EmployeeProfileAPI(BaseAPI):
    """Create Employee Profile"""

    def create_employee_profile(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createEmployeeProfile",
            headers=self.bearer_headers(token),
            data=payload,
        )
