# Pakistani Currency Converter 💱

A professional, feature-rich currency converter application built with Streamlit. Optimized for Pakistani rupee conversions with support for multiple currencies worldwide.

## Features ✨

- **Real-time Exchange Rates**: Live currency conversion using ExchangeRate-API
- **Single & Bulk Conversion**: Convert one amount or multiple currencies at once
- **Conversion History**: Track your conversions with timestamps and export options
- **Multiple Currencies**: Support for 12+ major currencies including PKR, USD, EUR, GBP, AED, SAR, INR, and more
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Performance Optimized**: Smart caching reduces API calls and improves speed
- **Professional UI**: Clean, intuitive interface with helpful tooltips

## Project Structure 📁

```
currency_converter/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── config/
│   └── settings.py            # Configuration and constants
│
├── services/
│   └── exchange_rate_service.py  # API integration and business logic
│
├── utils/
│   ├── formatters.py          # Display formatting utilities
│   └── validators.py          # Input validation functions
│
└── pages/
    ├── converter.py           # Main converter page
    ├── bulk_converter.py      # Bulk conversion page
    ├── history.py             # Conversion history page
    └── about.py               # About and information page
```

## Installation 🚀

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory**

```bash
cd currency_converter
```

2. **Create a virtual environment (recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
streamlit run app.py
```

5. **Access the app**
   The app will open in your default browser at `http://localhost:8501`

## Usage 📖

### Currency Converter

1. Select source and target currencies
2. Enter the amount to convert
3. View instant conversion results with exchange rates

### Bulk Converter

1. Enter amount and select source currency
2. Check multiple target currencies
3. Click "Convert" to see all conversions in a table
4. Download results as CSV if needed

### Conversion History

1. All conversions are logged automatically
2. View statistics and conversion records
3. Download history as CSV
4. Clear history when needed

### About Page

- Learn about supported currencies
- View implemented best practices
- Access API information

## Configuration ⚙️

Edit `config/settings.py` to customize:

- API endpoints and timeouts
- Supported currencies
- UI preferences
- Cache duration
- Display formats

### Environment Variables (Optional)

Create a `.env` file in the project root:

```
EXCHANGERATE_API_KEY=your_api_key_here
LOG_LEVEL=INFO
```

## Best Practices Implemented ✅

### Code Organization

- **Modular Architecture**: Separation of concerns with config, services, utils, and pages
- **Reusable Components**: DRY principles throughout the codebase
- **Clear Naming**: Descriptive function and variable names
- **Type Hints**: Python type annotations for better code clarity

### Error Handling

- Comprehensive exception handling for API calls
- User-friendly error messages
- Input validation for all user inputs
- Graceful degradation on failures

### Performance

- **Streamlit Caching**: TTL-based caching reduces redundant API calls
- **Efficient Conversions**: Optimized currency conversion logic
- **Resource Management**: Proper cleanup and state management

### User Experience

- **Responsive Layout**: Adapts to different screen sizes
- **Visual Hierarchy**: Clear sections and meaningful icons
- **Helpful Information**: Tooltips and descriptions throughout
- **Accessibility**: Easy-to-read colors and text

### Security

- Input validation and sanitization
- Safe API integration
- No sensitive data in logs
- Environment variable usage for configuration

## Supported Currencies 💱

| Code | Currency          | Region       |
| ---- | ----------------- | ------------ |
| PKR  | Pakistani Rupee   | Pakistan     |
| USD  | US Dollar         | USA          |
| EUR  | Euro              | Europe       |
| GBP  | British Pound     | UK           |
| AED  | UAE Dirham        | UAE          |
| SAR  | Saudi Riyal       | Saudi Arabia |
| INR  | Indian Rupee      | India        |
| CAD  | Canadian Dollar   | Canada       |
| AUD  | Australian Dollar | Australia    |
| CNY  | Chinese Yuan      | China        |
| JPY  | Japanese Yen      | Japan        |
| BDT  | Bangladeshi Taka  | Bangladesh   |

## API Information 🔌

- **Provider**: ExchangeRate-API.com
- **Update Frequency**: Real-time (cached for 1 hour)
- **Free Tier**: 1,500 requests/month
- **Accuracy**: ±1% (industry standard)

## Dependencies 📦

- **streamlit** (1.28.1) - Web application framework
- **requests** (2.31.0) - HTTP client library
- **python-dotenv** (1.0.0) - Environment variable management
- **pandas** (2.1.1) - Data manipulation and analysis

## Troubleshooting 🔧

### "API request timeout"

- Check your internet connection
- Verify API endpoint is accessible
- Increase timeout in settings.py

### "Currency not found"

- Ensure currency code is in SUPPORTED_CURRENCIES
- Check for typos in currency selection
- Verify API data format

### "Conversion returns zero"

- Ensure amount is greater than 0
- Check that currency pair is supported
- Verify exchange rates are loaded

## Development 🛠️

### Adding New Currencies

1. Add to `SUPPORTED_CURRENCIES` in `config/settings.py`
2. Add symbol in `formatters.py` if needed
3. Restart the app

### Customizing Appearance

- Modify settings in `config/settings.py`
- Update colors in CSS sections
- Adjust layout in individual page files

### Adding Features

1. Create new service in `services/` if needed
2. Add utility functions in `utils/`
3. Create new page in `pages/`
4. Update navigation in `app.py`

## Performance Tips ⚡

- Cache API responses appropriately
- Limit currency selections for bulk conversion
- Close unused browser tabs
- Use modern browsers for best performance

## Future Enhancements 🚀

- [ ] Historical exchange rate charts
- [ ] Favorite currency pairs
- [ ] Multi-language support
- [ ] Offline mode
- [ ] Mobile app version
- [ ] Cryptocurrency support
- [ ] Scheduled conversion alerts

## License 📄

This project is provided as-is for educational and practical use.

## Support 📞

For issues, feature requests, or suggestions:

- Check existing documentation
- Review error messages carefully
- Verify API status
- Check internet connection

## Credits 🙏

Built with:

- **Streamlit**: Amazing framework for data apps
- **ExchangeRate-API**: Reliable exchange rate data
- **Python Community**: Great libraries and tools

---

**Made with ❤️ for currency conversion enthusiasts**

_Last Updated: January 2025_
