# Pyhton Keywords


#	and \   A logical operator
x = (5 > 3 and 5 < 10)
print(x) # The return value will only be True if both statements return True, otherwise it will return False

if 5 > 3 and 5 < 10:
    print("Both statements are True")
else:
    print("At least one of the statements are False")


#	as  \   To create an alias
import calendar as c
print(c.month_name[1]) # In the example above, we create an alias, c, when importing the calendar module, and now we can refer to the calendar module by using c instead of calendar.


#	assert  \   For debugging
x = "hello"
#if condition returns True, then nothing happens:
assert x == "hello"
#if condition returns False, AssertionError is raised:
assert x == "goodbye" # this return the error

x = "hello"
#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"


#	break	\   To break out of a loop
for i in range(9):
    if i > 3:
        break # The break keyword is used to break out a for loop, or a while loop.
    print(i)

i = 1
while i < 9:
    print(i)
    if i == 3:
        break
    i += 1


#	class	\   To define a class
class Person: # A class is like an object constructor
    name = "John"
    age = 36
p1 = Person()
print(p1.name)


#	continue    \   To continue to the next iteration of a loop
for i in range(9):
    if i == 3:
        continue # The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
    print(i)

i = 0
while i < 9:
    i += 1
    if i == 3:
        continue
    print(i)


#	def \   To define a function
def my_function():
    print("Hello from a function")
my_function()

def main():
    print('I am the main fonction')
main()


#	del \   To delete an object
class MyClass:
    name = "John"
del MyClass # In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
print(MyClass)

x = "hello"
del x
print(x) # NameError: name 'x' is not defined


#	elif    \   Used in conditional statements, same as else if
for i in range(-5, 5):
  if i > 0:
    print("YES")
  elif i == 0:
    print("WHATEVER")
  else:
    print("NO")


#	else	\   Used in conditional statements
x = 2
if x > 3:
    print("YES")
else: # decides what to do if the condition is False.
    print("NO")
# Use the else keyword in a try...except block to define what to do if no errors were raised:\
x = 5
try:
    x > 10
except:
    print("Something went wrong")
else:
    print("The 'Try' code was executed without raising any errors!")


#	except  \   Used with exceptions, what to do when an exception occurs
try:
    x > 3
except:
    print("Something went wrong")
# It defines a block of code to run if the try block raises an error.
# You can define different blocks for different error types, and blocks to execute if nothing went wrong, see examples below.

# Write one message if it is a NameError, and another if it is an TypeError:
x = "hello"
try:
    x > 3
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")

# Try to execute a statement that raises an error, but none of the defined error types (in this case, a ZeroDivisionError):
try:
    x = 1/0
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")
except:
    print("Something else went wrong")

# Write a message if no errors were raised:
x = 1
try:
    x > 10
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")
else:
    print("The 'Try' code was executed without raising any errors!")


#	False	\   Boolean value, result of comparison operations
print(5 > 6) # Return "False"
# The False keyword is a Boolean value, and result of a comparison operation.
# The False keyword is the same as 0 (True is the same as 1).

# Other comparisons that returns False:
print(5 > 6)
print(4 in [1,2,3])
print("hello" is "goodbye")
print(5 == 6)
print(5 == 6 or 6 == 7)
print(5 == 6 and 6 == 7)
print("hello" is not "hello")
print(not(5 == 5))
print(3 not in [1,2,3])


#	finally	\   Used with exceptions, a block of code that will be executed no matter if there is an exception or not
try:
    x > 3
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The try...except block is finished")
# The finally keyword is used in try...except blocks. It defines a block of code to run when the try...except...else block is final.
# The finally block will be executed no matter if the try block raises an error or not.
# This can be useful to close objects and clean up resources.


#	for	\   To create a for loop
for x in range(1, 9): # It can be used to iterate through a sequence, like a list, tuple, etc.
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


#	from	\   To import specific parts of a module
from datetime import time # datetime is called a module, while time is a section of the module
x = time(hour=15)
print(x)


#	global	\   To declare a global variable
#create a function:
def myfunction():
    global x # The global keyword is used to create global variables from a no-global scope, e.g. inside a function.
    x = "hello" # Declare a global variable inside a function, and use it outside the function:
#execute the function:
myfunction()
#x should now be global, and accessible in the global scope.
print(x)


#	if	\   To make a conditional statement
x = 5
if x > 3:
    print("YES")
# The if keyword is used to create conditional statements (if statements), and allows you to execute a block of code only if a condition is True.

# Use the else keyword to execute code if the condition is False, see example below.
x = 5
if x > 6:
    print("YES")
else:
    print("NO")


#	import	\   To import a module
import datetime
x = datetime.datetime.now()
print(x)


#	in	\   To check if a value is present in a list, tuple, etc.
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("yes")

# The in keyword has two purposes:
# The in keyword is used to check if a value is present in a sequence (list, range, string etc.).
# The in keyword is also used to iterate through a sequence in a for loop:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


#	is	\   To test if two variables are equal
x = ["apple", "banana", "cherry"]
y = x
print(x is y)

# The is keyword is used to test if two variables refer to the same object.
# The test returns True if the two objects are the same object.
# The test returns False if they are not the same object, even if the two objects are 100% equal.
# Use the == operator to test if two variables are equal.
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y)


#	lambda	\   To create an anonymous function
x = lambda a : a + 10
print(x(5))

# The lambda keyword is used to create small anonymous functions.
# A lambda function can take any number of arguments, but can only have one expression.
# The expression is evaluated and the result is returned.
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


#	None	\   Represents a null value
x = None
print(x)
# The None keyword is used to define a null value, or no value at all.
# None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.

# If you do a boolean if test, what will happen? Is None True or False:
x = None
if x:
    print("Do you think None is True?")
elif x is False:
    print ("Do you think None is False?")
else:
    print("None is not True, or False, None is just None...")


#	nonlocal	\   To declare a non-local variable
def myfunc1():
    x = "John"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x
print(myfunc1())
# The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
# Use the keyword nonlocal to declare that the variable is not local.

# Same example as above, but without the nonlocal keyword:
def myfunc1():
    x = "John"
    def myfunc2():
        x = "hello"
    myfunc2()
    return x
print(myfunc1())


#	not	\   A logical operator
x = False
print(not x)
# The not keyword is a logical operator.
# The return value will be True if the statement(s) are not True, otherwise it will return False.


#	or	\   A logical operator
x = (5 > 3 or 5 > 10)
print(x)  # Return True if one of the statements are True:
# The or keyword is a logical operator.
# Logical operators are used to combine conditional statements.
# The return value will be True if one of the statements return True, otherwise it will return False.

# Using the or keyword in an if statement:
if 5 > 3 or 5 > 10:
    print("At least one of the statements are True")
else:
    print("None of the statements are True")


#	pass	\   A null statement, a statement that will do nothing
for x in [0, 1, 2]:
    pass # Create a placeholder for future code:
# The pass statement is used as a placeholder for future code.
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

# Using the pass keyword in a function definition:
def myfunction():
    pass

# Using the pass keyword in a class definition:
class Person:
    pass

# Using the pass keyword in an if statement:
a = 33
b = 200
if b > a:
    pass


#	raise	\   To raise an exception
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero") # Raise an error and stop the program if x is lower than 0:
# You can define what kind of error to raise, and the text to print to the user.

# Raise a TypeError if x is not an integer:
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")


#	return	\   To exit a function and return a value
def myfunction():
    return 3+3 # The return keyword is to exit a function and return a value.
print(myfunction())

# Statements after the return line will not be executed:
def myfunction():
    return 3+3
    print("Hello, World!")
print(myfunction())


#	True	\   Boolean value, result of comparison operations
print(7 > 6)
# The True keyword is a Boolean value, and result of a comparison operation.
# The True keyword is the same as 1 (False is the same as 0).

# Other comparisons that returns True:
print(5 < 6)
print(2 in [1,2,3])
print(5 is 5)
print(5 == 5)
print(5 == 5 or 6 == 7)
print(5 == 5 and 7 == 7)
print("hello" is not "goodbye")
print(not(5 == 7))
print(4 not in [1,2,3])


#	try	\   To make a try...except statement
try:
    x > 3
except:
    print("Something went wrong")
# The try keyword is used in try...except blocks. It defines a block of code test if it contains any errors.
# You can define different blocks for different error types, and blocks to execute if nothing went wrong, see examples below.

# Raise an error and stop the program when there is an error in the try block:
try:
    x > 3
except:
    Exception("Something went wrong")


#	while	\   To create a while 
x = 0
while x < 9: # A while loop will continue until the statement is false.
    print(x)
    x = x + 1


#	with	\   Used to simplify exception handling

#	yield	\   To end a function, returns a generator
