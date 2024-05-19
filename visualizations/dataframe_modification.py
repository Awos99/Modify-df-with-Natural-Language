import streamlit as st
from agents.agents import generate_dataframe_modif_code
import pandas as pd

def check_unique_columns(df):
    df.columns = df.columns.str.strip()  # Strip whitespaces from column names
    cols = pd.Series(df.columns)
    for dup in cols[cols.duplicated()].unique(): 
        cols[cols[cols == dup].index.values.tolist()] = [dup + str(i) if i != 0 else dup for i in range(sum(cols == dup))]
    df.columns = cols
    return df

def create_dataframe(name):
    container = st.container()

    col1, col2 = container.columns(2)
    col1.write(f"**{name}**")
    st.session_state[name] = col1.data_editor(st.session_state[name], num_rows='dynamic').reset_index(drop=True)
    with col2:
        st.subheader("Modify")
        box, button = st.columns([0.7, 0.3])
        column=box.selectbox("Column to drop", st.session_state[name].columns, label_visibility='collapsed')
        button_drop=button.button("Drop Column")
        if button_drop:
            st.session_state[name] = st.session_state[name].drop(columns=[column])
            button_drop = False
            st.rerun()
        text = st.text_input("Write modification", value="")
        button_apply = st.button("Apply")
        if button_apply:
            st.session_state['code'] = generate_dataframe_modif_code(st.session_state[name], text)
            print(st.session_state['code'])
            exec(st.session_state['code'], globals())
            print(st.session_state[name].columns)
            # check if the function is defined
            if 'modify_dataframe' in globals():
                st.session_state[name] = modify_dataframe(st.session_state[name])
            st.session_state[name] = check_unique_columns(st.session_state[name])
            button_apply = False
            text = ""
            st.rerun()
        if 'code' in st.session_state:
            st.write("Code:")
            st.code(st.session_state['code'])
        
