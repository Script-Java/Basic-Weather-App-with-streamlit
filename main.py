import streamlit as st
import requests
import json
from PIL import Image

key = "09825b826bf30441cf81c0bf19cd0743"
st.title("Weather App")
city_name = st.text_input("Please input your city then press enter", placeholder="City")
api = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'
response = requests.get(api).json()

city_name = response["name"]
weather_type = response["weather"][0]["main"]

city_name = response["name"]
weather_type = response["weather"][0]["main"]
weather_description = response["weather"][0]["description"]
temp = int(response["main"]["temp"] - 273.15) * 9 / 5 + 32
feels_like = int(response["main"]["feels_like"] - 273.15) * 9 / 5 + 32
min_temp = int(response["main"]["temp_min"] - 273.15) * 9 / 5 + 32
max_temp = int(response["main"]["temp_max"] - 273.15) * 9 / 5 + 32
humidity = response["main"]["humidity"]

st.title(f'{city_name}')
# image section
#if weather_type == "Clouds":
#    image = Image.open('img/cloud.png')
#    st.image(image,width=400)
st.write(f'#### Temperature: {temp}')
st.write(f'#### Weather Type:  {weather_type}')
st.write(f'#### Weather Description:  {weather_description}')
st.write(f'#### Feels like: {feels_like}')
st.write(f'#### Minimum Temperature: {min_temp}')
st.write(f'#### Maximum Temperatrue: {max_temp}')
st.write(f'#### Humidity: {humidity}%')


