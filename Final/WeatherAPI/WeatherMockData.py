# WeatherData.py

from ProcessData import WeatherDataManager


class WeatherDataFetcher:
    """
    Fetch mock weather data.
    Args:
        station_code (str): 4 digit code for NWS locations.
    Returns:
        dict: Mock weather data mimicking API JSON format.
    """
    def fetch_weather_data(self, station_code):
        return WeatherDataManager.load_data("mock_data.pkl")


if __name__ == "__main__":
    fetcher = WeatherDataFetcher()
    test_station_code = "KSFO"  # San Francisco as an example
    station_data = fetcher.fetch_weather_data(test_station_code)

    if station_data:
        print(station_data)
