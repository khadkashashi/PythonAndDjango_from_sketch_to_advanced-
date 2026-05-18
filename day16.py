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