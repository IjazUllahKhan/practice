"""
Main application entry point for Pakistani Currency Converter.
Follows Streamlit best practices with multi-page configuration.
"""

import streamlit as st
import sys
import os

# Configure page
st.set_page_config(
    page_title="Pakistani Currency Converter",
    page_icon="💱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://streamlit.io",
        "Report a Bug": "https://github.com",
        "About": "Pakistani Currency Converter v1.0"
    }
)

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.settings import APP_TITLE, APP_ICON
from pages import converter, bulk_converter, history, about


def main():
    """Main application entry point."""
    
    # Sidebar navigation
    st.sidebar.title(f"{APP_ICON} {APP_TITLE}")
    st.sidebar.markdown("---")
    
    # Navigation menu
    # Note: the `icons` parameter is not supported in all Streamlit versions.
    # Remove it for maximum compatibility; emoji can be included inside labels if needed.
    page = st.sidebar.radio(
        "Select Page",
        options=["Converter", "Bulk Converter", "History", "About"],
        help="Choose a page to navigate"
    )
    
    st.sidebar.markdown("---")
    
    # Sidebar info
    st.sidebar.info(
        """
        **Pakistani Currency Converter**
        
        A professional currency converter application built with Streamlit.
        
        Features:
        - Real-time exchange rates
        - Multiple currency support
        - Conversion history tracking
        - Bulk conversion
        """
    )
    
    # Page routing
    if page == "Converter":
        converter.render_converter_page()
    elif page == "Bulk Converter":
        bulk_converter.render_bulk_converter_page()
    elif page == "History":
        history.render_history_page()
    elif page == "About":
        about.render_about_page()
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption("💱 Currency Converter")
    with col2:
        st.caption("Built with Streamlit")
    with col3:
        st.caption("2025")


if __name__ == "__main__":
    main()
