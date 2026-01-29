"""
Conversion history and comparison page.
Displays and manages conversion history with comparison features.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import SUPPORTED_CURRENCIES


def initialize_history():
    """Initialize history in session state if not exists."""
    if "conversion_history" not in st.session_state:
        st.session_state.conversion_history = []


def add_to_history(from_currency, to_currency, amount, converted_amount, rate):
    """Add conversion to history."""
    st.session_state.conversion_history.append({
        "Timestamp": datetime.now(),
        "From": from_currency,
        "To": to_currency,
        "Amount": amount,
        "Converted": converted_amount,
        "Rate": rate,
    })


def render_history_page():
    """Render the conversion history page."""
    
    initialize_history()
    
    st.header("📋 Conversion History")
    st.markdown("Track and analyze your conversion history")
    st.markdown("---")
    
    if not st.session_state.conversion_history:
        st.info("📝 No conversions yet. Start converting currencies to build your history!")
        return
    
    # Display history statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Conversions", len(st.session_state.conversion_history))
    
    with col2:
        unique_from = len(set(h["From"] for h in st.session_state.conversion_history))
        st.metric("Unique From Currencies", unique_from)
    
    with col3:
        unique_to = len(set(h["To"] for h in st.session_state.conversion_history))
        st.metric("Unique To Currencies", unique_to)
    
    with col4:
        total_conversions = sum(h["Amount"] for h in st.session_state.conversion_history)
        st.metric("Total Amount Converted", f"{total_conversions:,.2f}")
    
    st.markdown("---")
    
    # Display history table
    st.subheader("Conversion Records")
    
    history_df = pd.DataFrame([
        {
            "Time": h["Timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
            "From": h["From"],
            "To": h["To"],
            "Amount": f"{h['Amount']:,.2f}",
            "Converted": f"{h['Converted']:,.2f}",
            "Rate": f"{h['Rate']:.4f}",
        }
        for h in st.session_state.conversion_history
    ])
    
    st.dataframe(history_df, use_container_width=True, hide_index=True)
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.conversion_history = []
            st.rerun()
    
    with col2:
        csv = history_df.to_csv(index=False)
        st.download_button(
            label="⬇️ Download as CSV",
            data=csv,
            file_name=f"conversion_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )


if __name__ == "__main__":
    render_history_page()
