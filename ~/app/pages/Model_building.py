import streamlit as st

# Set the title of the app
st.title("Model Building Report")

# Colab notebook URL
colab_url = "https://colab.research.google.com/drive/1synJHFfdN8xHGMOuAXSS_dVwVuostqXx"
embed_url = colab_url.replace("https://colab.research.google.com/drive/", "https://colab.research.google.com/drive/embed/")

# Embed Google Colab notebook using an iframe
iframe = f"""
<iframe 
    src="{embed_url}" 
    width="800" 
    height="600" 
    frameborder="0" 
    allowfullscreen>
</iframe>
"""
st.components.v1.html(iframe, height=600)

