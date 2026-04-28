#nested if (if inside if)
#Used when you want to check multiple conditions inside another condition.


if (1==1):
    print ("this is true")
else:
    if (2==2):

        print("these 2 are equal")
    print("this is false")


age =19
country = "nepal"
if(age>=18):
    if country =="nepal":
        print("eligible for license")
    elif country =="india":
        print("special licence for saarc country")
    else:
        print("not eligible for license")
else:
    print("under age")


gender = "M"

if gender =="M":
    print("male")
else:
    print ("female")


data = "male" if gender == "M" else "female"
print (data)




#list
print ("---------------------"*2)
#lists are ordered collection of data items.
#they store multiple items in a single variable
#list items are separated by commas and enclosed within square brackets [].
#list are changeable meaning we can alter then after creation
# start with index[0]
# Creating a list of string
#mutable data ie removeable and addable
list1 = ["Apple", "Banana", "Cherry", "Orang"]

# Creating a list of integers

list2 = [1, 4, 7, 3, 6, 0, 12, 23]

# Creating a list of boolean data type

list3 = [True, False, True, True, False]

# Craeting a list of float data type

list4 = [17.3, 71.3, 34.5, 87.0, 23.4]


# Creating a list with string, integers and boolean and float data type
list5 = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
print(type(list5))
print(list5[0])
print(list5[-1])
print(len(list5)) # start with index[1]
print(len(list5)-1) # total data





#slicing
#It is possible to access a section of items from the list using the slicing operator :, not just a single item

print (list5[0:5])
print(list5[1:])
print(list5[:6])
print(list5[:]) # print all list data using slicing imp for interview


data = [1,"test,4.5",None, 1]
print(data) 
print(data[1])
print(isinstance(data[1], str)) #check string , more valid

#print(type(data[1]==str)) 
#print(type(data[1])==str)

data = [1,"test,4.5",None, 1]
data[0]="this is updated on" # change data of that index
#data[5]="err"
print(data)
print(type (data))

#adding method on list

#append--> add only one at a time
data = ["hello", "test", 1,2,3,4,"broadway"]
data.append(1.6) # add at last
data.append("added")
print (data)

#extend--> just add two index
data = ["hello", "test", 1,2,3,4,"broadway"]
data1=[2,2,2,3]
data1.extend(data)
data.extend(data1)
print(data)
print (data1)

#insert --. add in perticular index
data = ["hello", "test", 1,2,3,4,"broadway"]
data.insert(1,"hari")
print(data)


#concat--> add two index and make new list
data = ["hello", "test", 1,2,3,4,"broadway"]
data1=[2,2,2,3]
data2= data+data1
print(data2)
print(data1)
print(data)

