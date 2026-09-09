import os
from dotenv import load_dotenv

load_dotenv()

# ERP-Staging-API
BASE_URL = os.getenv("BASE_URL")
API_NAME = os.getenv("API_NAME")
API_KEY = os.getenv("API_KEY")
STAFF_ID = os.getenv("STAFF_ID")
API_KEY_ERP_DATA = os.getenv("API_KEY_ERP_DATA")

# Payroll-Staging-API
PAYROLL_BASE_URL = os.getenv("PAYROLL_BASE_URL")
PAYROLL_USERNAME = os.getenv("PAYROLL_USERNAME")
PAYROLL_PASSWORD = os.getenv("PAYROLL_PASSWORD")
PAYROLL_GRANT_USERNAME = os.getenv("PAYROLL_GRANT_USERNAME")
PAYROLL_GRANT_PASSWORD = os.getenv("PAYROLL_GRANT_PASSWORD")
