
#difference
   - repr()
   - str()
   - print()

1 - repr(): 
    It shows the official string representation, which is useful for debugging.
    Shows the "official" string representation of an object, useful for debugging.
    Output: Should look like a valid Python expression that could be used to recreate the object.
    x = 3.14
    print(repr(x))  # Output: '3.14'

2 - str(): 
    It shows a human-readable representation, which is useful for displaying to the end user. 
    Shows a "nice" string representation of an object, meant to be readable.
    Output: Human-readable form.
    x = 3.14
    print(str(x))  # Output: '3.14'

3 - print(): 
    The print() function internally calls str(obj), so it outputs the same as str(obj).
    Outputs text to the console.
    How it works: Uses str() to convert objects to strings before printing.
    x = 3.14
    print(x)  # Output: 3.14

 There are three numeric types in Python:

  - int
  - float
  - complex

   x = 1    # int
   y = 2.8  # float
   z = 1 + 1j   # complex

 - To verify the type of any object in Python, use the type() function.
 - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
 - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
 - Complex numbers are written with a "j" as the imaginary part.
 - It can be converted from one type to another with the int(), float(), and complex() methods.
 - Python does not have a random() function to make a random number, but Python has a built-in module 
   called random that can be used to make random numbers.
   
'''
   import random
   print(random.randrange(1, 10))

'''
 Note: - You cannot convert complex numbers into another number type.

       
