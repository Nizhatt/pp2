#Join Sets

#union() and update()
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Intersection() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2 
print("2. ", set3)

set1.intersection_update(set2)
print("   ", set1)