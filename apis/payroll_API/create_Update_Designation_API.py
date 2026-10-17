from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class DesignationAPI(BaseAPI):
    """Test Script 3: Create or Update Designation"""

    def create_or_update_designation(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createOrUpdateDesignation",
            headers=self.bearer_headers(token),
            data=payload,
        )
