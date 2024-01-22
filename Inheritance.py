#create a child class
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class student(Person):
    pass

x= student("John","Mathew")
x.printname()

# add the __init__() function
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x=student("Mike","Olsen")
x.printname()

#single inheritance
class Parent:
    def func(self):
        print("hai")

class Child(Parent):
    def func2(self):
        print("hello")

obj=Child()
obj.func()


#multiple inheritance
class Parent:
    def func(self):
        print("Welcome")

class Student:
    def func1(self):
        print("hai")

class Child(Parent,Student):
    def func2(self):
        print("hello")


obj=Child()
obj.func1()

#multilevel inheritance
class Parent:
    def func(self):
        print("Welcome")

class Student(Parent):
    def func1(self):
        print("hai")

class Child(Student):
    def func2(self):
        print("hello")

obj=Child()
obj.func1()

class Parent:
    def func(self):
        print("Welcome")

class Student:
    def func1(self):
        print("hai")

class Child(Parent,Student):
    def func2(self):
        print("hello")

obj=Child()
obj.func()
obj.func1()
obj.func2()



#overriding
class Parents:
    def func(self):
        print("hello world")
class Student:
    def func(self):
        print("Hai")

class Child(Parents,Student):
    def func(self):
        print("Welcome")

obj= Child()
obj.func()

#super() Function
class Parents:
    def func(self):
        print("hello world")
class Student:
    def func1(self):
        print("Hai")

class Child(Parents,Student):
    def func(self):
        print("Welcome")
        super().func1()

obj= Child()
obj.func()

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname, lname)

x=Student("Mike","Olsen")
x.printname()

#Add properties
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationyear =2019
    def Welcome(self):
        print("Welcome", self.firstname, self.lastname," to the class of ",self.graduationyear)

p1= Student("Mike","Olsen")
p1.printname()
print(p1.graduationyear)
p1.Welcome()


