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
        try:
            all_data = self.read_from_pickle()
            if not all_data:
                return None

            station_data = [entry for entry in all_data if entry.get("Station") == station_code]
            if not station_data:
                return None

            # Get most recent data
            most_recent_data = station_data[-1]  # Just get the last entry for now

            # Return data in the correct format
            return {
                "Timestamp": most_recent_data.get('timestamp', most_recent_data.get('Timestamp', 'N/A')),
                "Description": most_recent_data.get('textDescription', most_recent_data.get('Description', 'N/A')),
                "Temperature": most_recent_data.get('Temperature', 'N/A'),
                "Dewpoint": most_recent_data.get('Dewpoint', 'N/A'),
                "Wind Speed": most_recent_data.get('Wind Speed', 'N/A'),
                "Humidity": most_recent_data.get('Humidity', 'N/A'),
                "Station": most_recent_data.get('Station', 'N/A'),
                "City": most_recent_data.get('City', 'N/A')
            }
        except Exception as e:
            print(f"Error in get_most_recent_data_for_station: {e}")
            return None

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