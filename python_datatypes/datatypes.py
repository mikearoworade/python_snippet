"""
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType
"""
# str
name = "Michael Aroworade"
print(name)
print(type(name))  # str

# int
age = 27
print(age)
print(type(age))  # int

# float
height = 5.8
print(height)
print(type(height))  # float

# complex
x = 1j
print(x)
print(type(x))  # complex

# list
family = ["Sunday", "Oluwakemi", "Samuel", "Adeniyi"]
print(family)
print(type(family))  # list

# tuple
parent = ("Sunday", "Oluwakemi")
print(parent)
print(type(parent))  # tuple

# set
brothers = {"Samuel", "Adeniyi"}
print(brothers)
print(type(brothers))  # set

# dict
fullname = {"firstname": "Michael", "lastname": "Aroworade"}
print(fullname)
print(type(fullname))  # dict

# range
y = range(10)
print(y)
print(type(y))  # range

# bool
z = True
print(z)
print(type(z))  # bool

# frozenset
food = frozenset({"rice", "bread", "yam"})
print(food)
print(type(food))  # frozenset

# bytes
a = b"Michael"
print(a)
print(type(a))  # bytes

# bytearray
b = bytearray(5)
print(b)
print(type(b))  # bytearray

# memoryview
c = memoryview(bytes(5))  # memoryview
print(c)
print(type(c))

# NoneType
d = None
print(d)
print(type(d))  # NoneType
