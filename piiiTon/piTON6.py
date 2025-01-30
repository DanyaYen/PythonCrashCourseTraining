import random

x = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

select = random.sample(x, 4)
y = ', '.join(map(str, select))
print(f'And the winner is {y}')