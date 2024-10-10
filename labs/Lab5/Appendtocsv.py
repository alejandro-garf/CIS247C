import csv
import random
import datetime

california_station_codes = [
    "KACV", "KAAT", "KBFL", "KBUR", "KCCR", "KCIC",
]

def append_to_csv(data_row, csv_filename='sample_weather_data.csv'):
   try:
        with open(csv_filename, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data_row)
   except FileNotFoundError:
       print(f"File {csv_filename} not found")
   except csv.Error as e:
       print(f"An error occured while writing to {csv_filename}:  {e}")

if __name__ == '__main__':
    station = random.choice(california_station_codes)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    temperature = random.randint(0, 40)
    data_entry = [station, timestamp, temperature]
    print(data_entry)
    append_to_csv(data_entry, "sample_weather_data.csv")



