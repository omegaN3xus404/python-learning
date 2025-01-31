class employe:
    company="itc"
    name ="defult name"
    def show(self):
        print(f"the name is {self.name} and yje compny is {self.company}")


class coder:
    language="python"
    def printlanguage(self):
        print(f"the name is {self.name} and the language is {self.language}")


# this inputs the both value of 1 and second
class progranm(employe,coder):
    def showlanguage(self):
        print(f"the name is {self.name} and the language is {self.language} and the comapny is {self.company}")


a=progranm()
a.showlanguage()
    
