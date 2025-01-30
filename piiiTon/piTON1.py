def city_country(x1, x2):
    full_name = f"{x1} {x2}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    x1 = input("First name: ")
    if x1 == 'q':
            break
    x2 = input("Last name: ")
    if x2 == 'q':
            break
    formatted_name = city_country(x1, x2)
    print(f"\nHello, {formatted_name}!")