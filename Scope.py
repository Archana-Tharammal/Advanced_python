# Local scope
def myfunc():
    y = 20
    print(y)


myfunc()


# Function inside function
def MyFunc():
    x = 250

    def innerfunc():
        print(x)

    innerfunc()


MyFunc()

# Global scope
x = 300


def Myfunc():
    print(x)


Myfunc()
print(x)

a = 500


def my_func():
    a = 545
    print(a)


my_func()
print(a)


# global keyword
def my_funcs():
    global x
    x = 456


my_funcs()
print(x)

x = 45


def func():
    global x
    x = 100


func()
print(x)
