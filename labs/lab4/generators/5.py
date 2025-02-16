def num():
    n = int(input("Enter a number: "))
    while n >= 0:
        yield n
        n -= 1

print(list(num()))