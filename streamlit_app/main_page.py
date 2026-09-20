import streamlit as st

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("🛍️ Retail Sales Analytics Dashboard")
st.write("""
Welcome! This dashboard gives you an interactive way to explore retail sales 
behaviour and understand what really drives product performance.

Dive into the EDA (exploratory data analysis) to see how price, promotion, category, and shelf position 
influence sales. Then head to the Model Predictions page to experiment with different 
inputs and instantly see how they affect expected sales volume using our 
XGBoost model.

Use the sidebar to get started — insights, visuals, and predictions are all 
just a click away.
""")