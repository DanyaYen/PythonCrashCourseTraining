while True:
    x1 = input("x1 (or 'q' to quit): ")
    if x1.lower() == 'q':
        break
    
    x2 = input("x2 (or 'q' to quit): ")
    if x2.lower() == 'q':
        break
    
    try:
        num1 = int(x1)
        num2 = int(x2)
        print(f"Result: {num1 + num2}")
    except ValueError:
        print("Please enter valid numbers.")