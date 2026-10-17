from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class HrServiceAPI(BaseAPI):
    """Service metadata for hr_InteaccHrRestServiceBean (used by the signature check)."""

    def describe(self, token):
        """Lists the service's methods and their parameter names."""
        return self.get(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean",
            headers={"Authorization": f"Bearer {token}"},
        )
