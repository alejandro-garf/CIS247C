import csv
import random
import datetime


#list of the station codes in California
california_station_codes = [
    "KACV", "KAAT", "KBFL", "KBUR", "KCCR", "KCIC",
]


def write_to_csv(data_list):
    with open('sample_weather_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(['Station', 'Timestamo', 'Temperature'])
        writer.writerows(data_list)

if __name__ == '__main__':
    mock_data_list = []

    for _ in range(100):
        station = random.choice(california_station_codes)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        temperature = random.randint(0, 40)
        data_entry = [station, timestamp, temperature]
        mock_data_list.append(data_entry)

    write_to_csv(mock_data_list)
