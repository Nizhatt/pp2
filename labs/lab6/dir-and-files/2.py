import os

path = r'C:\Windows\System32'
existence = os.path.exists(path)

if existence:
    ch=os.access(path, os.F_OK)
    print(f'Existence: {ch}')
    cho=os.access(path, os.R_OK)
    print(f'Readability: {cho}')
    chot=os.access(path, os.W_OK)
    print(f'Writeability: {chot}')
    choto=os.access(path, os.X_OK)
    print(f'Executeability: {ch}')
else:
    print("path doesnt exist")