#Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than an integer, detect their mistake using try and except and print an error message and skip to the next integers.
count = 0
total = 0
average = 0
while True:
    userInput = input('Enter a number: ')
    if userInput != 'done':
        try:
            number = int(userInput)
            count = count + 1
            total = total + number
        except: 
            print('Invalid input')
    else:
        print(total, count, total/count)
        break