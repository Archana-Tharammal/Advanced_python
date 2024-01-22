"""import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

#creating date objects
import datetime

x=datetime.datetime(2020,12,25)
print(x)

#Today's date only
x = datetime.date.today()
print(x)

#strftime() method


import datetime

#weekday
x= datetime.datetime(2022,5,11)
print(x.strftime("%A"))
print(x.strftime("%a"))

#weekday as a number 0-6
x=datetime.datetime.now()
print(x.strftime("%w"))

#day of month
x=datetime.datetime.now()
print(x.strftime("%d"))

#month name
x= datetime.datetime(2022,1,11)
print(x.strftime("%B"))
print(x.strftime("%b"))

#month as a number
x= datetime.datetime(2023,3,15)
print(x.strftime("%m"))

#year
x= datetime.datetime(2023,10,5)
print(x.strftime("%y"))
x= datetime.datetime.now()
print(x.strftime("%Y"))

#Hour 00-23
x= datetime.datetime.now()
print(x.strftime("%H"))

#Hour 00-23
x= datetime.datetime.now()
print(x.strftime("%I"))

#AM/PM
x= datetime.datetime.now()
print(x.strftime("%p"))

#Minute 00-59
x= datetime.datetime.now()
print(x.strftime("%M"))

#Second 00-59
x= datetime.datetime.now()
print(x.strftime("%S"))

#Microsecond 000000-999999
x= datetime.datetime.now()
print(x.strftime("%f"))

#UTC offset
x= datetime.datetime.now()
print(x.strftime("%z"))

#Timezone
x= datetime.datetime.now()
print(x.strftime("%Z"))

#Day number of year 001-366
x= datetime.datetime.now()
print(x.strftime("%j"))

#Week number of year, Sun as 1st day
x= datetime.datetime.now()
print(x.strftime("%U"))

#Week number of year,Mon as 1st day
x= datetime.datetime.now()
print(x.strftime("%W"))

#Local version of date and time
x= datetime.datetime.now()
print(x.strftime("%c"))

#Century
x= datetime.datetime.now()
print(x.strftime("%C"))

#Local version of date
x= datetime.datetime.now()
print(x.strftime("%x"))

#Local version of time
x= datetime.datetime.now()
print(x.strftime("%X"))

#A % character
x= datetime.datetime.now()
print(x.strftime("%%"))

#ISO 8601 year
x= datetime.datetime.now()
print(x.strftime("%G"))

#ISO 8601 weekday (1-7)
x= datetime.datetime.now()
print(x.strftime("%u"))

#ISO 8601 weeknumber (01-53)
x= datetime.datetime.now()
print(x.strftime("%V"))"""


#Find the current date and time
import datetime
x=datetime.datetime.now()
print(x)

#Get the current year
print(x.year)

#month of the year
print(x.strftime("%B"))

#day of the month
print(x.strftime("%d"))

#day of the week
print(x.strftime("%A"))