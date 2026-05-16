#function------> A function is a reusable block of code that performs a specific task. Functions help make code modular, organized, and easier to maintain.

#def keyword---->Functions are defined using the def keyword followed by the function name and parentheses.
#syntax: deffuncation_name():
         #code block
#        pass

def test():
    print("i am inside function")
test()
#Parameters----->Variables listed inside the function definition.
def adding(a,b):
    return a+b
print(adding(10,20))
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



#default args---------> A default argument in Python is a parameter that already has a value assigned to it.
#If the user does not pass a value while calling the function, Python uses the default value.
#syntax:
#def function_name(parameter=value):
    # code
def area (r,pie=3.14):
    area_of_circle= pie*r**2
    return area_of_circle
print(area(7,2))
print(area(2,12))



#positional ----- A positional argument is an argument passed to a function based on its position/order.
#example 1:
def student(name, age):
    print(name, age)
student("Shashi", 20)
#Shashi 20

#example 2:
def user_info(fname,lname):
    return f'First name is {fname} and last name is {lname}'
print(user_info('sudan',"bhandari"))
print(user_info("khadka","shashi"))
#First name is sudan and last name is bhandari
#First name is khadka and last name is shashi

#example 3---> default and positional
def area (r,pie=3.14):
    area_of_circle= pie*r**2
    return area_of_circle
print(area(7,2))
print(area(2,12))



#keyword arg -----> A keyword argument in Python means passing arguments using the parameter name while calling a function.
#syntax: function_name(parameter=value)


def student(name, age):
    print(name, age)

student(age=20, name="Shashi")
#Shashi 20

def user_info(age,fname,lname):
    return f'First name is {fname} and last name is {lname} and age is {age}'

print(user_info(lname="khadka", fname='shashi',age=22))
#First name is shashi and last name is khadka and age is 22



def calculate_bill(item,item_price,quantity,tax_rate=0.13,discount=0):
    total =item_price*quantity*tax_rate-(discount/100)
    print("total",total)
    return total
print(calculate_bill("mac",1200,2,tax_rate=0.13,discount=10))





#def add(*data)---> catch all data, *data collects all values as positional arguments into a tuple.
def add (*data): # stay in tuple
    print(data)
    return data

add(1,2,"jsdh",3,[12,12,345])
#add(1,2,3)
#add(1)
#* means: "Accept any number of positional arguments"








def data1(**kwargs):
    print(type(kwargs))
    print(kwargs.values())
    print(kwargs.keys())
    
    if "age" in kwargs.keys():
        print('age=',kwargs['age'])
    else:
        print("age is not found")
    return kwargs

data1(fname="shashi", num=1234,address="")


#age=kwargs.get("age")
#print(age)
#if age is None:
#    print("age is missing")
#else:
#print(age)



#def marks_sheet(*args,**kwargs):...#pass
def marks_sheet(*args,**kwargs):
    pass
print(marks_sheet(100,38,98,45,name="hari",grade=10))




def marks_sheet(*args,**kwargs):
    avg= sum(args)/len(args)
    #print(avg)
    #print(args)
    #print(kwargs)
    return f'{kwargs.get('name')}  obtain{avg}%'
print (marks_sheet(100,2354,345,name="shashi",grade=14))
print(marks_sheet(10,24,34,name="shashi",garde =12))



def marks_sheet(*args,**kwargs):
   avg= sum(args)/len(args)
   max_num =max(args)
   min_num= min(args)
   max_number=args[0]
   min_number=args[0]
   for i in args:
       if i >max_number:
           max_number=i
   return f'{kwargs.get('name')}  obtain{avg}% and max number is {max_num}and min number is {min_num}'
print (marks_sheet(100,2354,345,name="shashi",grade=14))
print(marks_sheet(10,24,34,name="shashi",garde =12))

#fact
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(factorial(5))

#count
def count_digits(n):
    count = 0
    for i in str(n):
        count += 1
    return count

print(count_digits(12345))

#rev
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

print(reverse(1234))