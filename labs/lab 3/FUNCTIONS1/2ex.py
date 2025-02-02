def temp():
    F = int(input("enter temp in  farenheit: "))
    C = (5 / 9) * (F - 32)
    return C

print("output temp in celsius: ", temp())