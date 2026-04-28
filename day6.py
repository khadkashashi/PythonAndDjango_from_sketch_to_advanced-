#Deleting items/elements from existing list
# The del used to delet element of the list via index
a=[1,2,3,4,5]
del a[0]
print(a)

#a=[1,2,3,4,5]
#del a # delete entire index data
#print(a)


# The remove() method remove the element/item with the specified value(itemname).
a=[1,2,3,4,5,1,1]
a.remove(2)
print(a)

# The pop() method deletes the element/item from last of the list by default.
a=[1,2,3,4,5,1,1]
result=a.pop(0)
last_data=a.pop()
a.pop()# remove last data
print(a)
print(result)

# The clear() method remove all the elements from the list.
a=[1,2,3,4,5,1,1]
a.clear()
print(a)




#count()
#The count() method returns the number of elements/item with the specified value(itemname).
a=[1,23,13,1,2,67,51]
a.sort() #for interviwe, 
print(a)



#reverse()
## The reverse() method reverses the order of the elements of the list.

a=[1,23,13,1,2,67,51]
a.sort(reverse=True)
print(a)

a=[1,23,13,1,2,67,51]
a.reverse()
print(a)



#sort()
# The sort() method sorts the list ascending by default
a=[1,23,13,1,2,67,51]
print(a.count(2))


#nested list
a=[1,2,3,4,[6,7,8]]
print(len(a))
#last_data=a[4]
#print(last_data[1])
#print(type(last_data))
print(a[4][1])


numbers =[int(input("enter 1st number:")),
           int(input("enter 2nd number:")),
           int(input('enter 3rd number:')),
           int(input("enter 4th number:")),
           int(input("enter 5th number:"))
]
print("list is:",numbers)
ave=0
ave=sum(numbers)/len(numbers)
print("total average=", ave)


#n=[]
#for i in range(5):
 #   num= int(input("enter 5 number:"))
  #  n.append(num)
#print("list order:",n)
    
# take 5 input from user and put it on list and find average of them.
a=int(input("enter the number,a"))
b=int(input("enter the number,b"))
c=int(input("enter the number,c"))
d=int(input("enter the number,d"))
e=int(input("enter the number,e"))
result=[]
result.append(a)
result.append(b)
result.append(c)
result.append(d)
result.append(e)

print(result)
avg=(result[0]+result[1]/len(result))
print(avg)