#Loop Dictionaries

thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#keys() method
for x in thisdict.keys():
  print(x)

#items() method:
for x, y in thisdict.items():
  print(x, y)

#values() method
for x in thisdict.values():
  print(x)