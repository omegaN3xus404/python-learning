def sum(a):
    if a==0 or a==1:
        return 1
    return a + sum(a-1)
  
a=int(input("enter the number:"))
b=sum(a)
print(b)

