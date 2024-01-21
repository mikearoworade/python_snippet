# A lambda function is a small anonymous function.
# Syntax - lambda argument: expression
x = lambda a: a + 10
print(x(5))

# Two argument
x = lambda a, b: a * b
print(x(5, 6))

# Three argument
x = lambda a, b, c: a + b + c
print(x(24, 27, 29))


# lambda as an anonymous function in another function
def myfunc(n):
    return lambda d: d*n


myDoubler = myfunc(2)
print(myDoubler(11))
