from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class SupervisorChangeAPI(BaseAPI):
    """Update Supervisor Change"""

    def update_supervisor_change(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/updateSupervisorChange",
            headers=self.bearer_headers(token),
            data=payload,
        )
