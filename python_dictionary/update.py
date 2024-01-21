# Change values.
bio = {
    "firstname": "Oluwaseun",
    "middlename": "Michael",
    "lastname": "Aroworade",
    "age": 27
}
print(bio)
bio["firstname"] = "Ayodele"
print(bio, end="\n\n")

# update() will update the dictionary with the items from given argument
bio.update({"job": "Software Engineer"})
print(bio)

# Remove item using pop()
bio.pop("middlename")
print(bio)

# popitem() will remove last inserted item
bio.popitem()
print(bio)

# del remove the item with specified key name
del bio["age"]
print(bio)

# clear empties dictionary
# you can completely delete dictionary with del
bio.clear()
print(bio)
del bio
