import streamlit as st
import pandas as pd
import plotly.express as px

#read data
df = pd.read_excel("factbook.xlsx")

#variable
x_col = "  GDP per capita "
y_col = " Life expectancy at birth"
size_col = "  Population "
# clr = "Country"
hvr_name_col = "Country"

fig = px.scatter(df, x=x_col, y=y_col, size=size_col, hover_name=hvr_name_col,
                 log_x=True, size_max=60)

st.plotly_chart(fig)