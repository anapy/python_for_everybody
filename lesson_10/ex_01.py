'''Exercise 1: Download a copy of the file
www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.'''

text = open('words.txt')

wordsDict = dict()
for line in text:
    line = line.rstrip()
    words = line.split()
    for word in words:
        wordsDict[word] = wordsDict.get(word, 0) + 1

searchWord = input('Enter a word: ')
print('The word', searchWord, 'is in the text', searchWord in wordsDict)