# List item are indexed and can be accessed using index number
names = ["Michael", "Ayodele", "Aroworade"]
print(names[1])

# Negative indexing
print(names[-1])

# Range of indexes
bio = ["Michael", "Ayodele", "Aroworade", "Software Engineer", "Python"]
print(bio[1:4])  # The search will start at index 1 (included) and end at index 4 (not included)
print(bio[1:])
print(bio[-4:-1])

# Check if item exit
if "Python" in bio:
    print("Yes, 'Python' is present.")

# Change list item
names = ["Michael", "Ayodele", "Aroworade"]
names[1] = "Oluwaseun"
print(names)

# Change a range of list value
names[1:3] = ["Vastcrown", "Incorporation"]
print(names)
print()

# Insert item with replacing
names = ["Michael", "Ayodele", "Aroworade"]
print(names)
names.insert(2, "Oluwaseun")
print(names)

