# TravelPriceNotifier

Welcome to TravelPriceNotifier, a Python project designed to simplify your travel planning process! This project leverages APIs to fetch real-time travel data and compares ticket prices from London to specified destination cities. If the ticket price is below the threshold set in your Google Sheet, the system notifies registered users via email and SMS.

## Features

- **API Integration:** Fetches real-time travel data using APIs.
- **Google Sheet Integration:** Extracts destination city names and price thresholds from a Google Sheet.
- **Price Comparison:** Compares fetched ticket prices to the set thresholds.
- **Notification System:**
  - **Email Notifications:** Sends email alerts to registered users when prices are below the threshold.
  - **SMS Notifications:** Sends SMS alerts to registered users for immediate notification.
- **User Registration:** Allows users to register for notifications.
- **Customizable Settings:** Users can customize notification preferences.
- **Documentation:** Comprehensive documentation provided for easy setup and usage.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/TravelPriceNotifier.git
