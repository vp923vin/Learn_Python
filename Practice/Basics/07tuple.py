thistuple = ("apple",)
print(type(thistuple))
# output tuple

thistuple = ("apple")
print(type(thistuple))
# output str

# # with one element it treat as a string if want to make it a tuple then add another element or add a comma.

thistuple = tuple(("apple", "banana", "cherry")) # constructor way to create a tuple
print(thistuple)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:-1])

# update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(y)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# 1 Create a tuple named fruits with the items: "apple", "banana", "cherry".
fruits = ("apple", "banana", "cherry")
print(fruits)
print(type(fruits))

# 2 Access the first item of the fruits tuple and print it.
print(fruits[0])

# 3 Access the last item of the fruits tuple using negative indexing and print it.
print(fruits[-1])

# 4 Slice the fruits tuple to get the first two items and print the result.
print(fruits[:-1])

# 5 Print the length of the fruits tuple.
print(len(fruits))

# 6 Create a tuple named single_item containing only one item, "apple", and print its type.
single_item = ("apple",)
print(type(single_item))

# 7 Convert the list vegetables = ["carrot", "broccoli", "spinach"] to a tuple and print it.
vegetables = ["carrot", "broccoli", "spinach"]
print(tuple(vegetables))

# 8 Convert the tuple fruits to a list, change "banana" to "kiwi", and convert it back to a tuple. Print the result.
y = list(fruits)
y[1] = "kiwi"
fruits = tuple(y)
print(fruits)
    
# 9 Add "orange" to the fruits tuple by converting it to a list, then converting it back to a tuple. Print the result.
y = list(fruits)
y.append("orange")
fruits = tuple(y)
print(fruits)

# 10 Create a new tuple more_fruits = ("orange", "grape"). Concatenate it with the fruits tuple and print the result.
more_fruits = ("orange", "grape")
fruits += more_fruits
print(fruits)

# 11 Delete the fruits tuple and try to print it. Observe the result.
del fruits
print(fruits)

# 12 Unpack the fruits tuple into three variables and print each variable.

(apple , orange, grape) = fruits
print(apple)
print(orange)
print(grape)

# 13 Create a tuple colors = ("red", "blue", "green", "yellow", "purple").
#  Unpack the first two colors into variables and the rest into a list. Print the results.
colors = ("red", "blue", "green", "yellow", "purple")
(red, blue, *green) = colors
print(red)
print(blue)
print(green)

# 14 Loop through the fruits tuple and print each item.
for fruit in fruits:
    print(fruit)

# 15 Join the tuple fruits with more_fruits and print the result.
fruits += more_fruits
print(fruits)

# 16 Create a tuple numbers = (1, 2, 3) and multiply it by 3. Print the result.
numbers = (1, 2, 3) * 3
print(numbers)

# 17 Check if "apple" is in the fruits tuple and print the result.
if "apple" in fruits: 
    print("apple is already exists")

# 18 Create a tuple numbers = (1, 2, 3, 2, 4, 2, 5) and count how many times 2 appears in the tuple. Print the result.
numbers = (1, 2, 3, 2, 4, 2, 5)
count = 0
for x in numbers:
    if 2 == x:
        count += 1

print(count)

# 19 Find the index of the first occurrence of 2 in the numbers tuple and print it.
iteration = 0
indexes = list()
for x in numbers:
    if x == 2:
        indexes.append(iteration)
        print(x)
    iteration += 1
    
print(indexes)
        

# 20 Create a nested tuple nested = ((1, 2, 3), ("a", "b", "c")). Access and print the element "b".

nested = ((1, 2, 3), ("a", "b", "c"))
print(nested[1][1])

