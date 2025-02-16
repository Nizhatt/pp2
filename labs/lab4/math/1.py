import math

def maths():
    degree = int(input("Input degree: "))
    radian = degree * (math.pi / 180)
    return radian

print("Output radian:" ,  round(maths(), 6))

    
    