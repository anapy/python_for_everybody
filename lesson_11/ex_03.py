'''Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''
file = open('text.txt')

letterCount = dict()
for line in file:
    #split line in words
    line = line.rstrip()
    #convert words to lower case
    words = line.split(' ')
    for word in words:
        word = word.lower()
        #split words in letters
        wordLetters = list(word)
        #don't count other than lower letters
        for letter in wordLetters:
            if 'a' <= letter <= 'z':
                letterCount[letter] = letterCount.get(letter, 0) + 1
    
lettersTuple = list()
for key, val in letterCount.items():
    lettersTuple.append((val, key))
    lettersTuple.sort(reverse=True)

for key, val in lettersTuple:
    print(key, val)