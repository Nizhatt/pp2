import re
camel=input()
pat=r'([a-z])([A-Z])'
ch=re.sub(pat, r'\1_\2', camel )
ch.upper()
print(ch.lower())