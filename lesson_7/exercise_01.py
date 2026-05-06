#Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
index = 1
word = 'banana'
wordLength = len(word)
while index <= len(word):
    print(word[wordLength - index])
    index = index + 1