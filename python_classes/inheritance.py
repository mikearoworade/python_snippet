# Inheritance allows us to define a class that inherits all the methods and
# properties from another class
# Parent class is the class being inherited from, aka base class
# Child class is the class that inherits from another class aka derived class
# Parent class "Person"
class Person:
    def __init__(self, firstname, lastname, age, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job

    def __str__(self):
        return f"My name is {self.firstname} {self.lastname}. I'm {self.age} old."

    def skill(self):
        print("I'm a " + self.job)


p = Person("Michael", "Aroworade", 27, "Software Engineer")
print(p)
p.skill()
print()
print()


# Child Class
class Employee(Person):
    def __init__(self, firstname, lastname, age, job, department, linemanager, ):
        super().__init__(firstname, lastname, age, job)
        self.department = department
        self.linemanager = linemanager

    def welcome(self):
        print("I work at JubailiBros Engineering. My department is", self.department,
              "and my line manager is", self.linemanager)


emp = Employee("Michael", "Aroworade", 27, "Software Engineer", "Info Tech", "Abdelmaleeq")
print(emp)
emp.skill()
emp.welcome()
