class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name of the employee {self.id} is {self.name}")

e1 = Employee("Vidi",12)
e2 = Employee("Shree",13)
e1.showDetails()
e2.showDetails()

class Programmer(Employee):
    def Lang(self):
        print("Default language is Python")

e3 = Programmer("Shruti",14)
e3.showDetails()
e3.Lang()