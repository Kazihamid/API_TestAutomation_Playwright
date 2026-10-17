from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class HrServiceAPI(BaseAPI):
    """Generic client for actions on hr_InteaccHrRestServiceBean (all POST + Bearer token)."""

    def call(self, action, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/{action}",
            headers=self.bearer_headers(token),
            data=payload,
        )

    def describe(self, token):
        """Lists the service's methods and their parameter names."""
        return self.get(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean",
            headers={"Authorization": f"Bearer {token}"},
        )
