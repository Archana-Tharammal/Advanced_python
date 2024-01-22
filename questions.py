#check if a number is +ve or -ve or 0 using if...elif...else
import math

a = int(input("enter the no: "))
if a>0:
    print(a," is positive")
elif a<0:
    print(a, " is negative")
else:
    print("It is zero")

#odd or even numbers
print("even numbers: ")
for i in range(1,27):

    if i%2==0:
            print(i,end=" ")

print()
print("odd numbers:")
for j in range(1,27):
    if j%2!=0:
        print(j,end=" ")


print()

#multipilcation table from 1 to 10 of a number

num=5
print("multiplication table of ",num)
for i in range(1,11):
    x=num*i
    print(num,"*",i,"=",x)

#sum of natural numbers upto num

num=5
sum=0
for i in range(1,num+1):
    sum=sum+i
print("sum of ",num,"numbers: ",sum)

#find the largest among three numbers
a=10
b=25
c=30
if a>b and a>c:
    print(a," is the largest number")
elif b>a and b>c:
    print(b, " is the largest number")
else:
    print(c, " is the largest number")

#find the square root of the number

import math
a=25
x=math.sqrt(a)
print(x)

