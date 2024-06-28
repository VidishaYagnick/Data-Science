class Employee:
  def __init__(self, name, salary):
    self.name = name 
    self.salary = salary
    
  @classmethod  #Alternative Constructor
  def fromStr(cls, string):
    return cls(string.split("-")[0], int(string.split("-")[1]))
    
e1 = Employee("Vidisha", 70000)
print(e1.name)
print(e1.salary)

string = "Shree-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
