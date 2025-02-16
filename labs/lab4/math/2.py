def trapezoid():
    h = int(input("Height: "))
    a = int(input("Base, first value: "))
    b = int(input("Base, second value: "))
    S = ((a + b) / 2) * h
    return S

print("Expected Output: ", round(trapezoid(), 6))