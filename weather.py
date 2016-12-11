import forecastio
from geopy.geocoders import Nominatim
import os  # use this to import your secret keys

# use .env file to hide your forecast.io api key
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
    api_key = os.environ.get('FORECAST_API_KEY')
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° at {}".format(summary, temperature, address)