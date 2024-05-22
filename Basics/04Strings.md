# STRINGS Basics
- strings length start from 0 index.
- Strings in python are surrounded by either single quotation marks, or double quotation marks.
- Assigning a string to a variable is done with the variable name followed by an equal sign and the string.
- You can assign a multiline string to a variable by using three quotes.

Note: in the result, the line breaks are inserted at the same position as in the code.

# Strings are Arrays
    - Like many other popular programming languages, strings in Python are arrays of bytes representing 
      unicode characters.
    - However, Python does not have a character data type, a single character is simply a string with a length of 1.
    - Square brackets can be used to access elements of the string.

    eg. a = "Hello, World!"
            print(a[1])  #output e

# loop string
    for x in "banana":
        print(x)

# To get the length of a string, use the len() function.

# check String

- To check if a certain phrase or character is present in a string, we can use the keyword in.
  txt = "The best things in life are free!"
  print("free" in txt)  # output True

    txt = "The best things in life are free!"
    if "free" in txt:
        print("Yes, 'free' is present.") 

# Check if NOT
- To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
    txt = "The best things in life are free!"
    print("expensive" not in txt) # output True


# STRING Slicing
- Specify the start index and the end index, separated by a colon, to return a part of the string.
   eg. b = "Hello, World!"
       print(b[2:5]) # output llo

- By leaving out the start index, the range will start at the first character
  eg. b = "Hello, World!"
      print(b[:5]) # output Hello

- By leaving out the end index, the range will go to the end
  eg. b = "Hello, World!"
      print(b[2:]) #output llo, World!

- Use negative indexes to start the slice from the end of the string
- negative indexing start from end
  eg. b = "Hello, World!"
      print(b[-5:-2]) #output orl

# STRING Modifiying
- The upper() method returns the string in upper case.
  eg. a = "Hello, World!"
      print(a.upper()) # output HELLO, WORLD!

- The lower() method returns the string in lower case:
  eg. a = "Hello, World!"
      print(a.lower()) #output hello, world!

- Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
- The strip() method removes any whitespace from the beginning or the end.
  eg. a = " Hello, World! "
      print(a.strip()) # output "Hello, World!"

- The replace() method replaces a string with another string
  eg. a = "Hello, World!"
      print(a.replace("H", "J")) 

- The split() method returns a list where the text between the specified separator becomes the list items.
- The split() method splits the string into substrings if it finds instances of the separator.
  eg. a = "Hello, World!"
      print(a.split(",")) # output ['Hello', ' World!']


# STRING Concatenation

- To concatenate, or combine, two strings you can use the + operator.
  eg. a = "Hello"
      b = "World"
      c = a + b
      print(c)  # output HelloWorld

# STRING Formatting

- we cannot combine strings and numbers like this
  eg. age = 36
      txt = "My name is John, I am " + age
      print(txt) 
      # output error
      Traceback (most recent call last):
        File "demo_string_format_error.py", line 2, in <module>
            txt = "My name is John, I am " + age
        TypeError: must be str, not int

Note: But we can combine strings and numbers by using f-strings or the format() method!

# F-Strings python(3.6)

- To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} 
  as placeholders for variables and other operations.
  eg. age = 36
      txt = f"My name is John, I am {age}"
      print(txt)
      # output 
      My name is John, I am 36

- A placeholder can contain variables, operations, functions, and modifiers to format the value.
- placeholder can include a modifier to format the value.
- A placeholder can contain Python code, like math operations.
- A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means 
  fixed point number with 2 decimals.
  eg. price = 59
      txt = f"The price is {price:.2f} dollars"
      print(txt)
      # output
      The price is 59.00 dollars

# STRING Escape Character

- To insert characters that are illegal in a string, use an escape character.
- An escape character is a backslash \ followed by the character you want to insert.
- give error invalid syntax
  eg. txt = "We are the so-called "Vikings" from the north."

- To fix this problem, use the escape character \".
  eg. txt = "We are the so-called \"Vikings\" from the north."


# Boolean True/Flase
print(10 > 9)
print(10 == 9)
print(10 < 9)
# output
True
False
False
- The bool() function allows you to evaluate any value, and give you True or False in return.
    print(bool("Hello"))
    print(bool(15))
    # output 
    True
    True


- Almost any value is evaluated to True if it has some sort of content.
- Any string is True, except empty strings.
- Any number is True, except 0.
- Any list, tuple, set, and dictionary are True, except empty ones.

Some Values are False

- In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
  the number 0, and the value None. And of course the value False evaluates to False.

- One more value, or object in this case, evaluates to False.
- if you have an object that is made from a class with a __len__ function that returns 0 or False
    eg. class myclass():
        def __len__(self):
            return 0

        myobj = myclass()
        print(bool(myobj))


# Operators

Python divides the operators in the following groups:

    - Arithmetic operators (-, +, %, *, /, //, **)
    - Assignment operators (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=)
    - Comparison operators (==, !=, >, <, >=, <=)
    - Logical operators (and, or, not)
    - Identity operators (is, is not)
    - Membership operators (in, not in)
    - Bitwise operators (&, |, ^, ~, <<, >>)

