# You cannot access items in a set by referring to an index or a key
names = {"Michael", "Ayodele", "Aroworade"}
for name in names:
    print(name)
print()

# Check if exist
print("Michael" in names)
print()

# Once a set is created, you cannot change its items, but you can add new items.
# add()
names.add("Oluwaseun")
print(names)
print()

# add sets together using update()
names = {"Michael", "Ayodele", "Aroworade"}
bio = {"Software", "Network", "Electrical"}
names.update(bio)
print(names, end="\n\n")

# add any iterable
names = {"Michael", "Ayodele", "Aroworade"}
bio = ("Software", "Network", "Electrical")
names.update(bio)
print(names, end="\n\n")


# Remove set items -- To remove set items, use the remove(), or discard(). Note: discard doesn't raise ERROR.
names = {"Michael", "Ayodele", "Aroworade"}
names.remove("Ayodele")
print(names)
names.discard("Ayodele")
print(names, end="\n\n")

# pop() here doesn't remove th last, rather random item.
# clear() empties the set
# del deletes completely
names = {"Michael", "Ayodele", "Aroworade"}
names.pop()
print(names)
names.clear()
print(names)
del names  # names doesn't exist anymore.
