import random
names = ["Gojo", "Aizen", "Kamino", "Martinez"]
print(f'Hello {random.choice(names)}!')
names.append(["kill=ua", "Itache", "light"])
print(names)
print(f'Hello {random.choice(names[-1])}!')
names.insert(1, "Satoru")
print(names)
names_pop = names.pop()
print(names_pop)
names[3] = "Goku"
print(names)
names.sort(reverse=True)
print(names)
print(len(names))
