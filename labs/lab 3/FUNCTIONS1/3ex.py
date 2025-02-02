def solve(numheads, numlegs):
    x = (4 * numheads - numlegs) // 2
    y = numheads - x
    return f"Кур: {x}, Кроликов: {y}"


numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result)  
