# WeatherData.py

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

    """
    Fetch weather data from an API endpoint.
    Args:
        station_code (str): 4 digit code for NWS locations.
    Returns:
        dict: The weather data in JSON format.
    """
    def fetch_weather_data(self, station_code, coordinates=False):  # https://api.weather.gov/openapi.json
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
                "Description": properties["textDescription"]
            }

            label_mapping = {
                "temperature": "Temperature",
                "dewpoint": "Dewpoint",
                "windSpeed": "Wind Speed",
                "relativeHumidity": "Humidity"
            }

            for prop, label in label_mapping.items():
                value = properties[prop]["value"]
                unit_code = properties[prop]["unitCode"]
                unit = self.convert_unit(unit_code)

                weather_data[label] = f"{value} {unit}" if value is not None else "N/A"

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
        if forecast_data:
            target_time = datetime.now(timezone.utc) + timedelta(hours=24)
            closest_period = None
            min_time_diff = timedelta.max
            for period in forecast_data['properties']['periods']:
                start_time = datetime.fromisoformat(period['startTime'])
                time_diff = abs(start_time - target_time)
                if time_diff < min_time_diff:
                    min_time_diff = time_diff
                    closest_period = period

            if closest_period:
                forecast_info = {
                    "Timestamp": closest_period['startTime'],
                    "Temperature": f"{closest_period['temperature']} {self.convert_unit(closest_period['temperatureUnit'])}",
                    "Dewpoint": f"{closest_period['dewpoint']['value']} {self.convert_unit(closest_period['dewpoint']['unitCode'])}",
                    "Wind Speed": closest_period['windSpeed'],
                    "Humidity": f"{closest_period['relativeHumidity']['value']} {self.convert_unit(closest_period['relativeHumidity']['unitCode'])}",
                    "Description": closest_period['detailedForecast']
                }
                return forecast_info
        return {}


if __name__ == "__main__":
    fetcher = WeatherDataFetcher()
    test_station_code = "KSFO"  # San Francisco as an example
    station_data = fetcher.fetch_weather_data(test_station_code)

    if station_data:
        print(f"Weather Data for station {test_station_code}:\n")
        print(station_data)
