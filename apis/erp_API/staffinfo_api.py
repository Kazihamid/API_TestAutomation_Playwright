from apis.base_api import BaseAPI
from config.config import BASE_URL,API_KEY,API_NAME

class StaffInfoAPI(BaseAPI):
    def get_staff_info(self):
        headers={
            "x-api-key": API_KEY,
            "api-name": API_NAME,
            "Content-Type": "application/json"
        }
        return self.get(f"{BASE_URL}/{API_KEY}/dbo.staffinfo", headers=headers)
