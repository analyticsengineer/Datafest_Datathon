import streamlit as st
import os
from google.oauth2 import service_account
from google.cloud import bigquery
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
credentials = service_account.Credentials.from_service_account_info({
    "type": os.getenv("GCP_SERVICE_ACCOUNT_TYPE"),
    "project_id": os.getenv("GCP_PROJECT_ID"),
    "private_key_id": os.getenv("GCP_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GCP_PRIVATE_KEY").replace('\\n', '\n'),  # Replace newline escape sequences
    "client_email": os.getenv("GCP_CLIENT_EMAIL"),
    "client_id": os.getenv("GCP_CLIENT_ID"),
    "auth_uri": os.getenv("GCP_AUTH_URI"),
    "token_uri": os.getenv("GCP_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("GCP_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("GCP_CLIENT_X509_CERT_URL"),
})

# Create a BigQuery client
client = bigquery.Client(credentials=credentials, project=os.getenv("GCP_PROJECT_ID"))

# Streamlit app
st.title("BigQuery Streamlit App")
