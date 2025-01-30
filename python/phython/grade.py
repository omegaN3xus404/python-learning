a=int(input("enter the marks in nepali"))
b=int(input("enter the marks in math"))
c=int(input("enter the marks in  english"))
sum=a+b+c
per=(sum/300)*100
if(per>90 or per>=100):
    print("you got A+")

elif(per>80 or per>=90):
    print("you got A")

    
elif(per>70 or per>=80):
    print("you got B+")

    
elif(per>60 or per>=70):
    print("you got B")

    
else:
    print("you got fail")

