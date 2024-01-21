# Dictionary are used to store data values in key:value pairs
# In earlier version of python, 3.7 above, python are ordered, changeable
# and do not allow duplicates.
bio = {
    "firstname": "Ayodele",
    "middlename": "Michael",
    "lastname": "Aroworade",
    "age": 27
}
print(bio, end="\n\n")

# print dictionary item
print(bio["age"])
print()

# Length of dictionary
print(len(bio))
print()

# the values in dictionary can be any data type
bio = {
    "firstname": "Ayodele",
    "middlename": "Michael",
    "lastname": "Aroworade",
    "birthday": [26, 3, 1996]
}
print(bio)
print(type(bio), end="\n\n")

# dict constructor
names = dict(firstname="Ayodele", lastname="Aroworade", age=27)
print(names)

# Copy dictionary: you can not copy by doing data = name. use copy()
data = names.copy()
print(data, end="\n\n")


# Nested dictionary
students = {
    "1st": {
        "firstname": "Imoh",
        "lastname": "Bassey"
    },
    "2nd": {
        "firstname": "Charles",
        "lastname": "Tessian"
    },
    "3rd": {
        "firstname": "Michael",
        "lastname": "Dean"
    }
}
print(students)

# Access item in nested dictionary
print(students["3rd"]["firstname"])
