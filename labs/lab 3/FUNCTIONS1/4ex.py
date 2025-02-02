def filter_prime():
    n=int(input("length of list "))
    arr=[]
    for i in range(n):
        q=int(input('enter a num'))
        arr.append(q)
        cnt=0
    prime=[]
    for ch in arr:
        cnt=0
        for j in range(1, ch+1):
            if ch%j==0:
                cnt+=1
        if cnt==2:
            prime.append(ch)
    return prime



print(filter_prime())