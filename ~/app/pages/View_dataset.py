import streamlit as st

# Set the title of the app
st.title("Student Response")

# Embed Google Sheet using an iframe
# Use the published URL of the Google Sheet
google_sheet_url = "https://docs.google.com/spreadsheets/d/1bdywDzhqfDHut36grVDXjEkxYsm7YX_66sLYOyHh7w4/edit?usp=sharing"

iframe = f"""
<iframe 
    src="{google_sheet_url}" 
    width="1080" 
    height="600" 
    frameborder="0" 
    allowfullscreen>
</iframe>
"""

st.components.v1.html(iframe, height=800)
