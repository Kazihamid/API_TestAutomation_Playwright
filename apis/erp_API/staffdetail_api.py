import os

from apis.base_api import BaseAPI
from config.config import BASE_URL, API_KEY, API_NAME, STAFF_ID

class StaffDetailAPI(BaseAPI):
    def get_staff_detail_info(self):
       
        headers={
            "x-api-key":API_KEY,
            "api-name":API_NAME,
            "Content-Type":"application/json"
         
        }
        return self.get(f"{BASE_URL}/{API_KEY}/erp.staffdetail/{STAFF_ID}", headers=headers)   
