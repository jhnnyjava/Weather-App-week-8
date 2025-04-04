import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_weather(city):
    url = f"{os.getenv('BASE_URL')}/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    print(f"Weather in {city}: {weather['main']['temp']}°C")
def get_forecast(city):
    url = f"{os.getenv('BASE_URL')}/forecast?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    return requests.get(url).json()
def show_forecast(data):
    for day in data['list'][::8]:  # Get daily (3-hour intervals)
        date = day['dt_txt'].split()[0]
        print(f"{date}: {day['main']['temp']}°C")
try:
    forecast = get_forecast(city)
    show_forecast(forecast)
except Exception as e:
    print(f"Forecast error: {e}")
WEATHER_ICONS = {
    'clear': '☀️',
    'clouds': '☁️',
    'rain': '🌧️',
    # Add more mappings
}

def get_icon(weather_condition):
    return WEATHER_ICONS.get(weather_condition.lower(), '🌈')
def display_temp(temp, units):
    return f"{temp}°C" if units == "metric" else f"{celsius_to_fahrenheit(temp)}°F"
import logging
logging.basicConfig(filename='weather.log', level=logging.INFO)

def log_weather(city):
    logging.info(f"Weather checked for {city}")
