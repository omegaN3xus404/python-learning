class empolye:
    salary=100000
    increment=50
    @property
    def hi(self):
        return (self.salary + self.salary*(self.increment/100))
    

c=empolye()
print(c.hi)   
        
        

        