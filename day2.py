a = " test"
a = "100"
print (type(a))
a = 10
print (type(a))

a =1.5
print (type(a))

a= False
print (type(a))

print(isinstance(12,str)) #type validation 
type(a)=str # there is go gurantee it will always true... because all have diff object

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


