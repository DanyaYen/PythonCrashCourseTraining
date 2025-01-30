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
    'q1': [
        'Russia', 'USA', 'Ukraine', 'China'
    ], 
    'q2': [
        '10,000,000', '100,000', '5,000,000', '3,000,000'
    ],
    'q3': [
        'Putin', 'Zelensky', 'Trump', 'Zeus'
    ], 
    'q4': [
        'Capital', 'unknown city', 'biggest in EU', 'biden administration'
    ], 
    'q5': [
        '100', '20', '10', '0'
    ], 
}

v2 ={
    'q1': [
        'America', 'USA', 'Ukraine', 'Great Britain'
    ], 
    'q2': [
        '10,000,000', '1,000,000', '12,000,000', '7,000,000'
    ],
    'q3': [
        'Kim Jong Un', 'Churchill', 'Mike Tyson', 'Adolf'
    ], 
    'q4': [
        'Capital', 'Village', 'biggest in Africa', 'Hot city'
    ], 
    'q5': [
        '100', '20', '10', '0'
    ], 
}

v3 = {
    'q1': [
        'Brazil', 'USA', 'Ukraine', 'China'
    ], 
    'q2': [
        '20,000,000', '6,000,000', '8,000,000', '4,000,000'
    ],
    'q3': [
        'Putin', 'Obama', 'Billie Eilish', 'Tony Stark'
    ], 
    'q4': [
        'Capital', 'Most named city', 'biggest in EU', 'biden administration'
    ], 
    'q5': [
        '40', '20', '10', '30'
    ], 
}

v4 = {
    'q1': [
        'Argentina', 'USA', 'Japan', 'China'
    ], 
    'q2': [
        '15,000,000', '20,000,000', '5,000,000', '3,000,000'
    ],
    'q3': [
        'Aizen', 'Miyadzaki', 'Gojo', 'Naruto'
    ], 
    'q4': [
        'Capital', 'unknown city', 'coldest in th world', 'nohomo administration'
    ], 
    'q5': [
        '28', '21', '19', '13'
    ], 
}

v5 = {
    'q1': [
        'Russia', 'Australia', 'Ukraine', 'Dubai'
    ], 
    'q2': [
        '10,000,000', '100,000', '5,000,000', '3,000,000'
    ],
    'q3': [
        'Drake', 'Zelensky', 'Hugh Jackman', 'Kenguru'
    ], 
    'q4': [
        'Capital', 'almost capital', 'biggest in EU', 'biden administration'
    ], 
    'q5': [
        '21', '27', '18', '30'
    ], 
}

def Kyiv():
    B = 0  
    streak = 0
    z = 'Kyiv'  
    print(f'Whoa, you chose {z}, let\'s try!')


    print(f'In which country is {z} located?')
    print('Variants:', ', '.join(v1['q1']))
    q1 = input("Enter your answer: ").strip()


    if q1.lower() == "dnr":
        B += 1000000
        print("Whoa! You found the way!")
        print('All treasure is yours:', B)
        return 

    if z in cities and q1.lower() == cities[z]['Country'].lower():
        B += 1
        streak += 1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Country'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'How many people live in {z} (around to million)?')
    print("Variants:", ', '.join(v1['q2']))
    q2 = input("Enter your answer: ").strip()

    if q2.replace(",", "").strip() == cities[z]['Population'].replace(",", ""):
        B += 1
        streak += 1
        if streak == 2:
            B +=1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Population'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'Who is a famous person from {z}?')
    print("Variants:", ', '.join(v1['q3']))
    q3 = input("Enter your answer: ").strip()

    if q3.lower() == cities[z]['Famous person in'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Famous person in'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the status of {z}?')
    print("Variants:", ', '.join(v1['q4']))
    q4 = input("Enter your answer: ").strip()

    if q4.lower() == cities[z]['Status'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Status'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the average temperature in {z}?')
    print("Variants:", ', '.join(v1['q5']))
    q5 = input("Enter your answer: ").strip()

    if q5 == cities[z]['Average temp']:
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4   
        elif streak == 5:
            B += 7    
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Average temp'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f"Thank you for playing! Your final score is: {B}! Your final streak is: {streak}!")

def London():
    z = 'London'
    B = 0  
    streak = 0 
    print(f'Whoa, you chose {z}, let\'s try!')


    print(f'In which country is {z} located?')
    print('Variants:', ', '.join(v2['q1']))
    q1 = input("Enter your answer: ").strip()


    if q1.lower() == "dnr":
        B += 1000000
        print("Whoa! You found the way!")
        print('All treasure is yours:', B)
        return 

    if z in cities and q1.lower() == cities[z]['Country'].lower():
        B += 1
        streak += 1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Country'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'How many people live in {z} (around to million)?')
    print("Variants:", ', '.join(v2['q2']))
    q2 = input("Enter your answer: ").strip()

    if q2.replace(",", "").strip() == cities[z]['Population'].replace(",", ""):
        B += 1
        streak += 1
        if streak == 2:
            B +=1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Population'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'Who is a famous person from {z}?')
    print("Variants:", ', '.join(v2['q3']))
    q3 = input("Enter your answer: ").strip()

    if q3.lower() == cities[z]['Famous person in'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Famous person in'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the status of {z}?')
    print("Variants:", ', '.join(v2['q4']))
    q4 = input("Enter your answer: ").strip()

    if q4.lower() == cities[z]['Status'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Status'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the average temperature in {z}?')
    print("Variants:", ', '.join(v2['q5']))
    q5 = input("Enter your answer: ").strip()

    if q5 == cities[z]['Average temp']:
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4   
        elif streak == 5:
            B += 7    
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Average temp'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f"Thank you for playing! Your final score is: {B}! Your final streak is: {streak}!")

def LA():
    z = 'LA'
    B = 0  
    streak = 0 
    print(f'Whoa, you chose {z}, let\'s try!')


    print(f'In which country is {z} located?')
    print('Variants:', ', '.join(v3['q1']))
    q1 = input("Enter your answer: ").strip()


    if q1.lower() == "dnr":
        B += 1000000
        print("Whoa! You found the way!")
        print('All treasure is yours:', B)
        return 

    if z in cities and q1.lower() == cities[z]['Country'].lower():
        B += 1
        streak += 1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Country'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'How many people live in {z} (around to million)?')
    print("Variants:", ', '.join(v3['q2']))
    q2 = input("Enter your answer: ").strip()

    if q2.replace(",", "").strip() == cities[z]['Population'].replace(",", ""):
        B += 1
        streak += 1
        if streak == 2:
            B +=1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Population'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'Who is a famous person from {z}?')
    print("Variants:", ', '.join(v3['q3']))
    q3 = input("Enter your answer: ").strip()

    if q3.lower() == cities[z]['Famous person in'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Famous person in'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the status of {z}?')
    print("Variants:", ', '.join(v3['q4']))
    q4 = input("Enter your answer: ").strip()

    if q4.lower() == cities[z]['Status'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Status'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the average temperature in {z}?')
    print("Variants:", ', '.join(v3['q5']))
    q5 = input("Enter your answer: ").strip()

    if q5 == cities[z]['Average temp']:
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4   
        elif streak == 5:
            B += 7    
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Average temp'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f"Thank you for playing! Your final score is: {B}! Your final streak is: {streak}!")

def Tokyo():
    z = 'Tokyo'
    B = 0  
    streak = 0
    print(f'Whoa, you chose {z}, let\'s try!')


    print(f'In which country is {z} located?')
    print('Variants:', ', '.join(v4['q1']))
    q1 = input("Enter your answer: ").strip()


    if q1.lower() == "dnr":
        B += 1000000
        print("Whoa! You found the way!")
        print('All treasure is yours:', B)
        return 

    if z in cities and q1.lower() == cities[z]['Country'].lower():
        B += 1
        streak += 1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Country'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'How many people live in {z} (around to million)?')
    print("Variants:", ', '.join(v4['q2']))
    q2 = input("Enter your answer: ").strip()

    if q2.replace(",", "").strip() == cities[z]['Population'].replace(",", ""):
        B += 1
        streak += 1
        if streak == 2:
            B +=1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Population'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'Who is a famous person from {z}?')
    print("Variants:", ', '.join(v4['q3']))
    q3 = input("Enter your answer: ").strip()

    if q3.lower() == cities[z]['Famous person in'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Famous person in'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the status of {z}?')
    print("Variants:", ', '.join(v4['q4']))
    q4 = input("Enter your answer: ").strip()

    if q4.lower() == cities[z]['Status'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Status'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the average temperature in {z}?')
    print("Variants:", ', '.join(v4['q5']))
    q5 = input("Enter your answer: ").strip()

    if q5 == cities[z]['Average temp']:
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4   
        elif streak == 5:
            B += 7    
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Average temp'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f"Thank you for playing! Your final score is: {B}! Your final streak is: {streak}!")

def Sydney():
    z = 'Sydney'
    B = 0  
    streak = 0
    print(f'Whoa, you chose {z}, let\'s try!')


    print(f'In which country is {z} located?')
    print('Variants:', ', '.join(v5['q1']))
    q1 = input("Enter your answer: ").strip()


    if q1.lower() == "dnr":
        B += 1000000
        print("Whoa! You found the way!")
        print('All treasure is yours:', B)
        return 

    if z in cities and q1.lower() == cities[z]['Country'].lower():
        B += 1
        streak += 1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Country'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'How many people live in {z} (around to million)?')
    print("Variants:", ', '.join(v5['q2']))
    q2 = input("Enter your answer: ").strip()

    if q2.replace(",", "").strip() == cities[z]['Population'].replace(",", ""):
        B += 1
        streak += 1
        if streak == 2:
            B +=1
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Population'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'Who is a famous person from {z}?')
    print("Variants:", ', '.join(v5['q3']))
    q3 = input("Enter your answer: ").strip()

    if q3.lower() == cities[z]['Famous person in'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Famous person in'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the status of {z}?')
    print("Variants:", ', '.join(v5['q4']))
    q4 = input("Enter your answer: ").strip()

    if q4.lower() == cities[z]['Status'].lower():
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Status'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f'What is the average temperature in {z}?')
    print("Variants:", ', '.join(v5['q5']))
    q5 = input("Enter your answer: ").strip()

    if q5 == cities[z]['Average temp']:
        B += 1
        streak += 1
        if streak == 2:
            B += 1
        elif streak == 3:
            B += 2
        elif streak == 4:
            B += 4   
        elif streak == 5:
            B += 7    
        print("Correct!")
        print(f'Balance is {B}')
        print(f'Streak is {streak}')
    else:
        streak = 0
        print("Incorrect! The correct answer is:", cities[z]['Average temp'])
        print(f'Balance is {B}')
        print(f'Streak is {streak}')

    print(f"Thank you for playing! Your final score is: {B}! Your final streak is: {streak}!")


def play_game():
    while True:
        print('Hey there! Below you have the list of some cities and you need to guess fun facts! Reward incleded \n when ready press 1 \n check rules press 2')
        x = int(input())
        if x == 1:
            print('here is the list, please choose one:')
            i = 1
            for city, info in cities.items():
                print(city, i)
                i += 1
            print("chose the city with the number form right")
            y = int(input())
            if y == 1:
                Kyiv()
            elif y == 2:
                London()
            elif y == 3:
                LA()
            elif y ==4:
                Tokyo()
            elif y == 5:
                Sydney()
        elif x == 2 : 
            print('In this poll you need to give correct answers.\n 1 correct answer - 1$, stricks are increase your score / balance \n if you want get you money you need make a transaction in app')
            print('Now reload app for start')
        else:
            print('press 1 or stop it)')

        play_again = input("Do you want to play again? (1/2): ").lower()
        if play_again != '1':
            print("Thank you for playing! Goodbye!")
            break
if __name__ == "__main__":
    play_game()