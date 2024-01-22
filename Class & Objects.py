class myClass:
    x = 6
print(myClass)


class MyClass:
    x = 10
p1 = MyClass()
print(p1.x)


#The __init__() function
class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age
p1=person("John",29)
print(p1.name)
print(p1.age)

#The __str__() function
class Person:
    def __init__(self,names,ages):
        self.name=names
        self.age=ages

    def __str__(self):
        return f"{self.name}, {self.age}"
p1= Person("John",30)
print(p1)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("My name is "+ self.name)
        print("My age is ",self.age)
p1= Person("John",20)

p1.age=40

p1.myfunc()


#_Class_and_objects_question_1
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello "+self.name)

p1= Person("John",20)
p1.myfunc()

#_Class_and_objects_question_2
class Car:
    def __init__(self,colour,model,year):
        self.colour=colour
        self.model=model
        self.year=year
    def myfunc(self):
        print("Colour of the car is ",self.colour)
        print("Car model is ", self.model)
        print("The year of launch is ", self.year)

p1= Car("Jet Black","Mercedes",2020)
p1.myfunc()

#_Class_and_objects_question_3
class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def myfunc(self):
        print("The title of the book is ", self.title)
        print("The author is ", self.author)
        print("The year of publish is ", self.year)

p1=Book("Harry Potter and the Deathly Hallows","J.K Rowling",2007)
p1.myfunc()


#_Class_and_objects_question_4
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        pi=3.14
        return pi*self.radius*self.radius

p1= Circle(10)
print(p1.area())

#_Class_and_objects_question_5
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length* self.breadth
p1= Rectangle(20,30)
print(p1.area())

#_Class_and_objects_question_6
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def printname(self):
        print("Name: ",self.name,", Grade:" ,self.grades)
        self.grades = "A+"

x=Student("Mike","A")
x.printname()
print(x.grades)

#_Class_and_objects_question_7
class Employee:
    def __init__(self,name ,salary):
        self.name=name
        self.salary=salary


    def printname(self):
        new_salary=60000
        print(self.name,self.salary)
        print((new_salary - self.salary) /(self.salary * 100))


x=Employee("Mike",50000)
x.printname()