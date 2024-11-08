import yfinance as yf
import pandas as pd


class MyTicker:

    def get_price(self, ticker,period) -> pd.DataFrame:
        return yf.Ticker(ticker).history(period=period)['Close']
    
    def get_prices(self,tickers, period) -> pd.DataFrame:
        prices = yf.Tickers(tickers).history(period=period)['Close']
        return prices
    
    def get_52_week_high(self, ticker) -> float:
        return yf.Ticker(ticker).info['fiftyTwoWeekHigh']
    
    def get_52_week_low(self, ticker) -> float:
        return yf.Ticker(ticker).info['fiftyTwoWeekLow']
    
    def get_50_day_average(self, ticker) -> float:
        return yf.Ticker(ticker).info['fiftyDayAverage']
    
    def get_200_day_average(self, ticker) -> float:
        return yf.Ticker(ticker).info['twoHundredDayAverage']

