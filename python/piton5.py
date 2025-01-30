favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

names = {'sarah', 'jack', 'jon', 'phil'}

for name in names:
    if name in favorite_languages:
        print(f"{name.title()}'s favorite language is {favorite_languages[name].title()}.")
    else:
        print(f"{name.title()}, please choose your favorite programming language.")

print("The following languages have been mentioned:")

for language in set(favorite_languages.keys()):
    print(language.title())