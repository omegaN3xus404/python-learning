class complex:
    
    def __init__(self,r,i):
       self.r=r
       self.i=i

    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
    

c1=complex(1,2)
c2=complex(2,3)

print(c1+c2)




