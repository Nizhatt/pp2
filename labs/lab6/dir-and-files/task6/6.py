path = r"labs/lab6/dir-and-files/task6/"


for i in range(1,27):
    f = f'{path}{chr(i+64)}.txt'
    open(f, 'w')

print('Files created successfully !')