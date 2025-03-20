task5 = open(r'labs/lab6/dir-and-files/5.py', 'r')
content = task5.read()

task7 = open(r'labs/lab6/dir-and-files/7.txt', 'w')
task7.write(content)

print("Exelent! Task5.py is copied to Task7.txt")