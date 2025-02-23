import re
a='InsertSpacesBetweenWordsStartingWithCapitalLetters'
pat=r'([A-Z])'
ch=re.sub(pat, r' \1', a )
print(ch.strip())