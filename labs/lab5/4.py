import re
text = input()

pattern = '[A-Z][a-z]+'
result = re.findall(pattern, text)
print(result)