def even_numbers():
    N = int(input("Enter a number: "))
    for i in range(N + 1):
        if i % 2 == 0:
            yield i 

print(list(even_numbers()))