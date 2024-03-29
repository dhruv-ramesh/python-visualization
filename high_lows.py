import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'weather_data/death_valley_2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    lows = []
    dates = []
    for row in reader:
        try:
            highs.append(int(row[3]))
            lows.append(int(row[4]))
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        except ValueError:
            print('missing_data')

# Plot data
fig = plt.figure(dpi = 128, figsize =(10,6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Format the plot
plt.title('Daily high and low temperatures-2021\n Death Valley, CA', fontsize = 16)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
