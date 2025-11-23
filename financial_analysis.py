import streamlit as st
from openai import OpenAI
import yfinance as yf

# Χρησιμοποιούμε το API key από το secrets.toml
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Financial Analysis AI")

# Παράδειγμα: παίρνουμε δεδομένα μιας μετοχής
ticker = st.text_input("Enter ticker symbol", "AAPL")
if ticker:
    data = yf.Ticker(ticker).history(period="1mo")
    st.write(data)

