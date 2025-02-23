import re
text = input()

pattern = 'a.+b'
result = re.findall(pattern, text)
print(result)