"""
Configuration settings for the currency converter application.
Follows best practices for environment management and constants.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
API_KEY = os.getenv("EXCHANGERATE_API_KEY", "free")  # Using free tier endpoint
API_BASE_URL = "https://api.exchangerate-api.com/v4/latest"
API_TIMEOUT = 10

# Supported Currencies with Pakistani Rupee focus
PRIMARY_CURRENCY = "PKR"
SUPPORTED_CURRENCIES = {
    "PKR": "Pakistani Rupee",
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "AED": "UAE Dirham",
    "SAR": "Saudi Riyal",
    "INR": "Indian Rupee",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar",
    "CNY": "Chinese Yuan",
    "JPY": "Japanese Yen",
    "BDT": "Bangladeshi Taka",
}

# UI Configuration
APP_TITLE = "Pakistani Currency Converter"
APP_ICON = "💱"
PAGE_ICON = "💱"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Cache Configuration
CACHE_DURATION = 3600  # 1 hour in seconds

# Display Configuration
DECIMAL_PLACES = 2
THOUSAND_SEPARATOR = True

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
