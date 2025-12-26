# ✈️ Flight Deal Tracker

A Python-based automated flight deal monitoring system that tracks flight prices from Google Sheets, searches for the cheapest available flights, and sends email notifications to subscribers when prices drop below target thresholds.

## 📋 Overview

This application integrates with the Amadeus Flight API and Google Sheets (via Sheety API) to automatically monitor flight deals. When a flight is found below your specified price threshold, the system sends notifications via email and optionally SMS through Twilio.

## ✨ Features

- **Automated Price Monitoring**: Continuously checks flight prices against your target prices stored in Google Sheets
- **IATA Code Resolution**: Automatically fetches and updates airport codes for cities in your watchlist
- **Smart Flight Search**: Searches for both direct and connecting flights to find the best deals
- **Multi-Channel Notifications**: Sends alerts via email and SMS when deals are found
- **Customer Management**: Manages subscriber email lists from Google Sheets
- **Flexible Search Parameters**: Configurable search options including departure dates, number of stops, and currency

## 🛠️ Technologies Used

- **Python 3.x**
- **Amadeus Flight API** - Flight search and pricing data
- **Sheety API** - Google Sheets integration for data management
- **Twilio API** - SMS notifications
- **SMTP (Gmail)** - Email notifications

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- Gmail account (for email notifications)
- Twilio account (for SMS notifications)
- Amadeus API credentials
- Sheety API access

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd flight-deal-tracker
```

2. Install required dependencies:
```bash
pip install requests twilio
```

3. Create an `API` directory and a `creds.py` file with your credentials:
```python
# API/creds.py
SHETTY_APP_USERNAME = "your_sheety_username"
SHETTY_APP_TOKEN1 = "your_sheety_token"
FLIGHT_API_KEY = "your_amadeus_api_key"
FLIGHT_API_SECRET = "your_amadeus_api_secret"
account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"
EMAIL = "your_email@gmail.com"
PASSWORD = "your_gmail_app_password"
```

4. Set up your Google Sheet with the following structure:

**Prices Sheet:**

| city  | iataCode | lowestPrice | id |
|-------|----------|-------------|----|
| Paris | CDG      | 50          | 2  |
| Tokyo | NRT      | 500         | 3  |

**Users Sheet:**

| firstName | lastName | emailAddress         | id |
|-----------|----------|----------------------|----|
| John      | Doe      | john@example.com     | 1  |

## 🚀 Usage

Run the main script:
```bash
python main.py
```

The application will:
1. Fetch your target cities and prices from Google Sheets
2. Retrieve subscriber email addresses
3. Automatically populate missing IATA codes
4. Search for flight deals from London (LON) to each destination
5. Send notifications when prices are below your thresholds

### Configuration

**Origin Airport**: Default is set to "LON" (London). Modify in `main.py`:
```python
origin_city_code = "LON"  # Change to your preferred departure city
```

**Search Window**: Default searches for tomorrow's flights. Adjust in `main.py`:
```python
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
```

**Flight Preferences**: Configure direct vs. connecting flights in the search parameters.

## 📁 Project Structure

```
flight-deal-tracker/
│
├── main.py                    # Main application entry point
├── data_manager.py            # Google Sheets API integration
├── flight_search.py           # Amadeus Flight API handler
├── flight_data.py             # Flight data models and processing
├── notification_manager.py    # Email and SMS notification handler
└── API/
    └── creds.py              # API credentials (not in repo)
```

## 🔧 Module Documentation

### DataManager (`data_manager.py`)
Handles all Google Sheets operations via Sheety API.

**Methods:**
- `get_message()`: Retrieves flight price data from the sheet
- `get_customer_emails()`: Fetches subscriber email list
- `put_data(json_payload, obj_id)`: Updates sheet records

### FlightSearch (`flight_search.py`)
Manages Amadeus API interactions for flight searches.

**Methods:**
- `get_new_token()`: Obtains OAuth2 authentication token
- `get_iata_code(city_name)`: Retrieves IATA airport code for a city
- `get_flight_data(origin, destination, date, is_direct)`: Searches for available flights

### FlightData (`flight_data.py`)
Processes and structures flight information.

**Functions:**
- `find_cheapest_flight(data)`: Parses API response and identifies the lowest-priced flight

**Class:**
- `FlightData`: Data model for storing flight details (price, origin, destination, date, stops)

### NotificationManager (`notification_manager.py`)
Sends notifications through multiple channels.

**Methods:**
- `send_notification()`: Sends SMS via Twilio
- `send_emails(customer_email)`: Sends email alerts to all subscribers

## 📧 Email Configuration

For Gmail, you'll need to use an App Password:
1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password at https://myaccount.google.com/apppasswords
3. Use this password in your `creds.py` file

## ⚠️ Important Notes

- **Rate Limiting**: The application includes a 2-second delay between requests to avoid API rate limits
- **API Costs**: Amadeus API has usage limits on free tier; monitor your usage
- **Security**: Never commit your `creds.py` file to version control
- **Gmail Limits**: Gmail has daily sending limits; adjust subscriber count accordingly

## 🐛 Troubleshooting

**No flights found:**
- Check if IATA codes are correctly populated
- Verify date format and search parameters
- Ensure API credentials are valid

**Authentication errors:**
- Regenerate API tokens
- Check token expiration times
- Verify all credentials in `creds.py`

**Email not sending:**
- Confirm Gmail App Password is correct
- Check Gmail security settings
- Verify SMTP port 587 is not blocked

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Amadeus for Developers](https://developers.amadeus.com/) - Flight API
- [Sheety](https://sheety.co/) - Google Sheets API integration
- [Twilio](https://www.twilio.com/) - SMS notifications

## 📞 Support

For questions or issues, please open an issue in the repository.

---

## 🎓 Learning Project

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp** on Udemy by Dr. Angela Yu. It demonstrates practical application of Python programming concepts including:

- **API Integration**: Working with REST ful APIs (Amadeus, Sheety, Twilio)
- **OAuth2 Authentication**: Implementing token-based authentication
- **Data Management**: CRUD operations with external data sources
- **Error Handling**: Managing API responses and exceptions
- **Object-Oriented Programming**: Structuring code with classes and methods
- **Email Automation**: SMTP protocol and email sending
- **SMS Integration**: Third-party service integration with Twilio
- **Environment Management**: Secure credential handling
- **Data Processing**: JSON parsing and data transformation
- **Datetime Operations**: Working with dates and time calculations

This project consolidates multiple concepts taught throughout the bootcamp into a real-world application that solves a practical problem: finding and tracking flight deals automatically.

---

**Note**: This application is designed for personal use and educational purposes. Ensure compliance with all API terms of service and usage limits.