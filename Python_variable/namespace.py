# x is in the global namespace
x = 26
print("Global scope variable: ", x)


def mainFunc():
    # y is in the local namespace
    y = 3
    print("Inside mainFunc: global scope x = {} and function variable = {}".format(x, y))

    def inner_func():
        # z is in the nested local namespace
        z = 1996
        print("Inside inner function: global scope x = {}, main function variable = {} and function variable = {}"
              .format(x, y, z))

    inner_func()


mainFunc()
