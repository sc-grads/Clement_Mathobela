# Global variable, initialize it with whatever value you want
x = 2

def increment():
    global x
    x += 1
    pass



## Call the function

increment()

## Print x


print(x)