# Stock Prediction Web App

This is a web application for predicting stock prices using Python. The app leverages several libraries including Streamlit, fbprophet, and yfinance to fetch, process, and forecast stock data.

## Modules Used

- **Streamlit**: Used for creating the web application interface.
- **fbprophet**: Used for time series forecasting.
- **yfinance**: Used for fetching historical stock data from Yahoo Finance.

## Installation

Before running the app, make sure you have Python installed on your system. You can install the required modules using pip:

#Usage

Enter Stock Ticker: Provide the stock ticker symbol of the company you want to predict the stock prices for (e.g., AAPL for Apple, MSFT for Microsoft).
Select Date Range: Choose the start and end date for the historical data you want to fetch.
Run Prediction: Click the "Predict" button to fetch the data and run the forecast.
Features
Interactive UI: Easy-to-use interface built with Streamlit.
Real-time Data: Fetches the latest stock data from Yahoo Finance.
Forecast Visualization: Displays the forecasted stock prices using fbprophet.
Example
Here's a quick example of how to use the app:

Open the terminal and navigate to the directory containing app.py.
Run the app using streamlit run app.py.
Enter the stock ticker symbol (e.g., GOOG for Alphabet Inc.).
Select the date range for historical data.
Click on "Predict" to see the forecasted stock prices.

