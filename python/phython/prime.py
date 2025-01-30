a=int(input("enter the number"))
for i in range (1,a):
    if(a%i)==0:
        print("it is prime number")
        break

else:
    print("it is not prime number")