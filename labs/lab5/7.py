import re

snake= "this_is_camel_case"
p=r'_'
q=re.split(p, snake)
a=[]
for i in q:
    b=i.capitalize()
    
    a.append(b)
ans=""
for i in a:
    ans+=i
print(ans)