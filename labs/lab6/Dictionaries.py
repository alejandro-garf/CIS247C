# Dictionaries.py

station_codes_dictionary = {"KLAX": "Los Angeles", "KSDM": "San Diego"}
print(station_codes_dictionary)

station_codes_dictionary["KSFO"] = "San Francisco"
print(station_codes_dictionary)

values_view = station_codes_dictionary.values()
print(list(values_view))

items_view = station_codes_dictionary.items()
print(list(items_view))

removed_city = station_codes_dictionary.pop("KSFO") # or del
print("After pop(): ", station_codes_dictionary, "Removed city: ", removed_city)

city = station_codes_dictionary["KLAX"]
print(city)

city = station_codes_dictionary.get("KSFO", "City not found")
print(city)

exists = "KSDM" in station_codes_dictionary
print(exists)

for code in station_codes_dictionary:
    print(code)
