import plotly.express as px
from dice import Die

die_0 = Die()
die_1 = Die(8)
die_2 = Die(10)

results = []

for roll_num in range(10_000):
    result = die_1.roll() * die_2.roll() * die_0.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides * die_2.num_sides * die_0.num_sides
poss_results = range(1, max_result+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

title = "Results of Rolling a D6 and a D10 and D8 10,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()