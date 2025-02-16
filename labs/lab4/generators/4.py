def squares(a, b):
    for number in range(a, b + 1):
        yield number * number

a = 1
b = 5
for square in squares(a, b):
    print(square)
