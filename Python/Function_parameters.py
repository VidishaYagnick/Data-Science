# Note: DEFAULT ARGUMENTS FOLLOWS NON DEFAULT ARGUMENTS

def average(a  , b = 2):
    print((a+b)/2)

average(6)
# a is required parameter, b is default parameter (can or cannot give the value)

average(b=4,a =2)
# a and b are now keyword parameters (sequence doesn't matter)

#variable length parameters

def avg(*numbers): #take tuple as input
    print(type(numbers))
    sum = 0
    for num in numbers:
        sum = sum + num
    print("Average is ",sum/len(numbers))

avg(2,4,6,8,10)

def name(**name): #take input as dictionary
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")