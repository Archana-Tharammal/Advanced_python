#RegEx functions
# findall() function
import re
txt="It is raining in Spain"
x=re.findall("ai",txt)
print(x)

x=re.findall("Portugal",txt)
if(x):
    print("Yes,there is at least one match!")
else:
    print("No match")

# search() function
import re
txt="It is raining in India"
x=re.search("\s",txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#split() function
txt="It is raining in India"
x=re.split("\s",txt)
print(x)

x=re.split("\s",txt,3)
print(x)

#sub() function
x=re.sub("\s"," * ",txt)
print(x)

x=re.sub("\s"," * ",txt,2)
print(x)

#match object
txt = "It is raining in Spain"
x = re.search("ai", txt)
print(x)
print(x.span())
print(x.string)
print(x.group())



# Metacharacters
import re

txt = "It is raining in India"
x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)

txt = "hello planet"
x = re.findall("he..o", txt)
print(x)

x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

y= re.findall("planet$", txt)
print(x)

if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")

x = re.findall("he.*o", txt)
print(x)

x = re.findall("he.+o", txt)
print(x)

x = re.findall("he.?o", txt)
print(x)

x = re.findall("he.{2}o", txt)
print(x)

txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#Special sequences
import re
txt = "The rain in Spain"

#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")

#Check if "ain" is present at the beginning of a WORD:
x=re.findall(r"\bain",txt)
print(x)
if x:
  print("yes,there is atleast one match!")
else:
  print("No match")

x=re.findall(r"ain",txt)
print(x)
if x:
  print("yes,there is atleast one match!")
else:
  print("No match")

#Check if "ain" is present, but NOT at the beginning of a word:

txt=" I live in India"
x = re.findall(r"\Bdia", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain\B", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#Return a match at every no-digit character:
x=re.findall("\D",txt)
print(x)
if x:
  print("Yes,there is at least one match")
else:
  print("No match")

#Return a match at every white-space character:

x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
# Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
txt="Is there rain in Spain?"
x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string ends with "Spain":
txt=" I live in India"
x = re.findall("India\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

# Sets
import re

txt = "I live in India"
# Check if the string has any a, i, or n characters:

x = re.findall("[ain]", txt)

print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# Check if the string has any characters between a and n:

txt = "It is raining in Spain"
x = re.findall("[a-n]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# Check if the string has any 0, 1, 2, or 3 digits:
txt = "The Worldcup 2023 is held in India"
x = re.findall("[0123]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#Check if the string has any digits:
txt="10 times before 4:21 AM"
x=re.findall("[0-9]",txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any two-digit numbers, from 00 to 59:
txt="5 times before 12:15 AM"
x=re.findall("[0-5][0-9]",txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any characters from a to z lower case, and A to Z upper case:
txt="2 times before 7:45 PM"
x=re.findall("[a-zA-Z]",txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any + characters:
txt = "By addition,2+5=7"
x = re.findall("[+]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
