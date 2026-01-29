"""
Utility functions for formatting and displaying data.
Handles currency formatting, number formatting, and display utilities.
"""

from config.settings import DECIMAL_PLACES, THOUSAND_SEPARATOR


def format_currency(amount: float, currency_code: str, currency_name: str = None) -> str:
    """
    Format amount with currency formatting.
    
    Args:
        amount (float): Amount to format
        currency_code (str): Currency code (e.g., 'USD', 'PKR')
        currency_name (str): Full currency name (optional)
        
    Returns:
        str: Formatted currency string
    """
    if amount is None:
        return "N/A"
    
    # Format number with thousand separator
    if THOUSAND_SEPARATOR:
        formatted_amount = f"{amount:,.{DECIMAL_PLACES}f}"
    else:
        formatted_amount = f"{amount:.{DECIMAL_PLACES}f}"
    
    return f"{currency_code} {formatted_amount}"


def format_exchange_rate(rate: float, from_currency: str, to_currency: str) -> str:
    """
    Format exchange rate for display.
    
    Args:
        rate (float): Exchange rate
        from_currency (str): Source currency code
        to_currency (str): Target currency code
        
    Returns:
        str: Formatted exchange rate string
    """
    if rate is None:
        return "N/A"
    
    return f"1 {from_currency} = {rate:.{DECIMAL_PLACES}f} {to_currency}"


def format_timestamp(timestamp: str) -> str:
    """
    Format timestamp for display.
    
    Args:
        timestamp (str): ISO format timestamp
        
    Returns:
        str: Formatted timestamp string
    """
    try:
        from datetime import datetime
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "Unknown"


def get_currency_symbol(currency_code: str) -> str:
    """
    Get currency symbol for display.
    
    Args:
        currency_code (str): Currency code
        
    Returns:
        str: Currency symbol
    """
    symbols = {
        "PKR": "₨",
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "AED": "د.إ",
        "SAR": "﷼",
        "INR": "₹",
        "CAD": "C$",
        "AUD": "A$",
        "CNY": "¥",
        "JPY": "¥",
        "BDT": "৳",
    }
    return symbols.get(currency_code, currency_code)
