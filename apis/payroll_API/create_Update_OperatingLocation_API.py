from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class OperatingLocationAPI(BaseAPI):
    """Create or Update Office (Operating Location)"""

    def create_or_update_operating_location(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createOrUpdateOperatingLocation",
            headers=self.bearer_headers(token),
            data=payload,
        )
