n=int(input())
arr=[]
for i in range(n):
    a=input()
    arr.append(a)
tup=tuple(a)
if(any(tup)):
    print("OK")
else:
    print("NO")