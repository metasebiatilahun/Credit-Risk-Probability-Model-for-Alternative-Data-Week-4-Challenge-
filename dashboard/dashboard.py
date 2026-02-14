import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Portfolio Optimization Dashboard", layout="wide")

st.title("📈 Time-Series Portfolio Forecasting")

# Sidebar for user interaction
ticker = st.sidebar.selectbox("Select Asset", ['TSLA', 'BND', 'SPY'])
days_to_forecast = st.sidebar.slider("Forecast Horizon (Days)", 7, 60, 30)

# Display Key Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Sharpe Ratio", "1.25") # Example placeholder values
with col2:
    st.metric("Max Drawdown", "-15.4%")
with col3:
    st.metric("Predicted Return", "+4.2%")

# Interactive Plotting
st.subheader(f"Price Trends and Forecasts for {ticker}")
# Assuming 'df' is loaded from your cleaned data
fig = px.line(df[df['Ticker'] == ticker], x='Date', y='Adj Close', title=f"{ticker} Historical Data")
st.plotly_chart(fig, use_container_width=True)

st.write("### Business Impact Analysis")
st.info("The forecasting model suggests a rebalancing of 5% from TSLA to BND to mitigate volatility.")