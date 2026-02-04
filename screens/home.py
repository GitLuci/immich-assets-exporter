import streamlit as st
from click import option

from load_screen_data import data_loader
from load_screen_data import data_actions

if 'refreshed-buckets' not in st.session_state:
    st.session_state['refreshed-buckets'] = None
if 'current-bucket-info' not in st.session_state:
    st.session_state['current-bucket-info'] = None
if 'current-bucket' not in st.session_state:
    st.session_state['current-bucket'] = None

if st.session_state['refreshed-buckets'] == None:
    st.session_state['refreshed-buckets'] = data_loader.refreshed_buckets()

def option_on_change(curr_option):
    if curr_option != None:
        st.session_state['current-bucket-info'] = data_loader.timebucket_assets_info(curr_option["timeBucket"])
        st.session_state['current-bucket'] = curr_option

option_on_change(st.selectbox(
    "What Time Line Bucket you want download ?",
    (st.session_state['refreshed-buckets']),index=None
))


st.write("Count is the number os items (photos or videos) in determinate time bucket")
st.write("You selected option:", st.session_state['current-bucket'])
st.write("Had:", st.session_state['current-bucket-info'])

if st.session_state['current-bucket'] != None:
    if st.button("Prepare download"):
        st.download_button(
            label="Download Zip",
            data=data_actions.timebucket_assets_download(st.session_state['current-bucket']['timeBucket']),
            file_name="images.zip",
            mime="bytes/zip",
            icon=":material/download:",
        )
    st.write('For huge amount of data, the button can have a delay to show, wait for some time and the download button will be appear.')


