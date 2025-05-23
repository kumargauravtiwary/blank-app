import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to get VIX signal
def get_vix_signal():
    vix = yf.download("^INDIAVIX", period="5d", interval="1d")
    latest_vix = vix['Close'].iloc[-1]

    if latest_vix < 13:
        return latest_vix, "🔵 VIX is low. Consider selling options (Spreads, Iron Condor)."
    elif 13 <= latest_vix <= 20:
        return latest_vix, "🟡 VIX is moderate. Neutral/Directional strategies like Covered Call or Calendar Spread are suitable."
    else:
        return latest_vix, "🔴 VIX is high. Market expects big moves. Consider buying options (Straddle, Strangle)."

# Main app function
def main():
    st.title("📈 Options Strategy Assistant with VIX Insight")

    vix_value, strategy = get_vix_signal()

    st.subheader("📊 India VIX Insight")
    st.metric(label="Current India VIX", value=round(vix_value, 2))
    st.info(strategy)

    st.markdown("---")
    st.subheader("🔍 Strategy Explorer (Coming Soon)")
    st.write("More strategy modules will be integrated here.")

if __name__ == "__main__":
    main()