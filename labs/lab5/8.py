import re
text = "HeLLoWorldThisIsPython"
pattern = r'[A-Z]+'
result = re.split(pattern, text)
print(result)