import os
from list_operations import *

dirpath = os.path.dirname(os.path.realpath(__file__))

# weather stations.
single_weather_station = []
five_weather_stations = []

# task a
# if you're using linux turn "\" to "/" in the down below function. 
def initialize_data():
    with open(f'{dirpath}\snoedybder_vaer_en_stasjon_dogn.csv', 'r') as f1, open(f'{dirpath}\snoedybder_vaer_fem_stasjoner_dogn.csv', 'r') as f2:
        global single_weather_station, five_weather_stations
        single_weather_station = list(csv.reader(f1, delimiter=';'))
        five_weather_stations = list(csv.reader(f2,  delimiter=';'))
initialize_data()

# task b
# TODO: Unbreakand and uncomment the code before delivery!
ski_seasons_data = count_skiable_days_per_season(single_weather_station, snow_depth_index=3, date_index=2)
for season, days in ski_seasons_data.items():
    # print(f"Winter season {season}-{season+1} had {days} skiing days.")
    break 

# task c
ski_year,ski_days = [],[]
for season, days in ski_seasons_data.items():
    ski_year.append(season);ski_days.append(days)
ski_trend =calculate_trend(ski_year,ski_days)[0]
print(f"C: The trend of skiing days is:{ski_trend}",end="")
if (ski_trend>0):
    print(", Thus the trend is rising")
elif (ski_trend<0):
    print(", Thus the trend is decreasing")
else:
    print(", Thus there is no trend")

# task d

