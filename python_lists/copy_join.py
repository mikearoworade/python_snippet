# You can not copy by typing list2 = list1. list2 will only be a reference to list1

names1 = ['Michael', 'Ayodele', 'Oluwaseun', 'Aroworade']
names2 = names1.copy()
print(names1)
print(names2)

# Or use list()
names3 = list(names1)
print(names3)

# join two lists
names = ["Michael", "Aroworade"]
bio = ["Software Engineer", "Electrical / Network Engineer"]
data = names + bio
print(data)
print()

names.extend(bio)
print(names)
