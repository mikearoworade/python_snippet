# Python does not have a built-in support for Arrays, but python lists can be used instead.
names = ["Michael", "Ayodele", "Aroworade"]
print(names)

# Get the value of the first array item
firstname = names[0]
print(firstname)

# Modify the value of the 2nd array item
names[1] = "Oluwaseun"
print(names)

# Length of an array
print("Length of array 'names' is {}".format(len(names)))
print()

# Looping through an array
for name in names:
    print(name)
print()

# Adding array element
names.append("Ayodele")
print(names)
print()

# Removing an array element using pop()
names.pop(1)
print(names)

# Removing an array element using remove()
names.remove("Ayodele")
print(names)
