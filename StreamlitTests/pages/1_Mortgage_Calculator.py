import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Mortgage Calculator",
    page_icon="💸",
)

st.title("💸 Mortgage Calculator")
st.divider()
st.sidebar.title("Mortgage Calculator")
st.sidebar.markdown("This is a simple tool to help users quickly check the repayment cost of a mortgage with user-given values")
st.sidebar.divider()
housePrice = st.number_input("House Price ($)", 0, None, value=250000)
if st.checkbox("Use Percentage?"):
    downpaymentPercentage = st.number_input("Downpayment (%)", 0, 100, value=10)
    downpayment = (downpaymentPercentage / 100) * housePrice
else:
    downpayment = st.number_input("Downpayment ($)", 0, value=25000)

interestRate = st.number_input("Interest Rate (%)", 0.0, value=3.5)
loanTerm = st.number_input("Loan Term in Years", 0, 30, value=20)

if loanTerm <= 0:
    st.divider()
    st.error("Loan Term must be greater than 0.")
else:
    numPayments = loanTerm * 12
    loanAmount = housePrice - downpayment
    monthlyInterestRate = interestRate / 12 / 100

    if interestRate == 0:
        monthlyPayment = round(loanAmount / numPayments, 2)
    else:
        monthlyPayment = round(loanAmount * (monthlyInterestRate * (1 + monthlyInterestRate) ** numPayments) / ((1 + monthlyInterestRate) ** numPayments - 1), 2)
    
    st.divider()
    st.write("Loaned amount: $", loanAmount)
    st.write("Monthly Payment: $", monthlyPayment)