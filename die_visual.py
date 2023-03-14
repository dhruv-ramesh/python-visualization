import pygal
from die import Die
from collections import defaultdict

# Create a D6
die1 = Die()
die2 = Die()

# Make some rolls and store the results in a list
results = []
for roll in range(100):
    results.append(die1.roll() + die2.roll())

# Analyze the results

frequencies = []
max_result = die1.num_sides + die2.num_sides
for val in range(2, max_result + 1):
    frequencies.append(results.count(val))

# Visualize the results

hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = list(str(x) for x in range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequencyof Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
