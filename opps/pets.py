class animal:
    pass

class pets(animal):
    pass


class dog(pets):
    @staticmethod
    def bark(a,b):
        print("bow bow")


d=dog()
d.bark(1,2)
