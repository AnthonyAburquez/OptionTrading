import yfinance as yf
import pandas as pd

"""
Available Predefined Bodies for yfinance Screener:

- day_gainers: Stocks with significant gains in price over the past day.
- day_losers: Stocks with significant losses in price over the past day.
- most_actives: Stocks with the highest trading volumes.

- undervalued_large_caps: Large-cap stocks considered undervalued based on certain financial metrics.
- undervalued_growth_stocks: Growth stocks that are currently undervalued.
- growth_technology_stocks: Technology sector stocks exhibiting growth characteristics.

- aggressive_small_caps: Small-cap stocks with aggressive growth potential.
- small_cap_gainers: Small-cap stocks with notable price gains.

- portfolio_anchors: Stocks considered stable and reliable, often used as foundational holdings in portfolios.

- most_shorted_stocks: Stocks with high short interest ratios.
"""
class MyScreener:
    def __init__(self):
        self.screener = yf.Screener()

    def parse(self):
        quotes = self.screener.response["quotes"]
        filted = pd.DataFrame([
        {
            'symbol': quote['symbol'],
            'shortName': quote['shortName'],
            'regularMarketPrice': quote['regularMarketPrice'],
            'regularMarketChange': quote['regularMarketChange'],
            'regularMarketChangePercent': quote['regularMarketChangePercent'],
            'regularMarketVolume': quote['regularMarketVolume'],
            'averageDailyVolume3Month': quote['averageDailyVolume3Month'],
            'averageDailyVolume10Day': quote['averageDailyVolume10Day'],
            'fiftyTwoWeekHigh': quote['fiftyTwoWeekHigh'],
            'fiftyTwoWeekLow': quote['fiftyTwoWeekLow'],
            'fiftyDayAverage': quote['fiftyDayAverage'],
            'twoHundredDayAverage': quote['twoHundredDayAverage'],
            'marketCap': quote['marketCap'],
            'averageAnalystRating': quote['averageAnalystRating']
        }
            for quote in quotes
        ])
        return filted
        
    def get_day_gainers(self):
        self.screener.set_predefined_body("day_gainers")
        return self.parse()
    
    def get_day_losers(self):
        self.screener.set_predefined_body("day_losers")
        return self.parse()

    def get_most_actives(self):
        self.screener.set_predefined_body("most_actives")
        return self.parse()

    def get_undervalued_large_caps(self):
        self.screener.set_predefined_body("undervalued_large_caps")
        return self.parse()

    def get_undervalued_growth_stocks(self):
        self.screener.set_predefined_body("undervalued_growth_stocks")
        return self.parse()

    def get_growth_technology_stocks(self):
        self.screener.set_predefined_body("growth_technology_stocks")
        return self.parse()

    def get_aggressive_small_caps(self):
        self.screener.set_predefined_body("aggressive_small_caps")
        return self.parse()

    def get_small_cap_gainers(self):
        self.screener.set_predefined_body("small_cap_gainers")
        return self.parse()

    def get_portfolio_anchors(self):
        self.screener.set_predefined_body("portfolio_anchors")
        return self.parse()

    def get_most_shorted_stocks(self):
        self.screener.set_predefined_body("most_shorted_stocks")
        return self.parse()



if __name__ == '__main__':
    myScreener = MyScreener()
    response = myScreener.get_growth_technology_stocks()
    print(response)
    print(f"Total companies: {len(response)}")
    