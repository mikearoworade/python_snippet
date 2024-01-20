# Remove specified item
names = ["Michael", "Ayodele", "Oluwaseun", "Aroworade"]
print(names)
names.remove("Oluwaseun")
print(names)
print()

# Remove specified index
names = ["Michael", "Ayodele", "Oluwaseun", "Aroworade"]
print(names)
names.pop(2)
print(names)
names.pop()
print(names)

# del also remove specified index
del names[0]
print(names)
del names
# print(names) -- this will cause an error

# clear() empties the list
names = ["Michael", "Ayodele", "Aroworade"]
print(names)
names.clear()
print(names)
