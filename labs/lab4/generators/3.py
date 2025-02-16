def even_numbers():
    N = int(input("Enter a number: "))
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i 

print(list(even_numbers()))