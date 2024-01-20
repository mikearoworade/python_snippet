# You can loop through list of items
names = ["Ayodele", "Michael", "Oluwaseun", "Aroworade"]
print(names)

for name in names:
    print(name)
print()

# Using len and range
for i in range(len(names)):  # iterable created is [0, 1, 2]
    print(names[i])
print()

# Using while loop
languages = ["Python", "Javascript", "C", "Java", "Swift", "SQL"]
i = 0
while i < len(languages):
    print(languages[i])
    i = i + 1
print()

# Looping Using list comprehension
skills = ["Electrical", "Software", "Embedded", "Network"]
[print(skill) for skill in skills]
