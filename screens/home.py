import streamlit as st
from load_screen_data import data_loader

if 'refreshed-buckets' not in st.session_state:
    st.session_state['refreshed-buckets'] = None


if st.session_state['refreshed-buckets'] == None:
    st.session_state['refreshed-buckets'] = data_loader.refreshed_buckets()




option = st.selectbox(
    "What Time Line Bucket you want download ?",
    (st.session_state['refreshed-buckets']),
)
st.write("Count is the number os items (photos or videos) in determinate time bucket")
st.write("You selected option:", option)