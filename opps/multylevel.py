class name:
    a=2

class sec(name):
    b=3

class roll(sec):
    c=5

o=name()
print(o.a)
o=roll()
print(o.a,o.b,o.c)