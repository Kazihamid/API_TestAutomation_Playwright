from apis.base_api import BaseAPI
from config.config import PAYROLL_BASE_URL


class DepartmentAPI(BaseAPI):
    """Test Script 2: create_update_department_programme"""

    def create_or_update_department(self, token, payload):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        return self.post(
            f"{PAYROLL_BASE_URL}rest/services/hr_InteaccHrRestServiceBean/createOrUpdateDepartment",
            headers=headers,
            data=payload,
        )
