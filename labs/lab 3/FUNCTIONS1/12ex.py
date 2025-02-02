def histogram():
    n=int(input("length of list "))
    arr=[]
    for i in range(n):
        q=int(input('enter a num '))
        arr.append(q)
    s=""
    for i in arr:
        s=""
        for j in range(i):
            s+="*"  
        print(s)





histogram()