class employe:
    compny="itc"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


# class programer:
#         compny="itc"
#         def show(self):
#             print(f"the name is {self.name} and the salatry is {self.salary}")

#         def showlanguage(self):
#             print(f"the name is {self.name} and he is a good language of {self.language}")

class programer(employe):
    def show(self):
     print(f"the name is {self.name} and the salatry is {self.salary}")

    def showlanguage(self):
             print(f"the name is {self.name} and he is a good language of {self.language}")



a=employe()
b=programer()

print(a.compny,b.compny)    