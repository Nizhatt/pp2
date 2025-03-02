s=input()
s.split()
cnt=0

a=len(list(filter(lambda x: ord('Z')>=ord(x)>=ord('A'), s)))
print(a)