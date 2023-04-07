#Write a program that creates two lists of integers and then finds the common elements between those two lists.
#Print the common elements.
a=[1,3,5,6,8,9,35]
b=[2,4,1,7,9,34,56]
print(a)
print(b)
c=list(set(a).intersection(b))
print(c)