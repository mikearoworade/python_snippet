# Python is an object-oriented programming language
# Almost everything in python is an object, with properties and methods.
# A class is like an object constructor, or a "blueprint" for creating object
# Create a class using "class" keyword
class DemoClass:
    pass  # class definition can not be empty. Hence, pass is used for where there's no content.


class Employee:
    job = "Software Engineer"


# Create an object
emp1 = Employee()
print(emp1.job)


# The __init__() function
# All classes have a function called __init__(), which is always executed when the class is initiated
# Use the __init__() function to assign values to object properties.
# The self parameter is a reference to the current instance of the class, and is used to
# access variables that belong to the class.
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


p = Person("Michael", "Aroworade", "27")
print(p.firstname, p.lastname, p.age)
print(p)  # without __str__
print()


# __str__() function controls what should be returned when the class object is represented as a string
class Person1:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"My name is {self.firstname} {self.lastname}. I'm {self.age} old."


p1 = Person1("Michael", "Aroworade", 27)
print(p1)
print()


# Object can also contain methods. methods in objects are functions that belong to the object
class Person2:
    def __init__(self, firstname, lastname, age, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job

    def __str__(self):
        return f"My name is {self.firstname} {self.lastname}. I'm {self.age} old."

    def skill(self):
        print("I'm a " + self.job)


p2 = Person2("Michael", "Aroworade", 27, "Software Engineer")
print(p2)
p2.skill()
print()
