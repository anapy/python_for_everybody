'''Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756'''

import re

file = open('mbox-short.txt')

count = 0
total = 0
regularExp = '^New .*: ([0-9]*)'
for line in file: 
    lst = re.findall(regularExp, line)
    if len(lst) > 0:
        total += int(lst[0])
        count += 1

print(int(total/count))



