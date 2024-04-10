% pip install pandas
% pip install plotly
import streamlit as st
import pandas as pd
from plotly import express as px
st.write('Hello world')
df = pd.read_excel('IQVIA_Thailand total market_2024.02.01.xlsx')
df.columns = ['country','sector','prescription','manufacturer','brand','drug','su2020','usd2020','su2021','usd2021','su2022','usd2022']
st.dataframe(df)
st.plotly_chart(px.scatter(df,x='su2022',y='usd2022'))
