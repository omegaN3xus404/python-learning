def factriol(n):
    if(n==0 or n==1):
        return 1
    return n * factriol(n-1)

n=int(input("enter a number you want the factriol of you want:"))
print(f"{factriol(n)}")

