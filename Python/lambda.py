square = lambda x : x*x
print(square(12))

cube = lambda x : x**3
print(cube(3))

avg = lambda x,y,z : (x+y+z)/3
print(avg(6,4,8))

# used when we need to pass function as argument : 
def example(fx , value):
    return 6 + fx(value)

#Method 1
print(example(cube,3))

#Method 2
print(example(lambda x : x**3, 3))

