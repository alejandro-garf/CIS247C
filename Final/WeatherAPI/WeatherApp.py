# WeatherApp.py

from ProcessData import WeatherDataManager
from WeatherData import WeatherDataFetcher


# List of station codes in California from https://www.cnrfc.noaa.gov/metar.php#CALIFORNIA
california_station_codes_with_cities = WeatherDataManager.load_data("california_station_codes.pkl")


def main():
    all_weather_data = []

    for station_code in california_station_codes_with_cities:
        try:
            station_weather_data = WeatherDataFetcher.fetch_weather_data(station_code)
        except Exception as e:
            print(f"An error occurred while fetching data for station {station_code}: {e}")
            continue

        if station_weather_data:
            city_name = california_station_codes_with_cities.get(station_code, 'Unknown City')
            print(f"Weather Data for station {station_code} ({city_name}):")
            for key, wd_value in station_weather_data.items():
                print(f"{key}: {wd_value}")
            print("----")

            station_weather_data["Station"] = station_code
            station_weather_data["City"] = city_name
            all_weather_data.append(station_weather_data)
            WeatherDataManager.append_to_pickle(station_weather_data)

    print("\nAll weather data added:")
    print(all_weather_data)


if __name__ == "__main__":
    main()