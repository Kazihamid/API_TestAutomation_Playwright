from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class JobConfirmationAPI(BaseAPI):
    """Create Job Confirmation"""

    def create_job_confirmation(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createJobConfirmation",
            headers=self.bearer_headers(token),
            data=payload,
        )
