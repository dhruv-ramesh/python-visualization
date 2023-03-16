import csv
import matplotlib.pyplot as plt

filename = 'weather_data/sitka_weather_07-2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        highs.append(int(row[4]))

# Plot data
fig = plt.figure(dpi = 128, figsize =(10,6))
plt.plot(highs, c = 'red')

# Format the plot
plt.title('Daily high temperature, July 2021', fontsize = 16)
plt.xlabel('', fontsize = 16)
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
