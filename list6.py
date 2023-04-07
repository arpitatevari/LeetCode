#!!!!!Write a program that creates a list of strings and then removes all elements that contain a specific substring. 
#Print the final list.
a=["Arpita", "Mannat","Sudipto","Shank","Ekta"]
print(a)
k="Ekta"
while(k in a):
    a.remove(k)
print(a)