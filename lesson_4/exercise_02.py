#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
try: 
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    if hours > 40:
        print('Pay:', 40 * rate + (hours % 40 * (rate * 1.5)))
        rate = rate * 1.5
    else :
        print('Pay:', hours * rate)
except: 
    print('Error, please enter numeric input')