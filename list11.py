#Write a program that creates a list of integers and then asks the user to input a position to remove an element from the list.
#Print the final list.
a=[1,3,4,5,6,7,8,90]
print(a)
b=int(input("Enter index value"))
del a[b]
print(a)