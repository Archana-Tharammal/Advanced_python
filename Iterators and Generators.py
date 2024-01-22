#Iteration
"""mytuple=("Apple","Orange","Banana")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr="Cherry"
myits=iter(mystr)
print(next(myits))
print(next(myits))
print(next(myits))
print(next(myits))
print(next(myits))
print(next(myits))

class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x

myclass =MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#StopIteration
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myclass=MyNumbers()
myiter= iter(myclass)

for x in myiter:
    print(x)"""

 #Generators
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
for value in simpleGeneratorFun():
    print(value)

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
x=simpleGeneratorFun()
print(next(x))
print(next(x))
print(next(x))


exp=(i*5 for i in range(5) if i%2==0)

for i in exp:
    print(i)


















