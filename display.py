import streamlit as st
import pandas as pd
from MyScreener import MyScreener
from MyTickers import MyTicker
from earnings import MyEarnings

def linechart(title,data, period):
    st.subheader(f"{title}")
    
def earnings(ticker):
    st.subheader(f"Earnings for {ticker}")
    earnings = MyEarnings().get_earnings(ticker)
    st.write(earnings)

def table(title,data:pd.DataFrame):
    st.subheader(f"{title}")
    st.write(data.sort_values(by=['Market Change %',"Market Cap","Price"], ascending=False))
    
def display( ):
    st.title("Option Pricing with Black-Scholes Model")
    myScreener = MyScreener()
    table("Growth Technology Stocks", myScreener.get_growth_technology_stocks())
    table("Undervalued Growth Stocks", myScreener.get_undervalued_growth_stocks())
    earnings("MSFT")

if __name__ == "__main__":
    display()