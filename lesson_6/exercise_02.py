# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 
smallest = None
biggest = None
while True:
    userInput = input('Enter a number: ')
    if userInput != 'done':
        try:
            number = int(userInput)
            if biggest is None or biggest < number:
                biggest = number
            if smallest is None or smallest > number:
                smallest = number
        except: 
            print('Invalid input')
    else:
        print('Maximum is', biggest)
        print('Minimum is', smallest)
        break