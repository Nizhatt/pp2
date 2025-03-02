# Write a Python program with builtin function to multiply all the numbers in a list

from functools import reduce
n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
a=reduce(lambda x,y: x*y, arr)
print(a)