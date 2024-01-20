# Strings in python are surrounded by either single or double quotes
print('Hello')
print("Michael")
print()

# Assign String to a variable
name = "Michael"
print(name)
print()

# Multi-line String
bio = """My name is Michael Aroworade
I currently work at JubailiBros Engineering
I'm an IT Support/Software Engineer
I have over 4 years of working experience.
"""
print(bio)

# Strings are arrays
name = "Michael Aroworade"
print(name[0])
print(name[6])
print()

# Looping through a string
fruit = "Banana"
for i in fruit:
    print(i)

print()

# String length
fullname = "Michael Aroworade"
print(len(fullname))
print()

# Check string
txt = "Software Engineering is my passion, and i will ensure i breakthrough through"
print("Software" in txt)
if "Software" in txt:
    print("Yes, Software is present.")
print()

# Check if not
txt = "Python is a great high level programming language."
print("Java" not in txt)
if "Java" not in txt:
    print("No, Java not present.")
print()

# Escape Character (\")
text = "I'm the \"King\" in the North"
print(text)
