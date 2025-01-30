def myG(x):
    if x in ['Tate', 'Trump', 'Durov']:
        print(f'Your {x} G is the best')
    elif x == 'Biden':
        print(f'Bro wait 5 seconds and think 1 more')
        i = 0
        while i < 10:
            i += 1
            print(i)
        x = input('Who is your G now? ')
        myG(x)
    else:
        print(f'Your {x} G is great')

x = input('Who is your G? ')
myG(x)