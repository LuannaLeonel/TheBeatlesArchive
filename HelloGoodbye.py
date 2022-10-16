import random

while True:
    num = random.randint(1,2)
    youSay = input("You say, ").lower()
    if youSay == 'yes':
        print('I say, "No"')

        if num == 1:
            print('(I say, "Yes", but I may mean, "No")')

    elif youSay == 'stop':
        print('and I say, "Go, go, go"')

        if num == 2:
            print('(I can stay still it\'s time to go)')

    elif youSay == 'goodbye':

        print('I say, "Hello"')
        print('')
        if num == 1:
            print('Why, why, why, why, why, why, do you\nSay,"Goodbye, goodbye, bye, bye"?\nOh no')
        else:
            print('I don\'t know why you say, "Goodbye", I say, "Hello, hello, hello"\nI don\'t know why you say, "Goodbye", I say, "Hello"')

    elif youSay == 'low':
        print('I say, "High"')

    elif youSay == 'why?':
        print('And I say, "I don\'t know"')
        print("Oh no")

    elif youSay == 'quit':
        break

    else:
        pass
    
    print('')



