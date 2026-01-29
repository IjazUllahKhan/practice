"""
About page with information and documentation.
Provides user guidance and application information.
"""

import streamlit as st


def render_about_page():
    """Render the about page."""
    
    st.header("ℹ️ About This App")
    st.markdown("---")
    
    # Application Info
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Purpose")
        st.markdown("""
        This is a professional Pakistani Currency Converter application built with Streamlit.
        It provides real-time exchange rate information and supports multiple currency conversions.
        """)
    
    with col2:
        st.subheader("📱 Features")
        st.markdown("""
        - **Live Conversion**: Real-time exchange rates
        - **Bulk Converter**: Convert to multiple currencies at once
        - **History Tracking**: Keep track of conversions
        - **Multiple Currencies**: Support for 12+ currencies
        - **Responsive Design**: Works on desktop and mobile
        """)
    
    st.markdown("---")
    
    # Supported Currencies
    st.subheader("💱 Supported Currencies")
    
    currencies_info = {
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
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        for currency, name in list(currencies_info.items())[:4]:
            st.markdown(f"**{currency}** - {name}")
    
    with col2:
        for currency, name in list(currencies_info.items())[4:8]:
            st.markdown(f"**{currency}** - {name}")
    
    with col3:
        for currency, name in list(currencies_info.items())[8:]:
            st.markdown(f"**{currency}** - {name}")
    
    st.markdown("---")
    
    # API Information
    st.subheader("🔌 Data Source")
    st.markdown("""
    Exchange rates are fetched from:
    - **Provider**: ExchangeRate-API.com
    - **Update Frequency**: Real-time (cached for 1 hour)
    - **Accuracy**: Industry-standard rates
    """)
    
    st.markdown("---")
    
    # Best Practices
    st.subheader("✅ Best Practices Implemented")
    
    practices = {
        "Code Organization": [
            "Modular architecture with separation of concerns",
            "Config, Services, Utils, Pages separate modules",
            "Reusable components and functions"
        ],
        "Error Handling": [
            "Comprehensive exception handling",
            "User-friendly error messages",
            "Input validation and sanitization"
        ],
        "Performance": [
            "Streamlit caching with TTL",
            "Efficient API calls",
            "Optimized data structures"
        ],
        "User Experience": [
            "Responsive layout",
            "Clear visual hierarchy",
            "Helpful tooltips and descriptions"
        ]
    }
    
    for category, items in practices.items():
        with st.expander(f"📌 {category}", expanded=False):
            for item in items:
                st.markdown(f"- {item}")
    
    st.markdown("---")
    
    # Footer
    st.subheader("👤 About the Developer")
    st.markdown("""
    This application demonstrates professional Streamlit development practices.
    It serves as an excellent example of:
    - Clean code architecture
    - Best practices for Streamlit applications
    - Proper project structure and organization
    - User-focused design and functionality
    """)
    
    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit | © 2025")


if __name__ == "__main__":
    render_about_page()
