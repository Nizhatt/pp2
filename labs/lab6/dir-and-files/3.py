import os

def path_info(path):
    print("------------------------------------------------------------------------------")
    if os.access(path, os.F_OK):
        
        if os.path.isfile(path):
            print("File name:", os.path.basename(path))
        else: 
            print("This is not a file (probably a directory)")

        print("Directory:", os.path.dirname(path))

    else:
        print("Path does not exist")



path = r"C:\Users\LENOVO\Desktop\pp2\labs\lab6\dir-and-files\1.py" #File
path_info(path)

path = r"C:\Users\LENOVO\Desktop\pp2\labs\lab6\dir-and-files" #Directory
path_info(path)

path = r"C:\Users\LENOVO\Desktop\pp2\labs\lab6\something" #Does not exist    
path_info(path)
print("------------------------------------------------------------------------------")