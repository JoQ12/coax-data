import streamlit as st
import yfinance as yf

st.set_page_config(page_title="COAX Data Terminal", layout="wide")

st.title("📊 COAX Data Terminal - Lite Version")
st.write("Retrieve financial market data in real-time.")

symbol = st.text_input("Enter a market symbol (example: EURUSD=X, GC=F, BTC-USD)", "EURUSD=X")

if st.button("Get Data"):
    try:
        data = yf.download(symbol, period="1mo")
        if data.empty:
            st.error("Invalid symbol or no data available.")
        else:
            st.success(f"Data loaded for {symbol}")
            st.line_chart(data["Close"])
            st.write(data.tail())
    except Exception as e:
        st.error(f"Error retrieving data: {e}")
