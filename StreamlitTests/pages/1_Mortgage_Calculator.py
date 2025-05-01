import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

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
startDate = st.date_input("Start Date", pd.to_datetime("today"))

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
    
    st.write("Loaned amount: $", loanAmount)
    st.write("Monthly Payment: $", monthlyPayment)
    st.divider()

    schedule = []
    remainingBalance = loanAmount
    totalPaidOff = 0
    totalInterestPaid = 0

    for i in range(1, numPayments + 1):
        interestPayment = round(remainingBalance * monthlyInterestRate, 2)
        principalPayment = round(monthlyPayment - interestRate, 2)
        totalPaidOff += principalPayment
        totalInterestPaid += interestPayment
        remainingBalance = max(0, remainingBalance - principalPayment)
        schedule.append([i, monthlyPayment, principalPayment, interestPayment, remainingBalance, totalPaidOff, totalInterestPaid])

        if remainingBalance == 0:
            break

    df_schedule = pd.DataFrame(schedule, columns=["Payment #", "Monthly Payment", "Principal", "Interest", "Remaining Balance", "Total Paid Off", "Total Interest Paid"])
    yearly_schedule = df_schedule[df_schedule["Payment #"] % 12 == 0].copy()
    yearly_schedule["Year"] = yearly_schedule["Payment #"] // 12
    
    leftSide, rightSide = st.columns(2)
    
    leftSide.subheader("Amortization Schedule")
    leftSide.dataframe(yearly_schedule[["Year", "Remaining Balance", "Total Paid Off", "Total Interest Paid"]])
    leftSide.divider()

    rightSide.subheader("Loan Progress Over Time")
    rightSide.line_chart(df_schedule.set_index("Payment #")[["Remaining Balance", "Total Paid Off", "Total Interest Paid"]])
    rightSide.divider()

    totalPrincipal = df_schedule["Principal"].sum()
    totalInterest = df_schedule["Interest"].sum()
    leftSide.subheader("Breakdown of Total Payments")
    pie_chart = px.pie(
        names=["Principal", "Interest"],
        values=[totalPrincipal, totalInterest],
        title="Total Payments Breakdown",
        hole=0.4
    )
    leftSide.plotly_chart(pie_chart)
    leftSide.divider()
