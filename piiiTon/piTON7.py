from pathlib import Path
import re
path = Path('D:\CS\piiiTon\py.txt')
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(re.sub(r'python', 'C#', line, flags=re.IGNORECASE))

guest_book_path = Path('D:\CS\piiiTon\py.txt')
guest_names = []

while True:
    x = input('What is your name? ')
    if x == '':
        break
    guest_names.append(x)
    print('Would you like to write another name? (press Enter to finish)')

# Writing guest names to the file
guest_book_path.write_text('\n'.join(guest_names))
print("Guest book has been updated.")