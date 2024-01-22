"""f=open("demo.txt")
print(f.read(6))
print(f.readline())
f=open("demo.txt")
for x in f:
    print(x)
f.close()
"""

f=open("demo.txt","a")
f.write("Now the file has more content!")
f.close()
f=open("demo.txt","r")
print(f.read())

f=open("demo.txt","w")
f.write("Woops! I have deleted the content!")
f.close()
f=open("demo.txt","r")
print(f.read())



import os
if os.path.exists("demofile.txt"):
    print("The file  exist")
else:
    print("The file does not exist")

import os
if os.path.exists("file2.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")