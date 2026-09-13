import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('happy.csv')
columns = df.columns

st.title('Temperature Calculator')
x_axis = st.selectbox('Select the data for X-axis', columns[0:5])
y_axis = st.selectbox('Select the data for Y-axis', columns[0:5])

df_x = df[x_axis]
df_y = df[y_axis]

st.subheader(f'x-axis {x_axis} and y-axis {y_axis}')

figure = px.scatter(x=df_x, y=df_y, labels=dict(x=x_axis, y=y_axis))
st.plotly_chart(figure)
