class secondvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"the i is {self.i} and  j is {self.j}")

class threevector(secondvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"the i is {self.i} and  j is {self.j} and k is {self.j}")

o=secondvector(1,2)
o2=threevector(1,2,3)

o.show()
o2.show()



