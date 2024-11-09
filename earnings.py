from yfinance import Ticker
import requests
import pandas as pd
import json

class MyEarnings():
    
    def __init__(self):
        with open("config.json") as f:
            self.config = json.load(f)
        self.API= self.config["EARNINGS_API_KEY"]
    
    def get_earnings(self, ticker) -> pd.DataFrame:
        url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={self.API}"
        response = requests.get(url)
        earnings = pd.DataFrame(response.json()["annualEarnings"])
        earnings["reportedEPS"] = pd.to_numeric(earnings["reportedEPS"])
        return earnings

    def get_earnings_calendar(self, ticker) -> pd.DataFrame:
        url = f"https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&symbol={ticker}&apikey={self.API}"
        response = requests.get(url)
        earnings_calendar = pd.DataFrame(response.json()["earningsCalendar"])
        return earnings_calendar

    def get_earnings_call(self, ticker) -> pd.DataFrame:
        url = f"https://www.alphavantage.co/query?function=EARNINGS_CALL&symbol={ticker}&apikey={self.API}"
        response = requests.get(url)
        earnings_call = pd.DataFrame(response.json()["earningsCall"])
        return earnings_call

    def get_earnings_surprise(self, ticker) -> pd.DataFrame:
        url = f"https://www.alphavantage.co/query?function=EARNINGS_SURPRISES&symbol={ticker}&apikey={self.API}"
        response = requests.get(url)
        earnings_surprise = pd.DataFrame(response.json()["earningsSurprises"])
        return earnings_surprise
