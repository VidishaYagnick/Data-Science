class Person:
    name = "Vidisha"
    occupation = "Python Developer"
    net_worth = 10000

    def info(self):
        print(f"Name is {self.name} and occupation is {self.occupation}")

A = Person()
B = Person()
B.name = "Shreeyam"
B.occupation = "Designer"

A.info()
B.info()