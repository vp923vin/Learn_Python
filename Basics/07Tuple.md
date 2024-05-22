# Tuples

 - Tuples are used to store multiple items in a single variable.
 - A tuple is a collection which is ordered and unchangeable.
    eg. thistuple = ("apple", "banana", "cherry")
        print(thistuple)

 - Tuple items are ordered, unchangeable, and allow duplicate values.
  # Ordered
    - When we say that tuples are ordered, it means that the items have a defined order, 
      and that order will not change.
  # Unchangeable
    - Tuples are unchangeable, meaning that we cannot change, add or remove items after the 
      tuple has been created.
  # Allow Duplicates
    - Since tuples are indexed, they can have items with the same value

  # Create Tuple With One Item
    - To create a tuple with only one item, you have to add a comma after the item, 
      otherwise Python will not recognize it as a tuple.
     
      thistuple = ("apple",)
      print(type(thistuple))
      # output
      <class 'tuple'>

      #NOT a tuple
      thistuple = ("apple")
      print(type(thistuple))
      # output 
      <class 'str'>

 - Tuple items can be of any data type.
 - Using the tuple() method to make a tuple
    thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
    print(thistuple)

  # Tuple Access
  - You can access tuple items by referring to the index number, inside square brackets.
  - Negative indexing means start from the end.
  - tuple access example
   eg. Return the third, fourth, and fifth item:
    thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(thistuple[2:5])

  - accessbility same as the string or list
  
  # Tuple update
  - Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
    or immutable as it also is called.
  - But there is a workaround. You can convert the tuple into a list, change the list, 
    and convert the list back into a tuple.
  - example:
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)
    print(x)
  - Since tuples are immutable, they do not have a built-in append() method, but there are 
    other ways to add items to a tuple:
    1 - Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, 
        add your item(s), and convert it back into a tuple.

        thistuple = ("apple", "banana", "cherry")
        y = list(thistuple)
        y.append("orange")
        thistuple = tuple(y)

    2 - Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, 
        (or many), create a new tuple with the item(s), and add it to the existing tuple:

        thistuple = ("apple", "banana", "cherry")
        y = ("orange",)
        thistuple += y
        print(thistuple)

    Note: You cannot remove items in a tuple.

    - Tuples are unchangeable, so you cannot remove items from it, but you can use the same 
      workaround as we used for changing and adding tuple items

        thistuple = ("apple", "banana", "cherry")
        y = list(thistuple)
        y.remove("apple")
        thistuple = tuple(y)

    - Or you can delete the tuple completely.
        thistuple = ("apple", "banana", "cherry")
        del thistuple
        print(thistuple) #this will raise an error because the tuple no longer exists

        