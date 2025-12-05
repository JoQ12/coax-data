import yfinance as yf
import pandas as pd

# COAX Synthetic Commodity Index (Gold, Oil, Cocoa, Cotton)

assets = ["GC=F", "CL=F", "CC=F", "CT=F"]  # Gold, Oil, Cocoa, Cotton

def generate_index():
    data = yf.download(assets, period="1mo")["Close"]
    normalized = data / data.iloc[0]  # normalize values
    index = normalized.mean(axis=1)   # calculate index average
    index.name = "COAX_Index_1"
    return index

if __name__ == "__main__":
    index_data = generate_index()
    print(index_data.tail())
