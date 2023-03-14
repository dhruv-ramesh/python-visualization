from die import Die
import pygal

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

# Make some rolls and store results in a list
results = []
max_result = die_1.num_sides + die_2.num_sides

for roll_num in range(50000):
    results.append(die_1.roll() + die_2.roll())

# Analyze the results
frequencies = []
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times"
hist.xlabels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual2.svg')
