from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"status": "COAX DATA API is running"}

@app.get("/price/{symbol}")
def get_price(symbol: str):
    data = yf.Ticker(symbol)
    price = data.history(period="1d")["Close"].iloc[-1]
    return {"symbol": symbol, "price": float(price)}
