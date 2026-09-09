import base64
from apis.base_api import BaseAPI
from config.config import (
    PAYROLL_BASE_URL,
    PAYROLL_USERNAME,
    PAYROLL_PASSWORD,
    PAYROLL_GRANT_USERNAME,
    PAYROLL_GRANT_PASSWORD,
)


class TokenAPI(BaseAPI):
    """Test Script 1: Bearer Token_Generation"""

    def generate_token(self):
        credentials = f"{PAYROLL_USERNAME}:{PAYROLL_PASSWORD}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        form_data = {
            "grant_type": "password",
            "username": PAYROLL_GRANT_USERNAME,
            "password": PAYROLL_GRANT_PASSWORD,
            "authentication_methods": "client_secret_basic",
        }

        return self.post(f"{PAYROLL_BASE_URL}oauth2/token", headers=headers, form=form_data)
