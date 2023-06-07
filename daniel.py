import streamlit as st

# Title
st.title('Simple Linear Regression')

# Sidebar
with st.sidebar:
    sidebar_type = st.radio('Choose Method', ['Correlation', 'Simple Linear Regression', 'R-Square'])
