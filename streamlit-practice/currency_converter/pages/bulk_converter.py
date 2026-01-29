"""
Bulk currency converter page.
Allows conversion from one currency to multiple currencies at once.
"""

import streamlit as st
import pandas as pd
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import SUPPORTED_CURRENCIES
from services.exchange_rate_service import ExchangeRateService
from utils.formatters import format_currency


def render_bulk_converter_page():
    """Render the bulk currency converter page."""
    
    st.header("📊 Bulk Converter")
    st.markdown("Convert one amount to multiple currencies at once")
    st.markdown("---")
    
    # Input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        amount = st.number_input(
            "Enter amount to convert",
            min_value=0.0,
            value=1000.0,
            step=1.0,
        )
    
    with col2:
        from_currency = st.selectbox(
            "From currency",
            options=list(SUPPORTED_CURRENCIES.keys()),
            format_func=lambda x: f"{x} - {SUPPORTED_CURRENCIES[x]}",
        )
    
    # Select target currencies
    st.subheader("Select target currencies")
    currencies_col1, currencies_col2 = st.columns(2)
    
    selected_currencies = []
    
    with currencies_col1:
        for i, currency in enumerate(list(SUPPORTED_CURRENCIES.keys())):
            if i % 2 == 0:
                if st.checkbox(
                    f"{currency} - {SUPPORTED_CURRENCIES[currency]}",
                    value=(currency != from_currency),
                    key=f"currency_{currency}"
                ):
                    selected_currencies.append(currency)
    
    with currencies_col2:
        for i, currency in enumerate(list(SUPPORTED_CURRENCIES.keys())):
            if i % 2 == 1:
                if st.checkbox(
                    f"{currency} - {SUPPORTED_CURRENCIES[currency]}",
                    value=(currency != from_currency),
                    key=f"currency_{currency}"
                ):
                    selected_currencies.append(currency)
    
    # Convert and display results
    if amount > 0 and selected_currencies:
        if st.button("🔄 Convert to Selected Currencies", use_container_width=True):
            with st.spinner("Fetching exchange rates and converting..."):
                exchange_data = ExchangeRateService.get_exchange_rates(from_currency)
            
            if exchange_data:
                # Prepare data for table
                conversion_results = []
                
                for target_currency in selected_currencies:
                    converted_amount = ExchangeRateService.convert_currency(
                        amount,
                        from_currency,
                        target_currency,
                        exchange_data
                    )
                    
                    if converted_amount is not None:
                        exchange_rate = exchange_data["rates"].get(target_currency)
                        conversion_results.append({
                            "Currency": f"{target_currency} ({SUPPORTED_CURRENCIES[target_currency]})",
                            "Amount": f"{converted_amount:,.2f}",
                            "Exchange Rate": f"1 {from_currency} = {exchange_rate:.4f}",
                        })
                
                if conversion_results:
                    # Display results table
                    st.subheader("Conversion Results")
                    df = pd.DataFrame(conversion_results)
                    st.dataframe(df, use_container_width=True, hide_index=True)
                    
                    # Summary
                    st.success(f"✅ Successfully converted {amount} {from_currency} to {len(conversion_results)} currencies")
                else:
                    st.error("❌ Unable to convert to selected currencies.")
            else:
                st.error("❌ Failed to fetch exchange rates.")
    elif selected_currencies:
        st.info("👆 Enter an amount and click 'Convert' to see results")


if __name__ == "__main__":
    render_bulk_converter_page()
