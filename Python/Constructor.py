class Person:
    def __init__(self,name,occ):
        self.name = name 
        self.occ = occ
    
    def info(self):
        print(f"Name is {self.name} and ocuupation is {self.occ}")

A = Person("Vidisha","Python Developer")
B = Person("Shreeyam","Designer")
A.info()
B.info()