"""
Main currency converter page.
Provides the core functionality for currency conversion.
"""

import streamlit as st
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import SUPPORTED_CURRENCIES
from services.exchange_rate_service import ExchangeRateService
from utils.formatters import format_currency, format_exchange_rate, format_timestamp
from utils.validators import validate_amount, validate_currency_code


def render_converter_page():
    """Render the main currency converter page."""
    
    st.header("💱 Currency Converter")
    st.markdown("---")
    
    # Create two columns for input layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("From")
        from_currency = st.selectbox(
            "Select source currency",
            options=list(SUPPORTED_CURRENCIES.keys()),
            format_func=lambda x: f"{x} - {SUPPORTED_CURRENCIES[x]}",
            key="from_currency"
        )
        amount = st.number_input(
            "Enter amount",
            min_value=0.0,
            value=1.0,
            step=1.0,
            key="amount_input"
        )
    
    with col2:
        st.subheader("To")
        to_currency = st.selectbox(
            "Select target currency",
            options=list(SUPPORTED_CURRENCIES.keys()),
            index=1,  # Default to USD
            format_func=lambda x: f"{x} - {SUPPORTED_CURRENCIES[x]}",
            key="to_currency"
        )
        st.text_input(
            "Converted amount",
            value="0.00",
            disabled=True,
            key="converted_amount_display"
        )
    
    # Perform conversion
    if amount > 0:
        with st.spinner("Fetching exchange rates..."):
            exchange_data = ExchangeRateService.get_exchange_rates(from_currency)
        
        if exchange_data:
            # Perform conversion
            converted_amount = ExchangeRateService.convert_currency(
                amount,
                from_currency,
                to_currency,
                exchange_data
            )
            
            if converted_amount is not None:
                # Display results
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        "From Amount",
                        format_currency(amount, from_currency),
                    )
                
                with col2:
                    st.metric(
                        "Arrow",
                        "→",
                        label_visibility="collapsed"
                    )
                
                with col3:
                    st.metric(
                        "To Amount",
                        format_currency(converted_amount, to_currency),
                    )
                
                # Display exchange rate
                exchange_rate = exchange_data["rates"].get(to_currency)
                if exchange_rate:
                    st.info(
                        f"📊 Exchange Rate: {format_exchange_rate(exchange_rate, from_currency, to_currency)}"
                    )
                
                # Display last update time
                st.caption(
                    f"Last updated: {format_timestamp(exchange_data['timestamp'])}"
                )
            else:
                st.error("❌ Unable to convert. Please try again.")
        else:
            st.error("❌ Failed to fetch exchange rates.")


if __name__ == "__main__":
    render_converter_page()
