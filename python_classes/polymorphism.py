# Polymorphism is often used in class method, where we can have multiple classes
# with the same method
class Software:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def skill(self):
        print(self.firstname, "is a Software Engineer.")


class Network:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def skill(self):
        print(self.firstname, "is a Network Engineer.")


class Electrical:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def skill(self):
        print(self.firstname, "is an Electrical Engineer.")


p1 = Software("Michael", "Aroworade")
p2 = Electrical("Ayodele", "Aroworade")
p3 = Network("Oluwaseun", "Aroworade")

for p in (p1, p2, p3):
    p.skill()
