import streamlit as st
import pandas as pd
from MyScreener import MyScreener
from MyTickers import MyTicker

def linechart(title,data, period):
    st.subheader(f"{title}")
    


def table(title, data):
    st.subheader(f"{title}")
    st.write(data)
    
def display( ):
    st.title("Option Pricing with Black-Scholes Model")
    myScreener = MyScreener()
    table("Growth Technology Stocks", myScreener.get_growth_technology_stocks())

    myTicker = MyTicker()
    linechart("Microsoft Price", myTicker.get_price("MSFT", "3mo"))

if __name__ == "__main__":
    display()