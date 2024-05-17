"""
# My First app
Here's out first attempt at using data to create a table:
"""

import pandas as pd
import streamlit as st
import numpy as np

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10,20,30,40]
})
df

dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))

)
st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("Hello World")