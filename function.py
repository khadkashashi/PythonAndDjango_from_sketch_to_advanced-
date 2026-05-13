#function------> A function is a reusable block of code that performs a specific task. Functions help make code modular, organized, and easier to maintain.

#def keyword---->Functions are defined using the def keyword followed by the function name and parentheses.
#syntax: deffuncation_name():
         #code block
#        pass

def test():
    print("i am inside function")
test()
#Parameters----->Variables listed inside the function definition.
#Arguments------> Values passed when calling the function.

def add(a, b):  # a, b = parameters
    return a + b

result = add(4, 5)  # 4, 5 = arguments

#Return Statement------>Used to send a value back to the caller.
def square(n):
    return n * n

def testing():
    a= (1,2,3,4)
    return a
data= testing()
print (data)



def function():
    a = int (input("enter the number:"))
    if a == 2:
        return 2
    else:
        return a
    print("hii")
data = function()
print (data)


# sum
def total():
    a=[67,2,45,7,9]
    sum =0
    for i in a:
        sum=sum+i
    return sum
data=total()
print(data)
