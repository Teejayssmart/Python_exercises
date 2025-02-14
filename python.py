# #variable types
# Strings : "anything here is a string"
# Integers : a number
# Boolean: to check value  type. it includes True and False
# type function = type() will check variable type of a value
# logic error: code will run but with error
# = is assignment value used in variable
#
# CONCEPT OF SWITCH VARIABLE
# if a = 2
#     b = 3
# make a = 3 and b = 3
# concept solution =
# create another variable to hold a's content which is 2
# therefore;
# c = 2
# now, a will be empty
# move b's content into a'
# a = 3
# b will now be empty
# transfer c content into b
# b = 2
# c will now be empty again
#
# a = 3
# b = 2
#
# ----------------------------
# OPERATORS
# ** = exponential e.g 5 ** 2 = 5 raise to power 2 = 25
#
# division will always give floating number results
#
# Priority in operators
# PEMDAS
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Subtraction
#
# % = modulus will give remainder numbers
# Also used to find a divisible numbers
# Also use to extract digits
#
# + is use to merge together 2 or more strings
# it is called concertenate
# does not work for int
# ---------------------------------------------------
# Input Function
# input()
# \n = new line character which can be used in strings
#
#
#
#
# ----------------------------------------
# len() = lenght function
# prints out characters
# ** does not work with integers as input
#
#
#
#
#
# ----------------------------
# ERRORS
# type errors = shows type of data errors
#
#
#
#
#
#
# -------------------------------
# CONVERT INTEGER TO STRING
# use str function = str()
#
#
#
#
# -----------------------------
# BOOLEAN EXPRESSIONS
# conditional executions
#  == is an equal sign use to check an expression if true or false
#
# == is an expression
# = is assignment operator
# != not equal to
# > greater than
# < less than
# >= is greater than or equal to
# <= is less than or equal to
#
# -----------------------------------------
# Conditional IF/ELSE CONCEPT
#
# There must be a condition
# And there will be a result whether condition is true or not true
#
# if condition:          (is true)
#     do this
# else:                  (if condition is not true)
#     do this
# Only two choices
#
# ------------------------------------------
# NESTED CONDITIONALS
#if first condition is not true, the rest
# inner\nested condition will not be checked
import string

# if condition1:
#     if condition2:
#         do this
#     else:
#         do this
# else:
#     do this
#
#
# -----------------------------------------------
# CHAINED CONDITIONAL
#
# use when you have multiple conditions
# only one branch will be executed and True
# where only one condition is needed to be true
if condition1:
    do this
elif condition2:
    do this
elif conditon3:
    do this
else:
    do this

-----------------------------------------------------
MULTIPLE IF STATEMENT
after checking condition1

multiple condition can be checked
And multiple condition can be true
if condition1:
    do this
if condition2:
    do this
if condition3:
    do this

-------------------------------------------------
LOGICAL OPERATORS
use to combine more than one condition:
"and"  both conditions needs to be True
"or" one condition needs to be True


--------------------------------------------------
TRY AND EXCEPT

Try:
     execute this part of code to see if it runs
except:
     do this if there was an exception
else:
      do this part if no exception

--------------------------------------------------
FUNCTION
INBUILT FUNCTION
* ready made function by python

-----------------------------------------
MATH MODULE
helps users to get access to mathmatical function in python
* use import math
use dot notations .

*How to create own module and import it

1. create another .py file and name it e.g. clasic.py
2. write ur code inside
3. go to main .py file and use import name of module
 import clasic

 -----------------------------------------------------
 RANDOMIZATION IN PYTHON
import random module
*import random
 new_number = random.randint(1,21)


-------------------------------------------
LIST
a_list = [a,b,c,d]
*to choose a particular index , use
a_list[2] = will produce "c"
to change index, assign new variable to the index
a_list[2] = f
a_list will now be:
a_list = [a,b,f,d]
* in a reverse row
a_list[-2] will be f
**To add to the end of a list , use append**
a_list.append("z")
a_list = [a,b,f,d,z]

ITERATIONS IN A LIST
--------------------------------------------------
To loop through a list, use for loop
e.g
for items in list_of_items:
    do this
for index in range(len(variable)):

a_list = [a,b,c,d]
for alphabet in a_list

-----------------------------------------
RANGE FUNCTION
*to loop through a set of list or numbers that are not provided
use range function
for number in range(1,11)
    print(number)
*will print numbers from 1 to 10
----------------------------------------------
REVERSE RANGE

for num in range(start, stop, decrement):
for number in range(1,11)
range does not work for strings

**Therefore, to loop through a list of numbers, use
for num in range(0,6)



    to loop through a set of strings, use
    for diff in differences:
        do this shit here#

-----------------------------------------
DATA STRUCTURE
ALGORITHM
STRINGS
**use len() function to count the numbers in a string.
**to get the last alphabet in a string, use -1
STRING TRAVERSAL
**this means to visit each letter in a string, do
something with it and move on .
to traverse using a for
    use for char in variable
        index = 0
to use while loop
    while index < len(variable)

------------------------------------
use in while looking for substring in string
------------------------------------------------
SLICING CONCEPT

sequence[start:end:step]
start: The index where the slice begins (inclusive).
end: The index where the slice ends (exclusive).
step: (Optional) The number of steps between each index in the slice.
----------------------------------------------------------------------------
PARSING STRING
Is a way of finding a substring in a string
vaiable.find('')