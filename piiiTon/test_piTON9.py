import json
import os

def get_stored_number():
    """Get stored number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_new_number():
    """Prompt for a new favorite number."""
    number = input("What's your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(int(number), f)
    return int(number)

def favorite_number():
    """Get and print the favorite number."""
    number = get_stored_number()
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        number = get_new_number()
        print(f"I'll remember that {number} is your favorite number.")

favorite_number()