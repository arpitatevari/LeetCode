#Write a program that creates a list of integers and then asks the user to input an integer to check if
#it exists in the list. Print a message indicating whether the integer is in the list or not.
a=[1,3,4,5,6,7,8,90]
print(a)
n=int(input("Enter Number:"))
if n in  a:
    print("Exist")
else:
    print("Not exists")    