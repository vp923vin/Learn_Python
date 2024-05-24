# SETS
-  Sets are used to store multiple items in a single variable.
- A set is a collection which is unordered, unchangeable*, and unindexed.

Note: Set items are unchangeable, but you can remove items and add new items.
Note: Sets are unordered, so you cannot be sure in which order the items will appear.

 - Set items are unordered, unchangeable, and do not allow duplicate values.
 - Unordered means that the items in a set do not have a defined order.
 - Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
 - Set items are unchangeable, meaning that we cannot change the items after the set has been created.
 - Sets cannot have two items with the same value.
 
  # Duplicate values will be ignored
  Note: The values True and 1 are considered the same value in sets, and are treated as duplicates.
        The values False and 0 are considered the same value in sets, and are treated as duplicates.

# Set Items - Data Types
  - Set items can be of any data type
  - A set can contain different data types
  - type()
    From Python's perspective, sets are defined as objects with the data type 'set'
    <class 'set'>

  -  It is also possible to use the set() constructor to make a set.
  eg.   thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
        print(thisset)

    

# Python Collections (Arrays)
There are four collection data types in the Python programming language:

 - List is a collection which is ordered and changeable. Allows duplicate members.
 - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 - Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 - Dictionary is a collection which is ordered** and changeable. No duplicate members.


# SET Access 
  - You cannot access items in a set by referring to an index or a key.
  - But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
    by using  the in keyword.
  - Once a set is created, you cannot change its items, but you can add new items.

# SET Add
  - To add one item to a set use the add() method.
  - eg.
        thisset = {"apple", "banana", "cherry"}
        thisset.add("orange")
        print(thisset)
        # output
        {'apple', 'orange', 'banana', 'cherry'}

  - To add items from another set into the current set, use the update() method.
  - eg.
        thisset = {"apple", "banana", "cherry"}
        tropical = {"pineapple", "mango", "papaya"}
        thisset.update(tropical)
        print(thisset)
        # output
        {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

  - The object in the update() method does not have to be a set, it can be any iterable object 
    (tuples, lists, dictionaries etc.).
  - eg. 
        thisset = {"apple", "banana", "cherry"}
        mylist = ["kiwi", "orange"]
        thisset.update(mylist)
        print(thisset)
        # output
        {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

# SET Remove
  - To remove an item in a set, use the remove(), or the discard() method.
  - eg.
        thisset = {"apple", "banana", "cherry"}
        thisset.remove("banana")
        print(thisset)
        # output
        {'apple', 'cherry'}

    Note: If the item to remove does not exist, remove() will raise an error.
    - Remove "banana" by using the discard() method.
    - eg. 
        thisset = {"apple", "banana", "cherry"}
        thisset.discard("banana")
        print(thisset)
        # output
        {'cherry', 'apple'}

    Note: If the item to remove does not exist, discard() will NOT raise an error.
    - You can also use the pop() method to remove an item, but this method will remove 
      a random item, so you cannot be sure what item that gets removed.

    - The return value of the pop() method is the removed item.
    - eg.
        thisset = {"apple", "banana", "cherry"}
        x = thisset.pop()
        print(x)
        print(thisset)
        # output
        cherry
        {'apple', 'banana'}

    Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

    - The clear() method empties the set:
    - eg. 
        thisset = {"apple", "banana", "cherry"}
        thisset.clear()
        print(thisset)
        # output
        set()

    - The del keyword will delete the set completely
    - eg.    
        thisset = {"apple", "banana", "cherry"}
        del thisset
        print(thisset)
        # output
        NameError: name 'thisset' is not defined

    - Loop through the set, and print the values:

        thisset = {"apple", "banana", "cherry"}

        for x in thisset:
            print(x)


# SET join
   - There are several ways to join two or more sets in Python.
   - The union() and update() methods joins all items from both sets.
   - The intersection() method keeps ONLY the duplicates.
   - The difference() method keeps the items from the first set that are not in the other set(s).
   - The symmetric_difference() method keeps all items EXCEPT the duplicates. 


- The union() method returns a new set with all items from both sets.
- eg.
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = set1.union(set2)
    print(set3)
    # output
    {'b', 1, 3, 'a', 2, 'c'}

- You can use the | operator instead of the union() method, and you will get the same result.
- eg. 
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = set1 | set2
    print(set3)

- All the joining methods and operators can be used to join multiple sets.
- When using a method, just add more sets in the parentheses, separated by commas.
- eg. 
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = {"John", "Elena"}
    set4 = {"apple", "bananas", "cherry"}

    myset = set1.union(set2, set3, set4)
    print(myset)

- When using the | operator, separate the sets with more | operators.

# Join a Set and a Tuple
- The union() method allows you to join a set with other data types, like lists or tuples.
  The result will be a set.
  eg.  
    x = {"a", "b", "c"}
    y = (1, 2, 3)
    z = x.union(y)
    print(z)
    # output
    {'c', 'b', 3, 2, 'a', 1}

Note: The  | operator only allows you to join sets with sets, and not with other data types 
like you can with the  union() method.

# Update
 - The update() method inserts all items from one set into another.
 - The update() changes the original set, and does not return a new set.
 - eg. 
    set1 = {"a", "b" , "c"}
    set2 = {1, 2, 3}
    set1.update(set2)
    print(set1)
    # output 
    {1, 2, 3, 'b', 'a', 'c'}

Note: Both union() and update() will exclude any duplicate items.

# Intersection 
  - Keep ONLY the duplicates
  - The intersection() method will return a new set, that only contains the items that are present in both sets.
  - eg. 
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}

        set3 = set1.intersection(set2)
        print(set3)
  - can use the & operator instead of the intersection() method, and you will get the same result.
  - eg.
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1 & set2
    print(set3)
    # output
    {'apple'}

    Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

    - The intersection_update() method will also keep ONLY the duplicates, but it will change the 
      original set instead of returning a new set.
    - eg.
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        set1.intersection_update(set2)
        print(set1)

    - The values True and 1 are considered the same value. The same goes for False and 0
    - The difference() method will return a new set that will contain only the items from the first set that 
      are not present in the other set.
    - it can be use the - operator instead of the difference() method, and you will get the same result.
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        set3 = set1 - set2
        print(set3) 
        
    Note: The - operator only allows you to join sets with sets, and not with other data types like you 
        can with the difference() method

    - The difference_update() method will also keep the items from the first set that are not in the 
      other set, but it will change the original set instead of returning a new set.
    - eg. 
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        set1.difference_update(set2)
        print(set1)
    
    - The symmetric_difference() method will keep only the elements that are NOT present in both sets.
    - You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
    Note: The ^ operator only allows you to join sets with sets, and not with other data types like you 
         can with the symmetric_difference() method.

        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        set3 = set1.symmetric_difference(set2)
        print(set3)

    The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
    eg. 
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        set1.symmetric_difference_update(set2)
        print(set1)
        # output 
        {'google', 'banana', 'microsoft', 'cherry'}