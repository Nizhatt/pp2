#If ... Else

a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")