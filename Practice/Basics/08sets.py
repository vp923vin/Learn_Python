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

#################################################################

# 1 Create a set named colors containing the items: "red", "green", "blue"?
colors = {"red", "green", "blue"}
print(colors)

# 2 Add the item "yellow" to the colors set.
colors.add("yellow")
print(colors)

# 3 Update the colors set with the items from another set: extra_colors = {"purple", "orange"} ?
extra_colors = {"purple", "orange"}
colors.update(extra_colors)
print(colors)

# 4 Remove "green" from the colors set using both the remove() and discard() methods. 
# Observe the difference in behavior if "green" is not in the set.

colors.remove("green1")
print(colors)

colors.discard("green")
print(colors)

# difference between the remove and discard that if key is not present in the set then remove give an error but discard will not give an error.

# 5 Clear all items from the colors set.
colors.clear()
print(colors)

# 6 Check if "blue" is an item in the set colors.
if "blue" in colors:
    print("blue is present in the colors set")
else:
    print("blue color is not present in colors")

# 7 Loop through the set colors and print each item.

for i in colors:
    print(i)

# 8 Create two sets, setA = {"apple", "banana", "cherry"} and setB = {"google", "microsoft", "apple"}. Find the union of these sets.

setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple"}
setC = setA.union(setB)
print(setC)

# or 

setC = setA | setB
print(setC)

# 9 Using setA and setB, find the intersection of these sets.

setC = setA & setB
print(setC)

# or 

setC = setA.intersection(setB)
print(setC)

# 10 Using setA and setB, find the difference between setA and setB.
setC = setA.difference(setB)
print(setC)

# or 

setC = setB - setA
print(setC)

# 11 Using setA and setB, find the symmetric difference between these sets.
setA.symmetric_difference(setA)
print(setA)

# 12 Using the update() method, merge setB into setA.
setA.update(setB)
print(setA)

# 13 Update setA to keep only the items that are also present in setB using intersection_update().
setA.intersection_update(setB)
print(setA)

# 14 Update setA to remove the items that are present in setB using difference_update().
setA.difference_update(setB)
print(setA)

# 15 Update setA to keep only the items that are not present in setB using symmetric_difference_update().
setA.symmetric_difference_update(setB)
print(setA)

# 16 Join the set numbers = {1, 2, 3} with the list more_numbers = [4, 5, 6] using the union() method.
numbers = {1, 2, 3}
more_numbers = [4, 5, 6]
result = numbers.union(more_numbers)
print(result)

# 17 Given a list names = ["Anna", "Bob", "Anna", "Cathy"], remove the duplicates using a set.
names = ["Anna", "Bob", "Anna", "Cathy"]
setA = list(set(names))
print(setA)

# 18 Given two sets, setX = {1, 2, 3} and setY = {1, 2, 3, 4, 5}, check if setX is a subset of setY
setX = {1, 2, 3}
setY = {1, 2, 3, 4, 5}
setZ = setX.intersection(setY)
if setZ == setX:
    print("setX is a subset of setY")
else:
    print("setY is not a subset of setY")

# or 
print(setX.issubset(setY))

# 19 Create a set comprehension that generates a set of even numbers from 1 to 20
setComp = set(x for x in range(1, 21))
print(setComp)

# 20 Given two lists, list1 = [1, 2, 3, 4, 5] and list2 = [4, 5, 6, 7, 8], find the common elements using sets.
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# result = set(list1).intersection(list2)
print(result)

# 21 Write a function that takes a sentence as input and returns a set of unique words in the sentence.

sentence = "hello, world this is a test of set World is a world."
print(set(sentence.split()))

# or 

def unique_set(sentence):
    return set(sentence.split())
sentence = "hello, world, this is a test of set World is a world."
print(unique_set(sentence))

# 22 Given two strings, str1 = "hello" and str2 = "world", find the common characters using sets.
str1 = "hello"
str2 = "world"
print(set(str1).intersection(str2))

# 23 Write a function that returns a set of prime numbers up to a given number n
# def prime_numbers(n):
#     primes = set()
#     for num in range(2, n + 1):
#         is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
#         if is_prime:
#             primes.add(num)
#     return primes

# print(prime_numbers(20))

# 24 Given three sets, set1 = {1, 2, 3}, set2 = {3, 4, 5}, and set3 = {5, 6, 7}, 
# find the symmetric difference of all three sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
result =  set1.symmetric_difference(set2).symmetric_difference(set3)
print(result)
