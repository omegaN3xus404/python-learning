with open("identical.txt","r")as f:
    c=f.read()


with open("identical2.txt","r")as f:
    v=f.read()


if(c==v):
    print("they are indntical")

else:
    print("they are not idemtical")
    