import streamlit as st
import yfinance as yf
from openai import OpenAI

client = OpenAI()

st.title("AI Financial Analysis Tool")

# Sidebar inputs
ticker = st.sidebar.text_input("Enter stock ticker (e.g. AAPL, MSFT)")
start_date = st.sidebar.date_input("Start date")
end_date = st.sidebar.date_input("End date")

if st.sidebar.button("Analyze"):

    if ticker:
        data = yf.download(ticker, start=start_date, end=end_date)

        st.subheader(f"Stock Data for {ticker}")
        st.line_chart(data["Close"])

        # Prepare data summary for AI
        summary_text = data.describe().to_string()

        st.subheader("AI Financial Summary")

        prompt = f"""
        You are a financial analyst. Based on the following stock data summary,
        give a financial analysis in simple terms:

        {summary_text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write(response.choices[0].message["content"])
    else:
        st.error("Please enter a valid stock ticker.")
