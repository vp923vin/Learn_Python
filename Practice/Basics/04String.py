#  strings
a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt) 

# string slicing
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

# STRING Modifiying

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

# string concat

a = "Hello"
b = "World"
c = a + " " + b
print(c) 

# STRING Formatting

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# STRING Escape Character
# txt = "We are the so-called "Vikings" from the north."
# error in string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(15))

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))