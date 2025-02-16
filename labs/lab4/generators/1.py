def generate_squares():
    N = int(input("Enter a number: "))
    for i in range(N + 1):
        yield i * i

print(list(generate_squares()))

