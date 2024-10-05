import streamlit as st
import pandas as pd

# Path to the CSV file
csv_file_path = 'data_dictionary.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Display the DataFrame
st.write("Data from CSV:")
st.dataframe(df)
