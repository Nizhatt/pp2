def rev():
    sen=input("enter a sentence ")
    arr=sen.split()
    arr.reverse()
    s=""
    for i in arr:
        s+=i
        s+=' '
    s.strip()
    return s


print(rev())