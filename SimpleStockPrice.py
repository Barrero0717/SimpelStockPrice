import yfinance as yf
import streamlit as st
import pandas as pd

# For this script, I use VOO, but you can use other ticker, like GOOGl, for Google, or AAPL, for Apple.


st.write(
    """
# Simple Stock Price App
### Show are the stock *closing price* and *volume* of VOO! (Vanguard S&P 500 ETF)

The Vanguard S&P 500 ETF (VOO) is a fund that invests in the stocks of some of the largest companies in the United States. VOO is an exchange-traded fund (ETF) that tracks the S&P 500 index by owning all of the equities within the S&P 500. The S&P 500's investment return is considered a gauge of the overall U.S. stock market.
    """
)

# Define the ticker symbol
tickerSymbol = 'VOO'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices of this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-03-20')

# Chart the stock price at the end of that day/month/year
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

# Chart how many shares were traded that day/month/year
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
