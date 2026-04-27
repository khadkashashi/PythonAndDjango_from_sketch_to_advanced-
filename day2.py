a = " test"
a = "100"
print (type(a))
a = 10
print (type(a))

a =1.5
print (type(a))

a= False
print (type(a))

print(isinstance(12,str)) #type validation ,validate about data type
type(a)=str # there is go gurantee it will always true because all have diff object

#typee casting

a = "100"
print("before casting", type(a))
b =int(a)
print("after clasting",type(b),b)

a="200"
print("before casting", type(a))
b = float(a)
print("after clasting",type(b),b)

a="0"
print("before casting", type(a),a)
b = bool(a)
print("after clasting",type(b),b)
# imp for interview diff between type casting and type validation,
#Difference Between Type Casting and Type Validation in Python
#Type Casting	                            Type Validation
#Converting one data type into another	     Checking whether data is of the correct type
#Used to change the type of a value          Used to verify input before processing
#Example: string "10" → integer 10	           Example: checking if age is an integer
#Functions used: int(), float(), str(), list()	Functions used: type(), isinstance()