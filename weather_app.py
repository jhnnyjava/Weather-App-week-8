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
