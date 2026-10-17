from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class LeaveApplicationAPI(BaseAPI):
    """Create Leave Application for Higher Study Leave"""

    def create_leave_application(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createLeaveApplication",
            headers=self.bearer_headers(token),
            data=payload,
        )
