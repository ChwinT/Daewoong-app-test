import streamlit as st
import pandas as pd
st.write('Hello world')
st.dataframe(pd.DataFrame({'index':[1,2,3],'value':[58,98,43]}))