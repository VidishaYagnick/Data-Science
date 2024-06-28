num = int(input("Enter a number between 5 and 9 : "))

if(num < 5 or num > 9):
    raise ValueError("Value must be between 5 and 9 ")