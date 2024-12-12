# ProcessData.py
# Alejandro Fonseca - Exam 3

import pickle


class WeatherDataManager:
    def __init__(self, filename):
        """
        Initialize the WeatherDataManager with a filename.
        Args:
            filename (str): Name of the pickle file to read/write data.
        """
        self.pickle_filename = filename

    def write_to_pickle(self, data_list):
        """
        Write weather data to a pickle file.
        Args:
            data_list (list): List of weather data dictionaries.
        """
        with open(self.pickle_filename, 'wb') as pickle_file:
            pickle.dump(data_list, pickle_file)
            print(f"Data written to {self.pickle_filename}.")

    def read_from_pickle(self):
        """
        Read weather data from a pickle file.
        Returns:
            list: List of weather data dictionaries.
        """
        try:
            with open(self.pickle_filename, 'rb') as pickle_file:
                return pickle.load(pickle_file)
        except FileNotFoundError:
            print(f"The file {self.pickle_filename} was not found.")
            return []
        except pickle.UnpicklingError as e:
            print(f"An error occurred while unpickling: {e}")
            return []

    def append_to_pickle(self, new_data):
        """
        Append new data to a pickle file.
        Args:
            new_data (dict): New weather data to append.
        """
        try:
            all_data = self.read_from_pickle()
            all_data.append(new_data)
            self.write_to_pickle(all_data)
        except Exception as e:
            print(f"An error occurred while appending data: {e}")

    def get_most_recent_data_for_station(self, station_code):
        """
        Get the most recent weather data for a specific station.
        Args:
            station_code (str): Station code to filter data.
        Returns:
            dict: Most recent weather data for the station.
        """
        all_data = self.read_from_pickle()
        station_data = [entry for entry in all_data if entry["Station"] == station_code]
        if not station_data:
            return None
        most_recent_data = max(station_data, key=lambda x: x["Timestamp"])
        return most_recent_data


    @staticmethod
    def load_data(filename):
        """
        Load data from a specified pickle file.
        Args:
            filename (str): The name of the pickle file to read.
        Returns:
            Any: The unpickled data.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"The file {filename} was not found.")
            return None
        except pickle.UnpicklingError as e:
            print(f"An error occurred while unpickling {filename}: {e}")
            return None
