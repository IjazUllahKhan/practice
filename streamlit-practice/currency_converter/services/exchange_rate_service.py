"""
Service module for fetching exchange rate data from external APIs.
Implements error handling and caching for better performance.
"""

import requests
import streamlit as st
from datetime import datetime
from typing import Dict, Optional
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import API_BASE_URL, API_TIMEOUT, CACHE_DURATION


class ExchangeRateService:
    """Service class for handling exchange rate operations."""
    
    @staticmethod
    @st.cache_data(ttl=CACHE_DURATION)
    def get_exchange_rates(base_currency: str) -> Optional[Dict]:
        """
        Fetch exchange rates for a given base currency.
        
        Args:
            base_currency (str): The base currency code (e.g., 'USD', 'PKR')
            
        Returns:
            Optional[Dict]: Dictionary containing exchange rates or None if request fails
        """
        try:
            url = f"{API_BASE_URL}/{base_currency}"
            response = requests.get(url, timeout=API_TIMEOUT)
            response.raise_for_status()
            
            data = response.json()
            
            if response.status_code == 200 and "rates" in data:
                return {
                    "base": data.get("base"),
                    "rates": data.get("rates"),
                    "timestamp": datetime.now().isoformat()
                }
            return None
            
        except requests.exceptions.Timeout:
            st.error(f"⏱️ Request timeout. Please try again.")
            return None
        except requests.exceptions.ConnectionError:
            st.error(f"🌐 Connection error. Please check your internet connection.")
            return None
        except requests.exceptions.HTTPError as e:
            st.error(f"❌ API Error: {e.response.status_code} - {e.response.reason}")
            return None
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error fetching exchange rates: {str(e)}")
            return None
        except ValueError:
            st.error("❌ Invalid response from API. Please try again.")
            return None
    
    @staticmethod
    def convert_currency(
        amount: float,
        from_currency: str,
        to_currency: str,
        rates: Dict
    ) -> Optional[float]:
        """
        Convert amount from one currency to another.
        
        Args:
            amount (float): Amount to convert
            from_currency (str): Source currency code
            to_currency (str): Target currency code
            rates (Dict): Dictionary containing exchange rates
            
        Returns:
            Optional[float]: Converted amount or None if conversion fails
        """
        try:
            if from_currency == to_currency:
                return amount

            # Ensure response structure is valid
            if not isinstance(rates, dict) or "rates" not in rates:
                return None

            rate_map = rates.get("rates", {})

            # Check both currencies exist in the rates map
            if to_currency not in rate_map or from_currency not in rate_map:
                # It's possible from_currency equals the declared base
                # so allow conversion when from_currency == base
                if from_currency != rates.get("base"):
                    return None

            if from_currency == rates.get("base"):
                # Direct conversion from base currency
                converted = amount * rate_map[to_currency]
            else:
                # Convert to base first, then to target
                base_amount = amount / rate_map[from_currency]
                converted = base_amount * rate_map[to_currency]
            
            return round(converted, 2)
            
        except (KeyError, ZeroDivisionError, TypeError):
            return None
