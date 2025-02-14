import matplotlib.pyplot as plt
from broke_walk import RandomWalk

while True: 
    rw = RandomWalk(50_000)
    rw.fill_walk()
    plt.style.use('default')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    edgecolors='none', s=1)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break