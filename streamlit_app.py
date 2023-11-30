import streamlit as st
import pandas as pd

data = {'Név': ['John', 'Jane', 'Bob', 'Alice'],
        'Életkor': [25, 30, 22, 28],
        'Város': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Streamlit alkalmazás kódja
st.title('Példa táblázat Streamlit-ben')
st.dataframe(df)
