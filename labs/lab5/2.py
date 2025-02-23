import re
text = input()

pattern = 'ab{2,3}'
result = re.findall(pattern, text)
print(result)