def parallelogram():
    side = int(input("Length of base: "))
    Length = int(input("Height of parallelogram: "))
    area = Length* side
    return area

print("Expected Output: ", round(parallelogram(), 6))