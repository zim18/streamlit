import streamlit as st
import pandas as pd
import plotly.express as px

#read data
df = pd.read_excel("factbook.xlsx")

#Bubble Chart
#variable
x_var = st.radio("Select X variable:", ["  GDP per capita ", "  Population ", "  Current account balance "])
y_var = st.radio("Select Y variable:", [" Life expectancy at birth", "  Population ", " Electricity consumption"])
size_var = st.radio("Select size variable:", [" Area", "  Population ", "  Highways ", "  Internet users "])
# x_col = "  GDP per capita "
# y_col = " Life expectancy at birth"
# size_col = "  Population "
clr = st.radio("Select color variable:", [" Area", "  Population ", "  Highways ", "  Internet users ", " Birth rate"])
hvr_name_col = "Country"

fig = px.scatter(df, x=x_var, y=y_var, size=size_var, color=clr, hover_name=hvr_name_col,
                 log_x=True, size_max=60)

fig.update_layout(
    title= "Bubble Chart")
#     xaxis_title="GDP per capita",
#     yaxis_title="Life expectancy"

st.plotly_chart(fig)

#dropdown list
select_col = st.selectbox("List Kolom", df.columns)

st.write(df[select_col])
