import csv


def read_from_csv(csv_filename):
    data_list = []
    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                data_list.append(row)
    except FileNotFoundError:
        print(f"File {csv_filename} not found")
    except csv.Error as e:
        print(f"An error occured while reading {csv_filename}:  {e}")

    return data_list

if __name__ == "__main__":
    read_data = read_from_csv("sample_weather_data.csv")

    print("data being read from csv: ")
    for row in read_data:
        print(row)



