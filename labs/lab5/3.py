import re
text = input()

pattern = '[a-z]+_[a-z]+'
result = re.findall(pattern, text)
print(result)