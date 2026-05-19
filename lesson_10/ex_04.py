'''Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195'''

fileName = input('Enter a file name: ')
text = open(fileName)

emailAddresses = dict()
for line in text:
    line = line.rstrip()
    words = line.split(' ')
    if words[0] != 'From' or len(words) < 3: continue
    emailAddresses[words[1]] = emailAddresses.get(words[1], 0) + 1
    
largest = None
bigEmail = None
for email, freq in emailAddresses.items():
    if largest is None or largest < freq:
        largest = freq
        bigEmail = email
print(bigEmail, largest)