import streamlit as st
import pandas as pd
import plotly.express as px

#read data
df = pd.read_excel("factbook.xlsx")

#Bubble Chart
#variable
x_col = "  GDP per capita "
y_col = " Life expectancy at birth"
size_col = "  Population "
clr = " Birth rate"
hvr_name_col = "Country"

fig = px.scatter(df, x=x_col, y=y_col, size=size_col, color=clr, hover_name=hvr_name_col,
                 log_x=True, size_max=60)

fig.update_layout(
    title="GDP per capita vs Life expectancy",
    xaxis_title="GDP per capita",
    yaxis_title="Life expectancy"
)
st.plotly_chart(fig)

#dropdown list
select_col = st.selectbox("List Kolom", df.columns)

st.write(df[select_col])
