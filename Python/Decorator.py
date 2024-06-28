def greet(fx):
    def mfx(*args, **kwargs):
        print("Welcome!!!")
        fx(*args,**kwargs)
        print("Thanks for using this function...")
    return mfx

@greet
def Hello():
    print("Hello world")

def add(a,b):
    print(a+b)

Hello()
greet(add)(1,2)

# Method 2 : shortcut
# greet(Hello)()