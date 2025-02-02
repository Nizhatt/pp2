def uni():
    n=int(input("length of list "))
    arr=[]  
    
    for i in range(n):
        q=int(input('enter a num '))
        arr.append(q)
    qwe=[]
    cnt=0

    for i in arr:
        cnt=-1
        for j in arr:
            if i==j:
                cnt+=1
        if cnt==0:
            qwe.append(i)
    return qwe
        


print(uni())