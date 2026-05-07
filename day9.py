#what is loop---> A loop is used to execute a block of code repeatedly until a condition is met.

#Python mainly provides:
#1.for loop → used when the number of iterations is known or when iterating over a sequence
#2.while loop → used when the number of iterations is not known and depends on a condition

#for Loop in Python
#A for loop is used to iterate over a sequence such as:list,tuple,string,dictionary,range
#Syntax
#for variable in sequence:
 #   statements

for i in[1,2,3,4,5,6]:
    print(i)

a= "ram"
for i in a:
    print(i)

b="broadway"
print("this is string index 0",a[0])

#Iterating Over Different Data Types
#list
numbers = [10, 20, 30]
for n in numbers:
    print(n)

#String
for ch in "Python":
    print(ch)

#Dictionary
data={
    "name":"shashi",
    "address":"nepal"
}
for i in data:
    print(i)
    print(f'{i}={data[i]}')
print(data.items())
for key, value in data.items(): #.items() is a dictionary method in Python.It returns both the key and value of a dictionary together.
    print(key,value)



items=[
    "apple",
    "ball",
    "cat",
    "dog",
    "elephant",
    "fish"

]
for index, data in enumerate(items): #enumerate() is a built-in Python function used to get both the index and the value while looping through a list, tuple, string, etc.
    #print(index)
    #print(data)
    print(index+1,data)

#range() function ---->range(start(optional ,by default stat with 0),stop(magnetory),step(optional, by default 1))
for i in range(1,20,2):
    print(i)

print('---------')
for i in range(20,1,-1):
    print(i)

#print even and odd number in list
even=[]
odd=[]
for num in range(1,20):
    if(num%2==0):
        even.append(num)
    
    else:
        odd.append(num)
print(even)
print(odd)



#Loop Control Statements
#1. break--> Stops the loop immediately.
for i in range(1,10,1):
    if i==4:
        break
    print(i)


#2.continue----->Skips the current iteration and moves to the next.
for i in range(1,10,1):
    if i == 5:
        continue
    print(i)


#Difference Between break and continue in Python
#break	                      continue
#Stops the loop completely	  Skips current iteration
#Exits the loop	              Moves to next iteration
#Used when loop should end	  Used when some values should be skipped

