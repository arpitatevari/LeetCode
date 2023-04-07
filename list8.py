#Write a program that creates a list of integers and then removes all duplicates from the list.
#Print the final list.
a = [1,1,2,1,3,4,1,2,3,4,7,9,7]
print(a)
dictionary = dict.fromkeys(a)
b = list(dictionary)
print(b)