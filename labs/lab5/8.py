import re
text = input()
pattern = r'[A-Z]+'
result = re.split(pattern, text)