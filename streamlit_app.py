import streamlit as st

st.title("My Streamlit App")
st.write("Hello, world!")


# read a secret
secret = st.secrets["SERVING_ENDPOINT"]

# show the secret
st.write(f"SERVING_ENDPOINT: {secret}")