import streamlit as st
from data.data_processing import upload_file, preview_data
import os
import pandas as pd

def main():
    st.set_page_config(layout="wide")
    st.title("Dynamic Dashboard Creator")
    try:
        path="API_TOKEN.txt"
        os.environ["OPENAI_API_KEY"] = open(path, 'r').read()
    except:
        pass
    
    
    if 'uploaded_file' not in st.session_state:
        st.session_state['df'] = upload_file()
        if st.session_state['df'] is not None:
            st.rerun()
        demo_button = st.button("Use Demo Data")
        if demo_button:
            st.session_state['uploaded_file'] = True
            st.session_state['df'] = pd.read_excel('dashboard.xlsx')
            st.rerun()

    
    if 'uploaded_file' in st.session_state:
        preview_data(st.session_state['df'])
        
            
if __name__ == "__main__":
    main()
