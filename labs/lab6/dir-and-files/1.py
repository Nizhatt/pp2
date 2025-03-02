# Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path=r'C:\pathforpp2'
content = os.scandir(path)
dirs=[]
files=[]
fd=[]
for entry in content:
    if entry.is_file():
        files.append(entry.name)
    if entry.is_dir():
        dirs.append(entry.name)
    fd.append(entry.name)
print("Folders: ", dirs)
print("-------------------")
print("Files: ", files)
print("-------------------")
print("Files and Folders: ", fd)