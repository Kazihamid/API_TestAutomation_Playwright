from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class WorkAwayOfficeInternationalVisitAPI(BaseAPI):
    """Create Work Away Office International Visit"""

    def create_work_away_office_international_visit(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createWorkAwayOfficeInternationalVisit",
            headers=self.bearer_headers(token),
            data=payload,
        )
