#Arithmetic Operators:
#+ Addition
#- Subtraction
#* Multiplication
#/ Division (float)
#// Floor Division
#% Modulus (remainder)
#** Exponentiation



print(1+1)
print(5-2)
print(7-6)
print(10/7)


#** --> exponentiation, only works in integer
print(2**10) #2 ko cube
#% modulas 
#% print remainder

print(10%3)
#// double slace, only answer in int.use when point number is not imp
print (10//3)


# for string +,*,  +--> (concatination)
a= "hello"
b="world"
print (a+b)

a= "hello"
b= 55
print (a+str(b))# b lai string ma convert gareko type casting

#pydantic v2-->  manage conflict of data manage.


#multiplication for string, one variable should be int.
a="hello"
b=3
print(a*b)

#comparision operator --> ==,<>,<=,>=,!=, answer is either true or false. used loops, comparisons, filtering, if/else statement, loops and conditions.
#= --> data assign, == -->value compare

# How Comparison Operators Work
#They compare values (numbers, strings, variables)
#They return True or False
#Useful in loops, comparisons, and filtering if/else statements, loops, and conditions

print ("sudan"!="sudan")
print (5>10)
print (5<10)
print (5!=3)
print(4<=6)
print(5==5)
print (6>=6)

#and or not
print(True and False)
print ("sudan" == "sudan" and 1<=100 )


#Python Logical Operators
#Logical operators in Python are used to combine conditions and return a boolean result (True or False).

#List of Logical Operators
#Operator	Meaning	                                Example	           Result
#and	    True only if both conditions are true	5 > 3 and 10 > 5	True
#or	        True if at least one condition is true	5 > 10 or 3 < 8	    True
#not	    Reverses (negates) the result	        not (5 > 3)     	False

#Examples
# Using and
age = 20
citizen = True
print(age >= 18 and citizen)  # True

# Using or
is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)  # True

# Using not
logged_in = False
print(not logged_in)  # True

#Key Points
#and → All conditions must be True
#or → At least one condition must be True
#not → Converts True → False and False → True