import random

while True: 
    alien_color = ["green", "red", "yellow"]
    chances = [55, 35, 10]
    backs = 0

    print("Welcome to the Alien Color Game!")

    while backs != 'dead':
        user_input = input("Enter '1' to play or 'q' to quit: ")
        
        if user_input.lower() == 'q':
            print("Thanks for playing! Final balance: {}".format(backs))
            break
        elif user_input != '1':
            print("Invalid input. Please enter '1' to play or 'q' to quit.")
            continue

        chosen_color = random.choices(alien_color, weights=chances, k=1)[0]
        
        if chosen_color == "green":
            backs += 5
            print("congrats, youve earned 5$")
            print("\n Your balance: {}".format(backs))
        elif chosen_color == "red":
            backs -= 5
            print("oh no! youve received damage -5$")
            print("\n Your balance: {}".format(backs))
        else:
            backs = 'dead'
            print("fuck no! Youve been elimineted by enemy")
            print("money has gone( \n One more try?")

    if backs == 'dead':
        print("Game Over!")

    play_again = input("Do you want to play again? (1/2): ")
    if play_again.lower() != '1':
        print("Thanks for playing! Goodbye!")
        break