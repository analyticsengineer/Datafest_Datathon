import streamlit as st

# Set the title of the app
st.title("Student Response")

# Embed Google Sheet using an iframe
# Use the published URL of the Google Sheet
google_sheet_url = "https://docs.google.com/spreadsheets/d/e/YOUR_PUBLISHED_LINK/pubhtml?widget=true&headers=false"

iframe = f"""
<iframe 
    src="{google_sheet_url}" 
    width="800" 
    height="600" 
    frameborder="0" 
    allowfullscreen>
</iframe>
"""

st.components.v1.html(iframe, height=800)
