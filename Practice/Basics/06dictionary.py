thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway") # dict() constructor
print(thisdict)

# Dictionary access
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print("value access: ", x)
x = thisdict.get("model")
print("get method to access value: ", x)
x = thisdict.keys()
print("all dict keys: ", x)
x = thisdict.values()
print("all values dict: ", x)
x = thisdict.items()
print("all items one by one: ", x)


# Dictionary Change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# Dictionary Add

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
} 
thisdict["color"] = "red"
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

# Dictionary Remove 

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# thisdict.pop("model")
# print(thisdict)

# thisdict.popitem()
# print(thisdict)

# del thisdict["model"]
# print(thisdict)

# thisdict.clear()
# print(thisdict)

# del thisdict
# print(thisdict)

# DICTIONARY Loop

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)


for x, y in thisdict.items():
  print(x, y)


# Dictionary copy

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)