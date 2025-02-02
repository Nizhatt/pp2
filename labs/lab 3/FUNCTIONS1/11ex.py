def palin():
    s=input("enter a string ")
    n=s
    b=s[::-1]
    if b==n:
        return "True"
    else:
        return "False"

print(palin())