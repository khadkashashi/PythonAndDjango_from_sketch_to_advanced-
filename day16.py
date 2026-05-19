#inheritance
class Parent():
    a=10
    b=20
class Child(Parent):
    a="from b"
    c=1000
    d="hari"
obj =Child()
print(obj.a)
#from b


class Parent():
    a = 10
    b = 20

    def add(self):
        return self.a + self.b


class Child(Parent):
    a = 50


obj = Child()

print(obj.a)
print(obj.add()) 
#from b
#50
#70
# always gives the priority to the child object


class Parent():
    a=10
    b=11
    def __init__(self):
        print("i am frim parent class")
    def add (self):
        return self.a +self.b
    
class Child(Parent):
    def __init__(self):
        print("i am from child class")
        #parent.__init__(self)
        super().__init__()
        #print("this is from parent class",super().b)
    
a=2
c=1000
d="hari"
obj =Child()
print(obj.a)



print("------------------------------")

#multilevel

class Parent():
    a=10
    b=11
    def __init__(self):
        print("i am from parent class")
    def add (self):
        return self.a +self.b
    
class Child(Parent):
    def __init__(self):
        print("i am from child class")
        #parent.__init__(self)
        super().__init__()
        self.aa=super().a
        #print("this is from parent class",super().b)
    
a=2
c=1000
d="hari"


class Child1(Child):
    d=2
    a=200
    def value_a(self):
        return super().a, self.aa,self.a

obj =Child1()
print(obj.a)

#i am from child class
#i am from parent class
#200
print(obj.value_a())
#(10, 10, 200)


##multipal
class Parent2():
    c = 100
    d = 50

    def parent_method(self):
        return "from parent2 class"

class Parent1():
    a = 20
    b = 30

    def parent_method(self):
        return "from parent1 class"

class Child(Parent2,Parent1):
    e = 1
    f = 2
    def parent_method(self):
        return f'{super().parent_method()}, {Parent1.parent_method(self)}'

print(Child.__mro__) #mro check order

obj = Child()
print(obj.a)
print(obj.parent_method())

#20
#from parent2 class, from parent1 class



class Person():
    name='Shashi'
    age=22
    def displayPerson(self):
        return f'{self.name},{self.age}'
class Worker():
    company='aura'
    salaray=90000
    def displayworker(self):
        return f'{self.company},{self.salaray}'
class Engineer(Person,Worker):
    def displayengineer(self):
        return f'{self.displayPerson()}, {self.displayworker()}'

print(Engineer.__mro__)
obj= Engineer()
print(obj.displayengineer())
#Shashi,22, aura,90000
#


#use constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayPerson(self):
        return f'{self.name}, {self.age}'


class Worker:
    def __init__(self, company, salary):
        self.company = company
        self.salary = salary

    def displayworker(self):
        return f'{self.company}, {self.salary}'


class Engineer(Person, Worker):
    def __init__(self, name, age, company, salary):
        Person.__init__(self, name, age)
        Worker.__init__(self, company, salary)

    def displayengineer(self):
        return f'{self.displayPerson()}, {self.displayworker()}'


print(Engineer.__mro__)

obj = Engineer('shashi', 22, 'aura', 90000)
print(obj.displayengineer())
#shashi, 22, aura, 90000