# Tuples are unchangeable. Hence, you can't add, remove, delete, change etc.
names = ("Aroworade", "Michael", "Ayodele", "Oluwaseun", "Vastcrown")
print(names, end="\n\n")

# To change, first convert tto list
names_list = list(names)
names_list[4] = "Hugethrone"
names = tuple(names_list)
print(names, end="\n\n")

# Add item
names = ("Aroworade", "Michael", "Ayodele", "Oluwaseun", "Vastcrown")
names_list = list(names)
names_list.append("Hugethrone")
names = tuple(names_list)
print(names)
print()

# Add tuple to a tuple
names = ("Aroworade", "Michael", "Ayodele", "Oluwaseun", "Vastcrown")
single = ("Hugethrone",)
names += single
print(names, end="\n\n")

# Remove item
names = ("Aroworade", "Michael", "Ayodele", "Oluwaseun", "Vastcrown")
names_list = list(names)
names_list.remove("Oluwaseun")
names = tuple(names_list)
print(names)

# Delete tuple
del names
# print(names) -- will raise an error
print()

# Packing a tuple: when we create a tuple, we normally assign values to it. This is called packing.
names = ("Aroworade", "Michael", "Ayodele")
print(names)


# Unpacking tuple: in python, we are also allowed to extract the values back into variables
(lastname, middlename, firstname) = names
print(lastname)
print(middlename)
print(firstname)
print()

# '*' ensure unmatched number of items becomes a list
names = ("Aroworade", "Michael", "Ayodele", "Oluwaseun", "Vastcrown")
(lastname, middlename, firstname, *other) = names
print(lastname)
print(middlename)
print(firstname)
print(other)
print()
