# Global Variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#  Another example of global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)