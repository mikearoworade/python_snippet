# tuples are used to store multiple items in a single variable.
# tuple is a collection which is ordered and unchangeable.

names = ("Michael", "Ayodele", "Aroworade")
print(names)
print()

# tuple items are ordered, unchangeable, and allow duplicates values.
# tuple items are indexed, the first item has index [0], second [1], etc.
names = ("Michael", "Aroworade", "Ayodele", "Aroworade")
print(names)
print()

# tuple length
print(len(names))
print()

# A tuple
name = ("Michael",)
print(type(name))

# NOT a tuple
name = ("Michael")
print(type(name))
print()

# tuple with different data type
bio = ("Michael", "Aroworade", 27, 5.8, "Male")
print(bio)
print()

# tuple constructor
names = tuple(("Michael", "Aroworade", "Ayodele"))
print(names)
print()

# Join two tuple
names = ("Michael", "Aroworade", "Ayodele")
bio = ("Software", "Electrical", "Embedded")
data = names + bio
print(data)
