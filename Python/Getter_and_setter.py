class GS:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}")

    @property
    def Ten_value(self):
        return 10 * self.value
    
    @Ten_value.setter
    def Ten_value(self, new_val):
        self.value = new_val / 10
        

A = GS(12)
A.show()
print(A.Ten_value)
A.Ten_value = 100
A.show()
