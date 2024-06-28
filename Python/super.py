class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

    def Example(self):
      print("PARENT")

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__( name, id)
        self.lang = lang

    def Example(self):
        print("CHILD")
        super().Example()

rohan = Employee("Soumya Maity", "425")
vidisha = Programmer("Vidisha", "2345", "Python")
print(vidisha.name)
print(vidisha.id)
print(vidisha.lang)

#vidisha.Example()

