import mymodule
mymodule.func("Jonathan")

import mymodule
a=mymodule.person["age"]
print(a)

import mymodule as mx
a=mx.person["name"]
print(a)

#Built-in modules

import platform
x=platform.system()
print(x)

import platform
x=dir(platform)
print(x)

from mymodule import person
print(person["age"])

from mymodule import car
print(car["model"])
