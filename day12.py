#diff between list and dict



#tuple----> A tuple is an ordered, immutable (unchangeable) collection of items in Python.
#Defined using ( ) parentheses.
#Items can be of different data types.
# example---> ('hii',"hello",1, 2,"apple",True)
#tuple is used when data must not change

#2. Tuple Properties
#Ordered → Items have fixed positions.
#Immutable → Cannot modify after creation.
#Allow duplicates → Same values can appear multiple times.
#Heterogeneous → Can store different data types.

a=(1,2,3,4,5)
b=(1,2,3,4,5)
print(type(a))
print(len(a))

#. Accessing Tuple Items
#indexing
s1=(10,"apple",1,True)
print(s1[0])
print(s1[-2])

#slicing
s2=(1,2,3,"hello","ball",2)
print(s2[1:4]) 
for i in b:
    print(i)


# Tuple vs List
#Feature	 Tuple	        List
#Mutability	 Immutable  	Mutable
#Syntax	     (1, 2, 3)  	[1, 2, 3]
#Performance  Faster	    Slower
#Use Case	 Fixed data	    Dynamic data



#Converting Between List and Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# Tuple Unpacking
t = (10, 20, 30)
a, b, c = t
print(a, b, c)   # 10 20 30

# Nested Tuples
tup = (1, (2, 3), (4, 5))

#Useful Tuple Methods
#count() 
(1, 2, 2, 3).count(2)  # 2

#index()
(10, 20, 30).index(20)  # 1










#set--------> A set in Python is an unordered collection of unique items.
#A set is defined using curly braces {} or the set() function.
#Unordered → elements do not have a fixed position
#No duplicates → repeated values are automatically removed
#Mutable → you can add or remove items
#Iterable → you can loop through elements
#Unindexed → Cannot access items using an index.

#used when: When you need to remove duplicates.
#When performing mathematical set operations.
#When fast membership checking is needed.

a={'hari','hello',1,2}
print(a)

#Using set() Constructor
a=[1,2,3,4,1,1,3,34]
b=set(a)
print(b)
#{1, 2, 3, 4, 34}

#Adding Items to a Set
#1.add()
s={'apple','cat',1,2}
s.add(3)
print(s)
#{1, 2, 3, 'cat', 'apple'}--> output
#2.update()---> add multiple items
a={"shashi","khadka",22,'nepal'}
a.update(['rampur', 'palpa'])
print (a)
#{'shashi', 'nepal', 'palpa', 'khadka', 'rampur', 22}

#Removing Items
#remove()--->Raises error if item not found
a={1,2,3,1,3,5,7}
a.remove(1)
print(a)
#{2, 3, 5, 7}

#discard()--> No error if item not found
s = {1, 2, 3}
s.discard(5)  
print(s)
#{1, 2, 3}
# No error


#pop() – Removes a random item
s = {10, 20, 30}
s.pop() 
print(s)
 # Random item removed

#clear() – Removes all items
s.clear()


#Set Operations
#Union (A ∪ B)
A = {1, 2, 3}
B = {3, 4, 5}
A | B  
# {1, 2, 3, 4, 5}

#Intersection (A ∩ B)
A & B  
# {3}

#Difference (A − B)
A - B  
# {1, 2}
B - A  
# {4, 5}

#Symmetric Difference
A ^ B 
 # {1, 2, 4, 5}


#Checking Membership
s = {"a", "b", "c"}
"a" in s  
 # True
"d" not in s 
  # True


#Frozenset--->A frozenset is an immutable version of a set.
#Cannot add or remove items.
#Useful as dictionary keys or set elements.
fs = frozenset([1, 2, 3])
