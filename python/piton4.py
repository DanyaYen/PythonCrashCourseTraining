import sys

cities = {
    "Kyiv": {
        'Country': 'Ukraine',
        'Population': '3,000,000',
        'Famous person in': 'Zelensky',
        'Status': 'capital',
        'Average temp': '20',
    },
    "London": {
         'Country': 'Great Britain',
        'Population': '12,000,000',
        'Famous person in': 'Churchill',
        'Status': 'capital',
        'Average temp': '10',
    },
    "LA" : {
         'Country': 'USA',
        'Population': '6,000,000',
        'Famous person in': 'Billie Eilish',
        'Status': 'Most named city',
        'Average temp': '30',
    },
    "Tokyo": {
         'Country': 'Japan',
        'Population': '15,000,000',
        'Famous person in': 'Miyazaki',
        'Status': 'capital',
        'Average temp': '21',
    }, 
    "Sydney" : {
         'Country': 'Australia',
        'Population': '5,000,000',
        'Famous person in': 'Hugh Jackman',
        'Status': 'almost capital',
        'Average temp': '27',
    },
}

v1 = {
    'q1': ['Russia', 'USA', 'Ukraine', 'China'],
    'q2': ['10,000,000', '100,000', '5,000,000', '3,000,000'],
    'q3': ['Putin', 'Zelensky', 'Trump', 'Zeus'],
    'q4': ['Capital', 'unknown city', 'biggest in EU', 'biden administration'],
    'q5': ['100', '20', '10', '0'],
}

v2 = {
    'q1': ['America', 'USA', 'Ukraine', 'Great Britain'],
    'q2': ['10,000,000', '1,000,000', '12,000,000', '7,000,000'],
    'q3': ['Kim Jong Un', 'Churchill', 'Mike Tyson', 'Adolf'],
    'q4': ['Capital', 'Village', 'biggest in Africa', 'Hot city'],
    'q5': ['100', '20', '10', '0'],
}

v3 = {
    'q1': ['Brazil', 'USA', 'Ukraine', 'China'],
    'q2': ['20,000,000', '6,000,000', '8,000,000', '4,000,000'],
    'q3': ['Putin', 'Obama', 'Billie Eilish', 'Tony Stark'],
    'q4': ['Capital', 'Most named city', 'biggest in EU', 'biden administration'],
    'q5': ['40', '20', '10', '30'],
}

v4 = {
    'q1': ['Argentina', 'USA', 'Japan', 'China'],
    'q2': ['15,000,000', '20,000,000', '5,000,000', '3,000,000'],
    'q3': ['Aizen', 'Miyazaki', 'Gojo', 'Naruto'],
    'q4': ['Capital', 'unknown city', 'coldest in the world', 'nohomo administration'],
    'q5': ['28', '21', '19', '13'],
}

v5 = {
    'q1': ['Russia', 'Australia', 'Ukraine', 'Dubai'],
    'q2': ['10,000,000', '100,000', '5,000,000', '3,000,000'],
    'q3': ['Drake', 'Zelensky', 'Hugh Jackman', 'Kenguru'],
    'q4': ['Capital', 'almost capital', 'biggest in EU', 'biden administration'],
    'q5': ['21', '27', '18', '30'],
}

def play_city_quiz(city):
    z = city
    B = 0  
    streak = 0
    print(f'Whoa, you chose {z}, let\'s try!')

    questions = [
        ('In which country is {} located?', 'Country', 'q1'),
        ('How many people live in {} (around to million)?', 'Population', 'q2'),
        ('Who is a famous person from {}?', 'Famous person in', 'q3'),
        ('What is the status of {}?', 'Status', 'q4'),
        ('What is the average temperature in {}?', 'Average temp', 'q5')
    ]

    city_index = list(cities.keys()).index(z)
    v = [v1, v2, v3, v4, v5][city_index]

    for i, (question, key, q_key) in enumerate(questions, 1):
        print(question.format(z))
        print('Variants:', ', '.join(v[q_key]))
        answer = input("Enter your answer: ").strip()

        if answer.lower() == "dnr":
            B += 1000000
            print("Whoa! You found the way!")
            print('All treasure is yours:', B)
            return B, streak

        if answer.replace(",", "").strip().lower() == cities[z][key].replace(",", "").lower():
            B += 1
            streak += 1
            if streak > 1:
                B += streak - 1
            print("Correct!")
        else:
            streak = 0
            print(f"Incorrect! The correct answer is: {cities[z][key]}")

        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f"Thank you for playing! Your final score is: {B}! Your final streak is: {streak}!")
    return B, streak

def play_game():
    while True:
        print('Hey there! Below you have the list of some cities and you need to guess fun facts! Reward included')
        print('When ready press 1\nTo check rules press 2\nTo quit press 3')
        x = input()

        if x == '1':
            print('Here is the list, please choose one:')
            for i, city in enumerate(cities.keys(), 1):
                print(f"{i}. {city}")
            print("Choose the city with the number from the list")
            y = input()
            if y.isdigit() and 1 <= int(y) <= len(cities):
                city = list(cities.keys())[int(y) - 1]
                play_city_quiz(city)
            else:
                print("Invalid choice. Please try again.")
        elif x == '2':
            print('In this quiz you need to give correct answers.')
            print('1 correct answer - 1$, streaks increase your score/balance')
            print('If you want to get your money you need to make a transaction in the app')
            input("Press Enter to continue...")
        elif x == '3':
            print("Thank you for playing! Goodbye!")
            sys.exit()
        else:
            print('Invalid input. Please press 1, 2, or 3.')
        
        play_again = input("Do you want to play again? (1/2): ").lower()
        if play_again != '1':
            print("Thank you for playing! Goodbye!")
            break
if __name__ == "__main__":
    play_game()