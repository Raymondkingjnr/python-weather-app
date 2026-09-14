import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input('Place: ')
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f'{option} for the next {days} days in {place}')

if place:
   try:
       data = get_data(place,days)
       if option == 'Temperature':
            temperature = [item['main']['temp'] / 10 for item in data]
            date = [date['dt_txt'] for date in data]
            figure = px.line(x=date, y=temperature, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)
       if option == 'Sky':
           images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png" }
           sky = [item['weather'][0]['main'] for item in data]
           image_path = [images[condition] for condition in sky ]
           st.image(image_path, width=110)
   except KeyError:
       st.error("That place does not exist")

       # for item in sky:
       #     if item == 'Clouds':
       #        st.image('images/cloud.png', width=115)
       #     elif item == "Rain":
       #         st.image('images/rain.png', width=115)
       #     elif item == "Snow":
       #         st.image('images/snow.png', width=115)
       #     elif item == "Clear":
       #         st.image('images/clear.png', width=115)
       #     else:
       #         st.image('images/clear.png', width=115)