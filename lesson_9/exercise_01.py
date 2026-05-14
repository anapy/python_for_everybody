#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

#function that modifies the list
def chop(array):
    del array[0:(len(array) - 1)]
    return None

fruits = list(['banana', 'pear', 'orange'])
chop(fruits)
print(fruits)

colors = list(['blue','purple','red', 'yellow'])
#function that keeps the list and return a new list
def middle(array):
    return array[1:len(array) - 1]

print(middle(colors))
print(colors)