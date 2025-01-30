with open("python.txt","r") as f:
   c=f.read()

if("python" in c):
    print("python is present")

else:
    print("it is absent")