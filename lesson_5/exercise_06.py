#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate): 
   if hours > 40:
      return 40 * rate + (hours % 40 * (rate * 1.5))
   else :
      return hours * rate

try: 
   hours = float(input('Enter Hours: '))
   rate = float(input('Enter Rate: '))
   print('Pay',computepay(hours, rate))
except: 
   print('Error, please enter numeric input')