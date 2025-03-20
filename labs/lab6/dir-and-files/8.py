import time
import os

path = r"C:\Users\LENOVO\Desktop\pp2\labs\lab6\dir-and-files\8.txt"


if os.access(path, os.F_OK): # Check if file exists
    if os.access(path, os.W_OK): # Check access to delete
        os.remove(path)
        print("[File was deleted]")
    else:
        print("[You don't have access to delete this file]")
        
else:
    print("[File was not found]")
    