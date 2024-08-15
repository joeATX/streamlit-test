import streamlit as st
import pandas as pd
from eda_app import run_eda_app

df = pd.read_csv('data/dataset.csv')

home_template = """
    #### Lung Cancer Predictor
    This dataset contains the most current lung cancer data

    #### About the Dataset
    This dataset provides annual data from several factors that are common with
    lung cancer.

    The data is sourced from:
    - **World Health Organization
    - **Retrieved from** https://www.kaggle.com/datasets/akashnath29/lung-cancer-dataset

    **Dataset Source:** Kaggle

    #### App Content
    - EDA Section: Exploratory Data Analysis
    - ML Section: ML Predictor App
"""

def main():
    st.title("Lung Cancer Predictions")
    menu = ["Home", "EDA", "ML"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write(home_template)
    elif choice == "EDA":
        run_eda_app()


if __name__ == '__main__':
    main()