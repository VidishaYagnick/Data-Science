class Emp:
    def __init__(self):
        self.__name = "Vidisha" 
        self.__name = "Vidisha" #Private
        self._occ = "Designer"  #protected   

A = Emp()
print(A._Emp__name) # Mangling
print(A._occ)