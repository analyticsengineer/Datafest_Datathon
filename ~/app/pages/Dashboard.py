import streamlit as st

# Set the title of the app
st.title("Embed Power BI Report")

# Embed Power BI report using an iframe
powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiYWNlNGVmYmItNWMyZS00M2FiLTk3YTUtNGE5NjEzY2Y5MzUwIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"
iframe = f"""
<iframe width="800" height="600" 
        src="{powerbi_url}" 
        frameborder="0" 
        allowFullScreen="true"></iframe>
"""
st.components.v1.html(iframe, height=600)

