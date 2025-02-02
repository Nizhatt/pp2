def spy_game():
    n=int(input("length of list "))
    arr=[]
    for i in range(n):
        q=int(input('enter a num '))
        arr.append(q)
    s=""
    for i in arr:
        s+=str(i)
    if s.find("007")!=-1:
        return "True"
    else:
        return "False"

print(spy_game())