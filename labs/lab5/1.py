import  re 

text =input()

pattern = 'ab*'
result = re.findall(pattern, text)
print(result)