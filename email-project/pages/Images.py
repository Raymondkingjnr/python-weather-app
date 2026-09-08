import streamlit as st
import requests

st.set_page_config(layout="centered")

st.markdown(""""
  <style>
    .article-image {
        flex: 1;
        max-width: 120px;
    }
    .article-image img {
        width: 100%;
        height: 90px;
        object-fit: cover;
        border-radius: 10px;
    }
  </style>
""", unsafe_allow_html=True)

st.subheader("Today Image from nasa")

api_key = "sCZLk5OqHRcbtug6AEd4I6r4fJKRSMmpsryV4fmI"
url = "https://api.nasa.gov/planetary/apod?"\
       f"api_key={api_key}"
request = requests.get(url)
response = request.json()

image_url = response["url"]
title = response["title"]
explanation = response["explanation"]

image_path = "img.png"
res = requests.get(image_url)

with open(image_path, "wb") as f:
    f.write(res.content)

st.write(title)
st.image(image_path)
st.write(explanation)