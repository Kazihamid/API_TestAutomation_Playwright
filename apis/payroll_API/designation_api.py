from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class DesignationAPI(BaseAPI):
    """Test Script 2: Create or Update Designation"""

    def create_or_update_designation(self, token, payload):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createOrUpdateDesignation",
            headers=headers,
            data=payload,
        )
