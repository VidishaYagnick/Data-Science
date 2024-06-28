x = 4 #global variable
def hello():
    x = 10 #local variable
    print(f"Local x is {x}")

hello()
print(f"Global x is {x}")

# global keyword : 
x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function