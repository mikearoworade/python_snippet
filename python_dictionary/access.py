# You can access the items of a dictionary by referring to its key name
bio = {
    "firstname": "Ayodele",
    "middlename": "Michael",
    "lastname": "Aroworade",
    "age": 27
}
print(bio)

# Get the value of "middlename" key
main = bio["middlename"]
print(main, end="\n\n")

# you can also use get()
main = bio.get("middlename")
print(main, end="\n\n")

# keys() will return a list of all keys in dictionary
keys = bio.keys()
print(keys)
# add new key:value
bio["job"] = "Software Engineer"
print(keys, end="\n\n")

# Get values()
values = bio.values()
print(values)
# add new key:value
bio["year"] = 1996
print(values, end="\n\n")

# items() method will return each item in a dictionary, as tuple of list
items = bio.items()
print(items)
# add new key value
bio["height"] = 5.8
print(items, end="\n\n")

# Check if a key exists
if "age" in bio:
    print("Yes, 'age' key is present in bio data.")