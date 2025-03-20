name=r"labs/lab6/dir-and-files/row.txt"
file=open(name)
cnt=0
for line in file:
    cnt+=1
print(cnt)