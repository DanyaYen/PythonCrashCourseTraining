import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')
x = range(1, 6)
y = [i**3 for i in x]

fig, ax = plt.subplots()
ax.plot(x, y,  color = 'green', linewidth = 5 )
ax.scatter(x, y, c=y, cmap=plt.cm.Greens, s=20)
ax.set_title("cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("cube of Value", fontsize=14)
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')
ax.axis([0, 6, 0, 216])

plt.show()