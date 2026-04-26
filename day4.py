#if condition--> block of code 
#syntax
#if (condtion):
    
if(2==1):
    print("this is true condition") #indent ie. cruser ali bhitra
else:
    print("flase condition")

age = 18
if age >=18:
    print("u can vote")
else:
    print("u cant vote")


#if+else =elif
if (2==2):
    print("this is if condition")
elif("hello"!="test"):
    print("this is elif condition")
elif (1==1):
    print (" this is 2nd elif condtion")
else:
    print("this is else")

percentage = -1

if percentage > 4.0 or percentage <0:
    print("Maximum GPA is 4.0 and minimum GPA Cant be less than 0")

elif percentage >= 3.6 and percentage <=4.0:
    print("A+")

elif percentage >= 3.2 and percentage <3.6:
    print("A")

elif percentage >= 2.8 and percentage <3.2:
    print("B+")

elif percentage >= 2.4 and percentage <2.8:
    print("B")

elif percentage >= 2.0 and percentage <2.4:
    print("C+")

elif percentage >= 1.6 and percentage <2.0:
    print("C")

elif percentage >= 1.2 and percentage <1.6:
    print("D+")

elif percentage >= 0.8 and percentage <1.2 :
    print("D")

else:
    print("Fail")
