# update sets 
# add multiple elements, list, tuple, or dictionary

thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"} # 1
tropical = "pineapple" #2
thisset.update(tropical)
print(thisset)
# output
# {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'} 1
# {'banana', 'i', 'a', 'e', 'l', 'cherry', 'p', 'apple', 'n'}   2

# add single element
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#eg.2

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # final set of elements
print(type(thisset)) #type of the set
print(len(thisset))  # print length



# remove items from sets
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # this method can raise error
print(thisset)



thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") # this method canot raise error
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.pop() # this method randomly delete tne element
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)


# lopp element of the set

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# set joins methods
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set2.union(set1)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)


x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

