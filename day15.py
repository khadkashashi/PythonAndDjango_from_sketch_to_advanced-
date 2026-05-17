#oop-----> Object-Oriented Programming (OOP) is a way of organizing and structuring code using objects and classes.
#helping make programs modular, reusable, and scalable.

#class ---> A class in Python is a blueprint for creating objects.
#Class → Design/Template
#Object → Real thing created from that design
#syntax : class Student:
   # pass
#class → keyword used to create class
#Student → class name
#pass → means “nothing inside yet”


#object---> An object is a real instance created from a class.
#Example:
#Class = Car
#Objects = BMW, Tesla, Toyota

class Car():
    wheel=4
    color='green'
    brand='BMW'
    def infro(self):
        return f'car brand name is {self.brand}'
    
    def car_info2(self):
        info =self.car_info2()
        return f'wheel{self.wheel} {info}'
obj =Car()
print(obj.wheel)
print(obj.car_info2)
obj.c =100 # obj attrs
print(obj.c)