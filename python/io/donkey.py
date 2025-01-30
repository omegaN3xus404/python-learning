a="donkey"
b="######"

with open("donkey.txt","r") as f:
    conten=f.read()

c=conten.replace(a,b)

with open("donkey.txt","w") as f:
    f.write(c)
    
    