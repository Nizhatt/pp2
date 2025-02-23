import re
text=input()
pattern='[\s,\.]+'
result=re.sub(pattern,':', text)
print(result)