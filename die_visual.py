import pygal
from die import Die
from collections import defaultdict

# Create a D6
die = Die()

# Make some rolls and store the results in a list
results = []
for roll in range(100):
    results.append(die.roll())

# Analyze the results

frequencies = []
for val in range(1, die.num_sides + 1):
    frequencies.append(results.count(val))

# Visualize the results

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = list(str(x) for x in range(1, die.num_sides + 1))
hist.x_title = "Result"
hist.y_title = "Frequencyof Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
