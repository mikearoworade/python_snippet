# Set are unordered, unchangeable, do not allow duplicates
names = {"Michael", "Ayodele", "Aroworade", "Michael"}
print(names, end="\n\n")

# True and 1 are considered the same value, False and 0 too.
names = {"Michael", "Ayodele", "Aroworade", True, 1, 27, False, 0}
print(names, end="\n\n")

# Length of a set
names = {"Michael", "Ayodele", "Aroworade", "Michael"}
print(len(names))
print()

# set constructor
names = set(("Michael", "Ayodele", "Aroworade"))
print(names)
