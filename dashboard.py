import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# --- DATABASE CONNECTION SETTINGS ---
db_user = 'braga_user'
db_password = 'braga_password'
db_host = 'db'
db_port = '5432'
db_name = 'braga_db'
table_name = 'osm_infra_braga'

# --- FUNCTION TO LOAD DATA ---
# The underscore in '_engine' tells Streamlit's cache to ignore this argument.
@st.cache_data
def load_data(_engine):
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql(query, _engine)
    return df

# --- APPLICATION TITLE ---
st.title("Braga Infrastructure Dashboard")

# --- CONNECT TO DATABASE AND LOAD DATA ---
try:
    db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(db_url)
    
    # The function call remains the same
    data = load_data(engine)

    st.header("Map of Points of Interest")
    
    # Rename columns for st.map() compatibility
    data.rename(columns={'latitude': 'lat', 'longitude': 'lon'}, inplace=True)
    
    st.map(data)

    st.header("Detailed Data View")
    st.write("Raw data loaded from PostgreSQL:")
    
    st.dataframe(data)

except Exception as e:
    st.error(f"An error occurred while connecting to the database or loading data: {e}")

