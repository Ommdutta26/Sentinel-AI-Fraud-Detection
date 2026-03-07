import streamlit as st
import plotly.graph_objects as go
from predict import predict_fraud

st.set_page_config(page_title="Sentinel AI Fraud Detection", layout="wide")

st.title("🛡️ Sentinel AI - Fraud Detection System")
st.markdown("Advanced ML system using **XGBoost + Neural Network + LSTM**")

st.sidebar.header("Transaction Input")

amount = st.sidebar.number_input("Transaction Amount")

old_balance = st.sidebar.number_input("Sender Old Balance")
new_balance = st.sidebar.number_input("Sender New Balance")

old_dest = st.sidebar.number_input("Receiver Old Balance")
new_dest = st.sidebar.number_input("Receiver New Balance")

dest_degree = st.sidebar.number_input("Receiver Connectivity")

velocity = st.sidebar.number_input("Transaction Velocity")

type_transfer = st.sidebar.checkbox("TRANSFER")
type_cashout = st.sidebar.checkbox("CASH_OUT")

if st.sidebar.button("Analyze Transaction"):

    decision, prob, risk = predict_fraud(
        amount,
        old_balance,
        new_balance,
        old_dest,
        new_dest,
        dest_degree,
        velocity,
        type_transfer,
        type_cashout
    )

    prob_value = float(prob.replace("%",""))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Fraud Decision")
        st.write(decision)

        st.subheader("Risk Level")
        st.write(risk)

    with col2:

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prob_value,
            title={'text': "Fraud Probability"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0,40], 'color': "green"},
                    {'range': [40,70], 'color': "yellow"},
                    {'range': [70,100], 'color': "red"},
                ],
            }
        ))

        st.plotly_chart(fig)