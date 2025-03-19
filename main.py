import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Data Cleaner", page_icon="🧹"  ,layout="wide"                  )
st.title("Data Cleaner")
st.write("Upload your data file and clean it up!")          

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write("## Data Cleaning")
    st.write("### Remove Duplicates")
    df = df.drop_duplicates()
    st.write(df)
    st.write("### Remove Null Values")
    df = df.dropna()
    st.write(df)
    st.write("### Save Cleaned Data")
    cleaned_data = BytesIO()
    df.to_csv(cleaned_data, index=False)
    st.download_button("Download", cleaned_data, "cleaned_data.csv", "text/csv")
    

