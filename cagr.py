import streamlit as st
import pandas as pd
import altair as alt

# Page config
st.set_page_config(page_title="CAGR Tools by OP", page_icon="📈", layout="centered")

# ---------- CSS STYLES ----------
st.markdown("""
    <style>
        .title-box {
            background-color: #d0d0d0;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            color: black;
            font-size: 24px;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
        }
        .input-label {
            color: white;
            font-weight: 500;
            font-size: 16px;
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
        .unit-box {
            background-color: #3a3a5c;
            padding: 10px 20px;
            height: 46px;
            border-radius: 20px;
            color: white;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .stTextInput > div > input {
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title-box">CAGR Tools by OP</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------- TABS (Full Width) ----------
tab1, tab2 = st.tabs(["📈 CAGR Calculator", "🔁 Reverse CAGR Calculator"])

# ---------- 📈 CAGR Calculator ----------
with tab1:
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.markdown('<div class="input-label">Initial Value</div>', unsafe_allow_html=True)
    with col2:
        initial_value = st.text_input("", value="10000", label_visibility="collapsed", key="initial")
    with col3:
        st.markdown('<div class="unit-box">₹</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.markdown('<div class="input-label">Final Value Costs</div>', unsafe_allow_html=True)
    with col2:
        final_value = st.text_input("", value="20000", label_visibility="collapsed", key="final")
    with col3:
        st.markdown('<div class="unit-box">₹</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.markdown('<div class="input-label">Duration of Investment</div>', unsafe_allow_html=True)
    with col2:
        years = st.text_input("", value="5", label_visibility="collapsed", key="years")
    with col3:
        st.markdown('<div class="unit-box">Yrs</div>', unsafe_allow_html=True)

    try:
        p = float(initial_value.replace(",", ""))
        f = float(final_value.replace(",", ""))
        t = float(years)

        if p <= 0 or f <= 0 or t <= 0:
            st.error("All values must be greater than 0.")
        else:
            cagr = ((f / p) ** (1 / t)) - 1
            cagr_percent = round(cagr * 100, 2)

            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.markdown('<div class="unit-box">CAGR</div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="result-box">{cagr_percent}</div>', unsafe_allow_html=True)
            with col3:
                st.markdown('<div class="unit-box">%</div>', unsafe_allow_html=True)

            years_list = list(range(1, int(t) + 1))
            values = [round(p * ((1 + cagr) ** year), 2) for year in years_list]
            df = pd.DataFrame({'Year': years_list, 'Investment Value': values})

            st.markdown("<div style='margin-top: 30px; margin-bottom: 15px; font-size: 24px; font-weight: bold; text-align: center;'>📊 Investment Growth Over Time</div>", unsafe_allow_html=True)
            chart = alt.Chart(df).mark_bar(color='#009e64').encode(
                x=alt.X('Year:O', title='Year', axis=alt.Axis(labelAngle=0)),
                y=alt.Y('Investment Value:Q', title='Value (₹)'),
                tooltip=['Year', 'Investment Value']
            ).properties(height=400)

            st.altair_chart(chart, use_container_width=True)

    except Exception as e:
        st.error("Please enter valid numbers only.")

# ---------- 🔁 Reverse CAGR Calculator ----------
with tab2:
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.markdown('<div class="input-label">Initial Value</div>', unsafe_allow_html=True)
    with col2:
        initial_value_r = st.text_input("", value="10000", label_visibility="collapsed", key="rev_initial")
    with col3:
        st.markdown('<div class="unit-box">₹</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.markdown('<div class="input-label">CAGR</div>', unsafe_allow_html=True)
    with col2:
        cagr_percent_r = st.text_input("", value="14.87", label_visibility="collapsed", key="rev_cagr")
    with col3:
        st.markdown('<div class="unit-box">%</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.markdown('<div class="input-label">Duration</div>', unsafe_allow_html=True)
    with col2:
        years_r = st.text_input("", value="5", label_visibility="collapsed", key="rev_years")
    with col3:
        st.markdown('<div class="unit-box">Yrs</div>', unsafe_allow_html=True)

    try:
        p_r = float(initial_value_r.replace(",", ""))
        cagr_r = float(cagr_percent_r) / 100
        t_r = float(years_r)

        if p_r <= 0 or cagr_r <= 0 or t_r <= 0:
            st.error("All values must be greater than 0.")
        else:
            final_r = p_r * ((1 + cagr_r) ** t_r)
            final_r = round(final_r, 2)

            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.markdown('<div class="unit-box">Maturity Value</div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="result-box">{final_r}</div>', unsafe_allow_html=True)
            with col3:
                st.markdown('<div class="unit-box">₹</div>', unsafe_allow_html=True)

            years_list_r = list(range(1, int(t_r) + 1))
            values_r = [round(p_r * ((1 + cagr_r) ** year), 2) for year in years_list_r]
            df_r = pd.DataFrame({'Year': years_list_r, 'Projected Value': values_r})

            st.markdown("<div style='margin-top: 30px; margin-bottom: 15px; font-size: 24px; font-weight: bold; text-align: center;'>📊 Future Value Projection</div>", unsafe_allow_html=True)
            chart_r = alt.Chart(df_r).mark_bar(color='#009e64').encode(
                x=alt.X('Year:O', title='Year', axis=alt.Axis(labelAngle=0)),
                y=alt.Y('Projected Value:Q', title='Value (₹)'),
                tooltip=['Year', 'Projected Value']
            ).properties(height=400)

            st.altair_chart(chart_r, use_container_width=True)

    except Exception as e:
        st.error("Please enter valid numbers only.")
