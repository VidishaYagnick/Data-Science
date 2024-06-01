x = int(input("Enter a number : "))
# x is the variable to match
match x:
    
    # if x is 0
    case 0:
        print("x is zero")
    
    # case with if-condition
    case 4 if x%2 == 0:
        print("x % 2 == 0 and case is 4")
    
    # default  
    case _ if x < 10:
        print(x, "is less than 10")