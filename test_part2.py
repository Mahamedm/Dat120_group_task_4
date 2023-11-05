import os
import csv
from list_operations import *

dirpath = os.path.dirname(os.path.realpath(__file__))

# weather stations.
single_weather_station = []
five_weather_stations = []
# print(f"{dirpath}\snoedybder_vaer_en_stasjon_dogn.csv")

# if you're using linux turn "\" to "/" in the down below function. 
def initialize_data():
    with open(f'{dirpath}\snoedybder_vaer_en_stasjon_dogn.csv', 'r') as f1, open(f'{dirpath}\snoedybder_vaer_fem_stasjoner_dogn.csv', 'r') as f2:
        global single_weather_station, five_weather_stations
        single_weather_station = list(csv.reader(f1))
        five_weather_stations = list(csv.reader(f2))
initialize_data()

# the csv files and their data are contained in single_weather_station and five_weather_stations = [].
# print(single_weather_station[1])

# Task a...

