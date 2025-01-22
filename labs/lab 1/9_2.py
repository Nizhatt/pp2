# Slicing Strings

b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello, World!"
print(b[:5]) #characters from the start to position 5 

#Slice To the End
b = "Hello, World!"
print(b[2:]) #characters from position 2, and all the way to the end

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2]) #From: "o" in "World!" (position -5) to, but not included: "d" in "World!" (position -2)