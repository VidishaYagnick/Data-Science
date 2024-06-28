x = [1,2,3]
print(dir(x))

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

P = Person("Vidisha",21)
print(P.__dict__)
print(help(Person))