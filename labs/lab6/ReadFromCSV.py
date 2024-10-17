# ReadFromCSV.py

import csv

# Make an empty dictionary to store station and city
station_city_dict = {}

# Open the CSV file to read
with open('sample_weather_data.csv', 'r') as file:
    # Make a reader object
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Read each row
    for row in reader:
        # Get station and city from the row
        station = row[0]
        city = row[1]

        # Add to dictionary
        station_city_dict[station] = city

# Print the dictionary
print("Station and City Dictionary:")
print(station_city_dict)

# Print each station and city
print("\nAll Stations and Cities:")
for station, city in station_city_dict.items():
    print(f"Station: {station}, City: {city}")