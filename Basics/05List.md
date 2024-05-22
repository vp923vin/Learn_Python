# List

- Lists are used to store multiple items in a single variable.
- Lists are created using square brackets.
  eg. thislist = ["apple", "banana", "cherry"]
      print(thislist)

- List items are ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] etc.
- When we say that lists are ordered, it means that the items have a defined order, 
  and that order will not change.
- If you add new items to a list, the new items will be placed at the end of the list.

Note: 
    - There are some list methods that will change the order, but in general: 
      the order of the items will not change.


- The list is changeable, meaning that we can change, add, and remove items in a list 
  after it has been created.

- A list can contain different data types
  eg. list1 = ["abc", 34, True, 40, "male"]
      print(list1)
      # output
      <class 'list'>

- It is also possible to use the list() constructor when creating a new list
  eg. thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
      print(thislist)


# LIST Access
- List items are indexed and you can access them by referring to the index number.
  eg. thislist = ["apple", "banana", "cherry"]
       print(thislist[1]) # output banana // The first item has index 0.

- Negative indexing means start from the end
- slicing is possible like string but here we use index value for slicing.
  eg. thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
      print(thislist[2:5])
- same like negative indexing will work as in string.
- To determine if a specified item is present in a list use the in keyword.
  eg. thislist = ["apple", "banana", "cherry"]
        if "apple" in thislist:
            print("Yes, 'apple' is in the fruits list")

# LIST Change

- To change the value of a specific item, refer to the index number.
  eg. thislist = ["apple", "banana", "cherry"]
      thislist[1] = "blackcurrant"
      print(thislist)
       # output
       ['apple', 'blackcurrant', 'cherry']

- To change the value of items within a specific range, define a list with the new values, 
  and refer to the range of index numbers where you want to insert the new values
  eg. thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
      thislist[1:3] = ["blackcurrant", "watermelon"]
      print(thislist)
      # output 
      ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

- If you insert more items than you replace, the new items will be inserted where you specified,
  and the remaining items will move accordingly.
  eg. thislist = ["apple", "banana", "cherry"]
      thislist[1:2] = ["blackcurrant", "watermelon"]
      print(thislist)
      # ouput
      ['apple', 'blackcurrant', 'watermelon', 'cherry']

Note: The length of the list will change when the number of items inserted does not match 
      the number of items replaced.

- If you insert less items than you replace, the new items will be inserted where you specified, 
  and the remaining items will move accordingly.
  eg. thislist = ["apple", "banana", "cherry"]
      thislist[1:3] = ["watermelon"]
      print(thislist)
      # ouput
      ['apple', 'watermelon']

- To insert a new list item, without replacing any of the existing values, we can use the insert() method.
- The insert() method inserts an item at the specified index.
  eg. thislist = ["apple", "banana", "cherry"]
      thislist.insert(2, "watermelon")
      print(thislist)
      # output
       ['apple', 'banana', 'watermelon', 'cherry']

# LIST Add

- To add an item to the end of the list, use the append() method.
  eg. thislist = ["apple", "banana", "cherry"]
      thislist.append("orange")
      print(thislist)
      # output
      ['apple', 'banana', 'cherry', 'orange']

- To append elements from another list to the current list, use the extend() method.
  eg. thislist = ["apple", "banana", "cherry"]
      tropical = ["mango", "pineapple", "papaya"]
      thislist.extend(tropical)
      print(thislist)
      # output
      ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

- The extend() method does not have to append lists, you can add any iterable object 
  (tuples, sets, dictionaries etc.).
  eg. thislist = ["apple", "banana", "cherry"]
      thistuple = ("kiwi", "orange")
      thislist.extend(thistuple)
      print(thislist)
      # output
      ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# LIST Remove

- The remove() method removes the specified item.
  eg. thislist = ["apple", "banana", "cherry"]
      thislist.remove("banana")
      print(thislist)
      # output
      ["apple", "cherry"]

- If there are more than one item with the specified value, the remove() method removes 
  the first occurance.
  eg. thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
      thislist.remove("banana")
      print(thislist)
      # ouptut
      ["apple", "cherry", "banana", "kiwi"]

- The pop() method removes the specified index.
  eg. thislist = ["apple", "banana", "cherry"]
      thislist.pop(1)
      print(thislist)
      # output 
      ["apple", "cherry"]

- If you do not specify the index, the pop() method removes the last item.

- The del keyword also removes the specified index.
  eg. thislist = ["apple", "banana", "cherry"]
      del thislist[0]
- The del keyword can also delete the list completely.

- The clear() method empties the list, Tand list still remains, but it has no content.

# LIST Loop

- eg. loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

- loop with index 
Use the range() and len() functions to create a suitable iterable.
eg.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

- List Comprehension offers the shortest syntax for looping through lists.
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# LIST Comprehension
- List comprehension offers a shorter syntax when you want to create a new list based on 
  the values of an existing list.
  Example:
     Based on a list of fruits, you want a new list, containing only the fruits with the 
     letter "a" in the name.
  Without list comprehension you will have to write a for statement with a conditional test inside.
  eg. without list comprehension
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []
    for x in fruits:
    if "a" in x:
        newlist.append(x)

    print(newlist)

or

    With list comprehension you can do all that with only one line of code:
    eg. 
        fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
        newlist = [x for x in fruits if "a" in x]
        print(newlist)

The Syntax
newlist = [expression for item in iterable if condition == True]

- The expression is the current item in the iteration, but it is also the outcome, 
  which you can manipulate before it ends up like a list item in the new list.
  eg. newlist = [x.upper() for x in fruits]

- Set all values in the new list to 'hello'. we can set whatever we can.
  eg. fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
      newlist = ['hello' for x in fruits]
      print(newlist)
      # output
      ['hello', 'hello', 'hello', 'hello', 'hello']

- The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome.
  eg. newlist = [x if x != "banana" else "orange" for x in fruits]
  # output
  ['apple', 'orange', 'cherry', 'kiwi', 'mango']
  Explanation: Return the item if it is not banana, if it is banana return orange

# LIST Sort
- List objects have a sort() method that will sort the list alphanumerically, ascending, by default
    eg. 
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort()
    print(thislist)

    - To sort descending, use the keyword argument reverse = True
      thislist.sort(reverse = True)
    

- customize sort function 

   - You can also customize your own function by using the keyword argument key = function.
     The function will return a number that will be used to sort the list (the lowest number first):
     eg. Sort the list based on how close the number is to 50:

     def myfunc(n):
        return abs(n - 50)
     thislist = [100, 50, 65, 82, 23]
     thislist.sort(key = myfunc)
     print(thislist)
     # output
     [50, 65, 23, 82, 100]

- By default the sort() method is case sensitive, resulting in all capital letters being 
  sorted before lower case letters.

- So if you want a case-insensitive sort function, use str.lower as a key function
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort(key = str.lower)
    print(thislist)
    # output
    ['banana', 'cherry', 'Kiwi', 'Orange']

- The reverse() method reverses the current sorting order of the elements.
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.reverse()
    print(thislist)
    # output
    ['cherry', 'Kiwi', 'Orange', 'banana']

- cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference 
  to list1, and changes made in list1 will automatically also be made in list2.

- There are ways to make a copy, one way is to use the built-in List method copy().
  eg. 
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)

- Another way to make a copy is to use the built-in method list().
  eg. thislist = ["apple", "banana", "cherry"]
      mylist = list(thislist)
      print(mylist)

# LIST Join
There are several ways to join, or concatenate, two or more lists in Python

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

 concatenation
list3 = list1 + list2
print(list3)

or by loop 

for x in list2:
  list1.append(x)

print(list1)

or  extend()

list1.extend(list2)
print(list1)
