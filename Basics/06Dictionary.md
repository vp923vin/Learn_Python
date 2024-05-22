# Dictionary
 - Dictionaries are used to store data values in key:value pairs.
 - A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
 - Dictionaries are written with curly brackets, and have keys and values.
 - eg.
     thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)

- Dictionary items are ordered, changeable, and do not allow duplicates.
- Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# orderd or unordered
- When we say that dictionaries are ordered, it means that the items have a defined order, 
  and that order will not change.
  Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
# changeable
- Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary 
  has been created.
# duplicate
- Dictionaries cannot have two items with the same key.

- can find len() length, and type() datatype.

- It is also possible to use the dict() constructor to make a dictionary.
eg. thisdict = dict(name = "John", age = 36, country = "Norway")

Note: as of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionary access
 - You can access the items of a dictionary by referring to its key name, inside square brackets.
 - There is also a method called get() that will give you the same result.
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = thisdict["model"]
    or
    x = thisdict.get("model")

- The keys() method will return a list of all the keys in the dictionary.
  x = thisdict.keys()

- The values() method will return a list of all the values in the dictionary.
  x = thisdict.values()

- The list of the keys and values is a view of the dictionary, meaning that any changes done to the 
  dictionary will be reflected in the keys list and values list and in the dictionary.

- The items() method will return each item in a dictionary.
  x = thisdict.items()


# Dictionary Change

- The update() method will update the dictionary with the items from the given argument.
- The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# Dictionary Add
- Adding an item to the dictionary is done by using a new index key and assigning a value to it.
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    } 
    thisdict["color"] = "red"
    print(thisdict)

- The update() method will update the dictionary with the items from a given argument. 
  If the item does not exist, the item will be added.

- The argument must be a dictionary, or an iterable object with key:value pairs.
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  thisdict.update({"color": "red"})

# Dictionary Remove 
 -  The pop() method removes the item with the specified key name.
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.pop("model")
    print(thisdict)

- The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
    thisdict.popitem()
    print(thisdict)

- The del keyword removes the item with the specified key name.
    del thisdict["model"]
    print(thisdict)

- The del keyword can also delete the dictionary completely.
- The clear() method empties the dictionary
  thisdict.clear()
  print(thisdict)


# DICTIONARY Loop

 - loop through a dictionary by using a for loop.
    Print all key names in the dictionary, one by one
    for x in thisdict:
        print(x)

 - Print all values in the dictionary, one by one
    for x in thisdict:
        print(thisdict[x])

- loop values 
for x in thisdict.values():
  print(x)

- loop items key and value both
for x, y in thisdict.items():
  print(x, y)

- keys loop

for x in thisdict.keys():
  print(x)

# Dictionary copy

- You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only 
  be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

- There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

or 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


- A dictionary can contain dictionaries, this is called nested dictionaries.

- To access items from a nested dictionary, you use the name of the dictionaries,
  starting with the outer dictionary

  print(myfamily[key1][key12])

