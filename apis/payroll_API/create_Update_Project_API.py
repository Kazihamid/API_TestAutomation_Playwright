from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class ProjectAPI(BaseAPI):
    """Create or Update Project (Section)"""

    def create_or_update_project(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createOrUpdateSection",
            headers=self.bearer_headers(token),
            data=payload,
        )
