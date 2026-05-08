#nested for loop ------> nested for loop means a loop inside another loop.
#The inner loop runs completely for each iteration of the outer loop.
for i in range(1,5,1):
    print("code block for i")
    for j in range(6,11,1):
        print(i,j)

#code block for i
#1 6
#1 7
#1 8
#1 9
#1 10
#code block for i
#2 6
#2 7
#2 8
#2 9
#2 10
#code block for i
#3 6
#3 7
#3 8
#3 9
#3 10
#code block for i
#4 6
#4 7
#4 8
#4 9
#4 10




#while loop-----> A while loop is used to repeat a block of code as long as a condition is True.
#It keeps running until the condition becomes False.

#syntax:
#  while condition:
    # block of code
    #statement(s)


i = 0
while i < 5:
    print(i)
    i += 1


i =10
while(i==10):
    print('this is while loop')
    i=11


print("------")
i=1
while(i<=10):
    print(i)
    i=i+1



#print items data using while loop
items=[
    "apple",
    "ball",
    "cat"
]
i=0
while i<len(items):
    print(items[i])
    i=i+1


#Infinite Loop Example
while True:
    print("Hello")


# Important Points
#Condition is checked before each iteration
#If condition never becomes False → infinite loop
