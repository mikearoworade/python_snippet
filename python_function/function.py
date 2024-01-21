# A function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Creating a function

def intro():
    """Ordinary function without argument to print to screen"""
    print("My name is Michael Aroworade.")


def greet(name):
    """Function with argument to print to screen"""
    print("Smart and fine {}.".format(name))


def bio(age, job):
    """Function with more than one argument"""
    print("I'm {} years old, i'm a {}.".format(age, job))


def languages(*args):
    """Arbitrary argument. Unknown number of arguments"""
    print("I have {} proficiencies. They are ".format(len(args)), args)


def data(**kwargs):
    """Arbitrary keyword arguments."""
    for key, value in kwargs.items():
        print(key, value)
    print()


def birthday(dob):
    """Passing list through function"""
    for i in dob:
        print(i)
    print()


def xyears(y):
    return 27 + y


intro()
greet("Michael")
bio(27, "Software Engineer")
languages("Python", "C", "SQL", "Javascript", "PHP")
data(firstname="Michael", lastname="Aroworade")
birthday([26, 3, 1996])
print("I will be {}, in {} years time.".format(xyears(5), 5))
