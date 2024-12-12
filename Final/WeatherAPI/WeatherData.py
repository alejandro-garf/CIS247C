# WeatherData.py
# Alejandro Fonseca - Exam 3

import requests
import json
from datetime import datetime, timedelta, timezone


class WeatherDataFetcher:
    def __init__(self, base_url="https://api.weather.gov/"):
        self.base_url = base_url
        self.unit_mappings = {
            "wmoUnit:degC": "°C",
            "wmoUnit:km_h-1": "km/h",
            "wmoUnit:percent": "%",
            "wmoUnit:Pa": "Pa",
        }

    def convert_unit(self, unit_code):
        return self.unit_mappings.get(unit_code, unit_code)

    def fetch_weather_data(self, station_code, coordinates=False):
        url = f"{self.base_url}stations/{station_code}/observations/latest"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if coordinates:
                return self.parse_forecast_data(data)
            else:
                return self.parse_weather_data(data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {station_code}: {e}")
            return None
        except json.JSONDecodeError:
            print(f"Invalid JSON response for {station_code}")
            return None

    def parse_weather_data(self, data):
        try:
            properties = data["properties"]
            weather_data = {
                "Timestamp": properties.get("timestamp", "N/A"),
                "Description": properties["textDescription"],
                "Temperature": f"{properties['temperature']['value']} °C",
                "Dewpoint": f"{properties['dewpoint']['value']} °C",
                "Wind Speed": f"{properties['windSpeed']['value']} km/h",
                "Humidity": f"{properties['relativeHumidity']['value']} %"
            }
            return weather_data
        except KeyError as e:
            print(f"Missing key in data: {e}")
            return None

    def get_forecast_data(self, lat, lon):
        try:
            points_url = f"{self.base_url}points/{lat},{lon}"
            response = requests.get(points_url)
            response.raise_for_status()
            points_data = response.json()

            # Get the forecast URL
            forecast_url = points_data['properties']['forecast']

            # Step 2: Get forecast data
            response = requests.get(forecast_url)
            response.raise_for_status()
            forecast_data = response.json()
            return forecast_data
        except Exception:
            return None

    def parse_forecast_data(self, data):
        lat = data['geometry']['coordinates'][1]
        lon = data['geometry']['coordinates'][0]
        forecast_data = self.get_forecast_data(lat, lon)

        if forecast_data and 'properties' in forecast_data and 'periods' in forecast_data['properties']:
            closest_period = forecast_data['properties']['periods'][0]  # Get the first period

            forecast_info = {
                "Timestamp": closest_period['startTime'],
                "Temperature": f"{closest_period['temperature']}",
                "Wind Speed": closest_period['windSpeed'],
                "Description": closest_period['detailedForecast']
            }
            return forecast_info
        return {}


if __name__ == "__main__":
    fetcher = WeatherDataFetcher()
    test_station_code = "KSFO"  # San Francisco as an example
    station_data = fetcher.fetch_weather_data(test_station_code)
    if station_data:
        print(station_data)