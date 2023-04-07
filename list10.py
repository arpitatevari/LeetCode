#Write a program that creates a list of integers and then finds the sum of all the even numbers in the list. 
#Print the sum.
a=[1,3,4,5,6,7,8,90]
print(a)
result = 0
for item in a:
    if not item%2:
        result += item
print(result)