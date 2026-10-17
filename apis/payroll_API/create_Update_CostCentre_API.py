from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class CostCentreAPI(BaseAPI):
    """Create or Update Cost Centre"""

    def create_or_update_cost_centre(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createOrUpdateCostCentre",
            headers=self.bearer_headers(token),
            data=payload,
        )
