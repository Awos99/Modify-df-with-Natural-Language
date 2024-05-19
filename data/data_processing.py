import pandas as pd
import streamlit as st
from visualizations.dataframe_modification import create_dataframe
import pandas as pd

def extract_tables_from_excel(excel_path):
    # Load the Excel file
    xls = pd.ExcelFile(excel_path)
    sheet_data={}
    for sheet_name in xls.sheet_names:
        print(sheet_name)
        df = pd.read_excel(xls, sheet_name=sheet_name)
        sheet_data[sheet_name] = df
    return sheet_data


def upload_file():
    uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])
    if uploaded_file:
        st.session_state['uploaded_file'] = True
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            return extract_tables_from_excel(uploaded_file)
        return {'csv_table': df}
    return None


def preview_data(df):
    if df is not None:
        if type(df) == dict:
            table_name=list(df.keys())[0]
            if table_name not in st.session_state:
                st.session_state[table_name] = df[table_name].reset_index(drop=True)
            st.write(f"Table Name: {table_name}")
            create_dataframe(table_name)
            st.write("Basic Statistics:")
            st.write(st.session_state[table_name].describe())
        else:
            if 'df' not in st.session_state:
                st.session_state['df'] = df
            st.write("View of the dataset:")
            create_dataframe('df')
            st.write("Basic Statistics:")
            st.write(st.session_state['df'].describe())
