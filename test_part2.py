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
ski_seasons_data = count_skiable_days_per_season(single_weather_station, snow_depth_index=3, date_index=2)
for season, days in ski_seasons_data.items():
    print(f"Winter season {season}-{season+1} had {days} skiing days.")


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

# task d) 
filtered_ski_seasons_data = count_skiable_days_per_season(single_weather_station, snow_depth_index=3, date_index=2, min_days=200)
filtered_ski_year,filtered_ski_days = [],[]
for season, days in filtered_ski_seasons_data.items():
    filtered_ski_year.append(season);filtered_ski_days.append(days)

filtered_ski_year, filtered_ski_days = [int(year) for year in filtered_ski_year], [int(year) for year in filtered_ski_days]

a, b = calculate_trend(filtered_ski_year, filtered_ski_days)

# print(f"{filtered_ski_year[0]} - {filtered_ski_year[-1]}")

# Generate two points for the trend line
start_year = min(filtered_ski_year)
end_year = max(filtered_ski_year)
trend_start = a * start_year + b
trend_end = a * end_year + b

plt.figure(1)

# Plot the actual snow depth data
plt.scatter(filtered_ski_year, filtered_ski_days, color='blue', label='Actual Ski Days')

# Plot the trend line
plt.plot([start_year, end_year], [trend_start, trend_end], color='red', label='Trend Line')

# Label the plot
plt.xlabel('Year')
plt.ylabel('Number of Days with Skiers')
plt.title('Snow Depth and Trend Line')
plt.legend()

# task e) Plant growth
temp_dict = filter_temp_data(single_weather_station,300)

# converting dict to lists for plotting
plantgrowth = []
years1 = list(temp_dict.keys())
for lst in temp_dict:
    plantgrowth.append(calculate_plantgrowth(temp_dict[lst]))

plt.figure(2)
plt.bar(years1,plantgrowth)
plt.xlabel('Year')
plt.ylabel('Sum plantgrowth')
plt.title('Total plantgrowth per year')

# task f) Drought
dry_dict = find_dry_season(single_weather_station,300)

# converting dict to lists for plotting
dry_list = []
years2 = list(dry_dict.keys())
for keys in dry_dict:
    dry_list.append(dry_dict[keys])

plt.figure(3)
plt.grid()
plt.plot(years2,dry_list)
plt.xlabel('Year')
plt.ylabel('Longest time without rain')
plt.title('Longest time without rain by year')

# task g) Data analysis and plotting code

valid_years = {}  

for row in single_weather_station[1:]:  
    try:
        year = int(row[2].split('.')[2])  
        skydekke = float(row[6].replace(',', '.'))  

        
        if year not in valid_years:
            valid_years[year] = {'penvaersdager': 0, 'days_with_data': 0}

        valid_years[year]['days_with_data'] += 1

        if skydekke <= 3:
            valid_years[year]['penvaersdager'] += 1
    except (ValueError, IndexError):
        pass

valid_years = {year: data for year, data in valid_years.items() if data['days_with_data'] >= 300}

years = list(valid_years.keys())
penvaersdager = [data['penvaersdager'] for data in valid_years.values()]

plt.figure(4)
plt.bar(years, penvaersdager)
plt.xlabel('Year')
plt.ylabel('Number of penværsdager')
plt.title('Number of penværsdager per year')


 # task h)

wind_data = analyze_wind_data(single_weather_station)

# def plot_wind_data(data):
years = list(wind_data.keys())
highest_wind_speeds = [max(wind_data[year]['wind_speeds']) for year in years]
median_wind_speeds = [sorted(wind_data[year]['wind_speeds'])[len(wind_data[year]['wind_speeds']) // 2] for year in years]


plt.figure(5,figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(years, highest_wind_speeds, marker='o')
plt.xlabel('Year')
plt.ylabel('Highest Wind Speed (m/s)')
plt.title('Highest Wind Speed per Year')


plt.subplot(2, 1, 2)
plt.plot(years, median_wind_speeds, marker='o', color='orange')
plt.xlabel('Year')
plt.ylabel('Median Wind Speed (m/s)')
plt.title('Median Wind Speed per Year')

plt.tight_layout()


# task i)
monthly_avg_temps = calculate_monthly_averages(single_weather_station, temp_index=4, date_index=2)
sorted_months = sorted(monthly_avg_temps.keys(), key=lambda d: datetime.strptime(d, '%B %Y'))

# monthly average
sorted_avg_temps = [monthly_avg_temps[month] for month in sorted_months]

# calculate the differences
temp_differences = calculate_differences(sorted_avg_temps)


# Plotting the average temperatures
plt.figure(6,figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(sorted_months, sorted_avg_temps, label='Average Monthly Temperature', color='blue', marker='o')
plt.xticks(rotation=45)
plt.xlabel('Month and Year')
plt.ylabel('Average Temperature')
plt.title('Monthly Average Temperatures')

# plotting the differences month to month
plt.subplot(2, 1, 2)
plt.plot(sorted_months[1:], temp_differences, label='Month-to-month Temperature Differences', color='red', marker='x')
plt.xticks(rotation=45)
plt.xlabel('Month and Year')
plt.ylabel('Temperature Difference')
plt.title('Monthly Temperature Differences')
plt.legend()
plt.tight_layout()

# Plot all
plt.show()