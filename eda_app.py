import streamlit as st
import pandas as pd

@st.cache_data
def load_data(df):
    return pd.read_csv(df) 


df = load_data("data/dataset.csv")

def run_eda_app():
    st.subheader("Exploratory Data Analysis")
    submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
    if submenu == "Descriptive":
        st.dataframe(df)

        with st.expander("Data Types"):
            st.dataframe(df.dtypes)

        with st.expander("Data Summery"):
            st.dataframe(df.describe())

    elif submenu == "Plots":
        st.subheader('Data Visualization')
    
        