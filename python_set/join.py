# Join two sets using union()
names = {"Michael", "Aroworade", "Ayodele"}
bio = {"Software", "Network", "Electrical"}
data = names.union(bio)
print(data, end="\n\n")

# Using update()
names.update(bio)
print(data, end="\n\n")

# using intersection(), returns items that exist in both. intersection_update() keeps all
names = {"Michael", "Aroworade", "Ayodele", "Software"}
bio = {"Software", "Network", "Electrical", "Michael"}
data = names.intersection(bio)
names.intersection_update(bio)
print(data, end="\n\n")
print(names)
print()

# Keep all but not the duplicates using symmetric_difference_update()
# symmetric_difference() will return a new set.
names = {"Michael", "Aroworade", "Ayodele", "Software"}
bio = {"Software", "Network", "Electrical", "Michael"}
data = names.symmetric_difference(bio)
print(data, end="\n\n")
names.symmetric_difference_update(bio)
print(names, end="\n\n")
