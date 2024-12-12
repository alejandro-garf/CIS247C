# WeatherGUI.py

import tkinter as tk
from tkinter import messagebox
from WeatherMockData import WeatherDataFetcher
from ProcessData import WeatherDataManager
from WeatherApp import california_station_codes_with_cities


class WeatherAppGUI:
    def __init__(self, main_window):
        self.wdf = WeatherDataFetcher()
        self.wdm = WeatherDataManager('weather_data.pkl')
        self.main_window = main_window
        self.main_window.title("California Weather Data")

        # Frames
        listbox_frame = tk.Frame(self.main_window, padx="10", pady="10")
        listbox_frame.pack(fill='x', expand=True)

        button_frame = tk.Frame(self.main_window, padx="10", pady="10")
        button_frame.pack(fill='x')

        display_frame = tk.Frame(self.main_window, padx="10", pady="10")
        display_frame.pack(fill='both', expand=True)

        # Station ListBox
        self.station_listbox_label = tk.Label(listbox_frame, text="Select a Station:")
        self.station_listbox_label.pack()
        self.station_listbox = tk.Listbox(listbox_frame)
        self.station_listbox.pack(side='left', fill='both', expand=True)
        for station_code in california_station_codes_with_cities:
            self.station_listbox.insert(tk.END, f"{station_code} - {california_station_codes_with_cities[station_code]}")
        self._scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        self._scrollbar.pack(side='right', fill=tk.Y)
        self._scrollbar.config(command=self.station_listbox.yview)

        # Live Data Button
        self.live_data_button = tk.Button(button_frame, text="Live Weather Data",
                                          command=lambda: self.fetch_weather_data("live"))
        self.live_data_button.pack(side='left', expand=True)

        # Historical Data Button
        self.csv_data_button = tk.Button(button_frame, text="Historical Data",
                                         command=lambda: self.fetch_weather_data("historical"))
        self.csv_data_button.pack(side='left', expand=True)

        # Forecast Data Button
        self.csv_data_button = tk.Button(button_frame, text="Forecast Data",
                                         command=lambda: self.fetch_weather_data("forecast"))
        self.csv_data_button.pack(side='left', expand=True)

        # Display Format Button
        self.manager_details_button = tk.Button(button_frame, text="Data Format",
                                                command=self.display_manager_details)
        self.manager_details_button.pack(side='left', expand=True)

        # Weather Data Display
        self.weather_data_display = tk.Text(display_frame, height=15, width=50)
        self.weather_data_display.pack()

    def fetch_weather_data(self, button_type):
        selected_station_index = self.station_listbox.curselection()
        if not selected_station_index:
            messagebox.showinfo("Info", "Please select a weather station.")
            return

        station_code = self.station_listbox.get(selected_station_index).split(' - ')[0]
        try:
            if button_type == "live":
                station_weather_data = self.wdf.fetch_weather_data(station_code)
            elif button_type == "historical":
                station_weather_data = self.wdm.get_most_recent_data_for_station(station_code)
            else:
                raise ValueError("Invalid data type specified")
            if station_weather_data:
                self.display_weather_data(station_weather_data, station_code)
            else:
                self.weather_data_display.delete(1.0, tk.END)
                self.weather_data_display.insert(tk.END, f"No Data")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_weather_data(self, weather_data, station_code):
        city_name = california_station_codes_with_cities.get(station_code, 'Unknown City')
        self.weather_data_display.delete(1.0, tk.END)
        self.weather_data_display.insert(tk.END, f"Weather Data for {station_code} ({city_name}):\n")
        for key, wd_value in weather_data.items():
            self.weather_data_display.insert(tk.END, f"{key}: {wd_value}\n")

    def display_manager_details(self):
        manager_details = str(self.wdm)
        messagebox.showinfo("Format Details", manager_details)


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()


