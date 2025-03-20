import os

path = r'C:\Users\LENOVO\Desktop\pp2\labs\lab6\dir-and-files\1.py'


print("Existence:",os.access(path, os.F_OK)) # Existence
print("Readability:",os.access(path, os.R_OK)) # Readability
print("Writability:",os.access(path, os.W_OK)) # Writeability
print("Executability:",os.access(path, os.X_OK)) # Executeability