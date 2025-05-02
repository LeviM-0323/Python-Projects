import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Explorer",
    page_icon="📊",
)

st.title("📊 Data Explorer")
st.markdown("Upload a CSV file to explore and visualize your data.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Data Visualization")
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    if st.button("Generate Plot"):
        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis]. alpha=0.7)
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig)
else:
    st.info("Please upload a CSV file to get started.")