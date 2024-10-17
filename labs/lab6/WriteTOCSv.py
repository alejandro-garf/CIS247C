# WriteToCSV.py
#Lab 6 by Alejandro Fonseca

import csv
from datetime import datetime
import random

station_codes = {
    "KMYV": "Marysville",
    "KSMX": "Santa Maria",
    "KWVI": "Watsonville",
    "KLVK": "Livermore",
    "KFOT": "Fortuna"
}

# Open a new CSV file to write
with open('sample_weather_data.csv', 'w', newline='') as file:
    # Make a writer object
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Station', 'City', 'Timestamp', 'Temperature'])

    # Get current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Write data for each station
    for station, city in station_codes.items():
        # Make a random temperature between 0 and 40
        temperature = random.randint(0, 40)

        # Write the row
        writer.writerow([station, city, current_time, temperature])

print("done")