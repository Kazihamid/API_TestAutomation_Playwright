from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class EmployeeTransferAPI(BaseAPI):
    """Create Employee Transfer"""

    def create_employee_transfer(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createEmployeeTransfer",
            headers=self.bearer_headers(token),
            data=payload,
        )
