# AppendToCSV.py

import csv
from datetime import datetime
import random

# Make a dictionary for new station codes and cities
new_stations = {
    "KMMH": "Mammoth Lakes",
    "KHWD": "Hayward",
    "KRNO": "Reno",
    "KOAK": "Oakland"
}

# Open the CSV file to append
with open('sample_weather_data.csv', 'a', newline='') as file:
    # Make a writer object
    writer = csv.writer(file)

    # Get current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Write data for each new station
    for station, city in new_stations.items():
        # Make a random temperature between 0 and 40
        temperature = random.randint(0, 40)

        # Write the row
        writer.writerow([station, city, current_time, temperature])

print("New data has been added to the CSV file!")

# Let's read and print the updated file
print("\nUpdated CSV file contents:")
with open('sample_weather_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)