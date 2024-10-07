import streamlit as st

# Set the title of the app
st.title("Student Response")

# Embed Google Sheet using an iframe
# Make sure to set the URL to the published Google Sheet
google_sheet_url = "https://docs.google.com/spreadsheets/d/1bdywDzhqfDHut36grVDXjEkxYsm7YX_66sLYOyHh7w4/edit?usp=sharing"
iframe = f"""
<iframe 
    src="{google_sheet_url}" 
    width="800" 
    height="600" 
    frameborder="0" 
    allowfullscreen>
</iframe>
"""

# Combine the two iframes in a single HTML output
combined_iframe = f"""
<div>
    {iframe}
    <iframe src="YOUR_IFRAME_SOURCE" width="100%" height="800" style="border: none;"></iframe>
</div>
"""

st.components.v1.html(combined_iframe, height=800)
