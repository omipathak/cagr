import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="CAGR Tools by OP", page_icon="📈", layout="centered")

# ---------- MOBILE-FRIENDLY CSS ----------
st.markdown("""
    <style>
        .title-box {
            background-color: #d0d0d0;
            padding: 5px;
            border-radius: 10px;
            text-align: center;
            color: black;
            font-size: 22px;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
        }
        .input-label {
            color: white;
            font-weight: 500;
            font-size: 16px;
            margin-bottom: 5px;
        }
        .result-box {
            background-color: #009e64;
            padding: 10px 20px;
            height: 46px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-size: 18px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .stTextInput > div > input {
            font-size: 14px;
        }
        @media only screen and (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box">CAGR Tools by OP</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📈 CAGR Calculator", "🔁 Reverse CAGR Calculator"])

# ---------- 📈 CAGR Calculator ----------
with tab1:
    initial_value = st.text_input("Initial Value (₹)", value="10000", key="initial")
    final_value = st.text_input("Final Value (₹)", value="20000", key="final")
    years = st.text_input("Duration (Yrs)", value="5", key="years")

    try:
        p = float(initial_value.replace(",", ""))
        f = float(final_value.replace(",", ""))
        t = float(years.replace(",", ""))

        if p <= 0 or f <= 0 or t <= 0:
            st.error("All values must be greater than 0.")
        else:
            cagr = ((f / p) ** (1 / t)) - 1
            cagr_percent = round(cagr * 100, 2)

            formatted_cagr = f"{cagr_percent:.2f}"
            st.markdown(f'<div class="result-box">CAGR: {formatted_cagr}%</div>', unsafe_allow_html=True)

            years_list = list(range(1, int(t) + 1))
            values = [round(p * ((1 + cagr) ** year), 2) for year in years_list]
            formatted_values = [f"₹ {v:,.2f}" for v in values]
            df = pd.DataFrame({'Year': years_list, 'Investment Value': values, 'Label': formatted_values})

            st.markdown("<div style='margin-top: 30px; text-align:center; font-size: 20px; font-weight: bold;'>📊 Investment Growth Over Time</div>", unsafe_allow_html=True)
            chart = alt.Chart(df).mark_bar(color='#009e64').encode(
                x=alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
                y=alt.Y('Investment Value:Q'),
                tooltip=['Year', alt.Tooltip('Investment Value:Q', title='Value (₹)', format=',.2f')]
            ).properties(height=400)

            st.altair_chart(chart, use_container_width=True)

    except:
        st.error("Please enter valid numbers only.")

# ---------- 🔁 REVERSE CAGR ----------
with tab2:
    initial_value_r = st.text_input("Initial Value (₹)", value="10000", key="rev_initial")
    cagr_percent_r = st.text_input("CAGR (%)", value="12", key="rev_cagr")
    years_r = st.text_input("Duration (Yrs)", value="5", key="rev_years")

    try:
        p_r = float(initial_value_r.replace(",", ""))
        cagr_r = float(cagr_percent_r.replace(",", "")) / 100
        t_r = float(years_r.replace(",", ""))

        if p_r <= 0 or cagr_r <= 0 or t_r <= 0:
            st.error("All values must be greater than 0.")
        else:
            final_r = round(p_r * ((1 + cagr_r) ** t_r), 2)
            formatted_final = f"₹ {final_r:,.2f}"
            st.markdown(f'<div class="result-box">Final Value: {formatted_final}</div>', unsafe_allow_html=True)

            years_list_r = list(range(1, int(t_r) + 1))
            values_r = [round(p_r * ((1 + cagr_r) ** year), 2) for year in years_list_r]
            formatted_values_r = [f"₹ {v:,.2f}" for v in values_r]
            df_r = pd.DataFrame({'Year': years_list_r, 'Projected Value': values_r, 'Label': formatted_values_r})

            st.markdown("<div style='margin-top: 30px; text-align:center; font-size: 20px; font-weight: bold;'>📊 Future Value Projection</div>", unsafe_allow_html=True)
            chart_r = alt.Chart(df_r).mark_bar(color='#009e64').encode(
                x=alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
                y=alt.Y('Projected Value:Q'),
                tooltip=['Year', alt.Tooltip('Projected Value:Q', title='Value (₹)', format=',.2f')]
            ).properties(height=400)

            st.altair_chart(chart_r, use_container_width=True)

    except:
        st.error("Please enter valid numbers only.")
