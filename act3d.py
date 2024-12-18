import streamlit as at
import requests

st.title("weather Dashboard")
st.subheader("Load data from openweathermap.org")
user_input = st.text_input("enter town name:")


api_url = f'https://api.apenweathermap.org/data/2.5/weather?q={user_input}&appid=ac2d2697871c0160f61dec4ef11b36fg'

try:
    response = request.get(api_url)
    if response.status_code == 200:
        api_data = response.json()
        st.subheader("Raw API Data")
        st.json(api_data, expanded=False)
        weather = api_data['weather'][0]['main']
        temperature = api_data['main']['temp'] - 273.15
        weather
        temperature
        
        town_placeholder = st.empty()
        temperature_placeholder = st.empty()
        weather_placeholder = st.empty()
        with town_placeholder:
            st.subheader(f'Current Temperature at {user_input}")
        with temperature_placeholder:
            st.metric(label="Temperature (*C)", value=f"{weather}")
        with weather_place holder:
            st.metric(label="weather", value=f'{weather}")

except Exception as e:
    st.Error(f"Error fetching data: {e}")
    