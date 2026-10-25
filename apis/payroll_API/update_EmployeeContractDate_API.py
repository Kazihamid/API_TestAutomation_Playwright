from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class EmployeeContractDateAPI(BaseAPI):
    """Update Employee Contract Date"""

    def update_employee_contract_date(self, token, payload):
        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/updateContractDateEmployee",
            headers=self.bearer_headers(token),
            data=payload,
        )
