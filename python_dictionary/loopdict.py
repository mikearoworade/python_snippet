data = {
    "firstname": "Ayodele",
    "middlename": "Michael",
    "lastname": "Aroworade",
    "age": 27
}

# Using for loop: print keys
for key in data:
    print(key)
print()
# OR
for key in data.keys():
    print(key)
print()

# Using for loop: print value
for key in data:
    print(data[key])
print()
# OR
for value in data.values():
    print(value)
print()

# Using items()
for key, value in data.items():
    print("{}: {}".format(key, value))
print()
