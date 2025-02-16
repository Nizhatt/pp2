def regular_polygon():
    side = int(input("Input number of sides: "))
    leng = int(input("Input the length of a side: "))
    area = leng * leng
    return area

print("The area of the polygon is: ", regular_polygon())