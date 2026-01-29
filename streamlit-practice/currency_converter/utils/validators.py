"""
Utility functions for input validation.
Ensures data integrity and proper error handling.
"""


def validate_amount(amount: str) -> tuple[bool, float, str]:
    """
    Validate currency amount input.
    
    Args:
        amount (str): Amount string to validate
        
    Returns:
        tuple: (is_valid, amount_float, error_message)
    """
    try:
        # Strip whitespace
        amount = amount.strip()
        
        if not amount:
            return False, 0, "Amount cannot be empty"
        
        # Convert to float
        amount_float = float(amount)
        
        if amount_float < 0:
            return False, 0, "Amount cannot be negative"
        
        if amount_float == 0:
            return False, 0, "Amount must be greater than 0"
        
        if amount_float > 1e12:  # Prevent unreasonable amounts
            return False, 0, "Amount is too large"
        
        return True, amount_float, ""
        
    except ValueError:
        return False, 0, "Please enter a valid number"


def validate_currency_code(code: str, available_currencies: list) -> tuple[bool, str]:
    """
    Validate currency code.
    
    Args:
        code (str): Currency code to validate
        available_currencies (list): List of available currency codes
        
    Returns:
        tuple: (is_valid, error_message)
    """
    code = code.upper().strip()
    
    if not code:
        return False, "Currency code cannot be empty"
    
    if code not in available_currencies:
        return False, f"Currency '{code}' is not supported"
    
    return True, ""


def validate_exchange_rate_response(response: dict) -> tuple[bool, str]:
    """
    Validate API response structure.
    
    Args:
        response (dict): API response to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not response:
        return False, "Empty response from API"
    
    if "base" not in response or "rates" not in response:
        return False, "Invalid API response structure"
    
    if not isinstance(response["rates"], dict):
        return False, "Invalid rates data format"
    
    return True, ""
