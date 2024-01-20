# Comprehension offers a shorter syntax

# Normal Syntax
names = ["Michael", "Ayodele", "Oluwaseun", "Aroworade", "Vascrown"]
w_present = []

print(names)
for name in names:
    if 'w' in name:
        w_present.append(name)

print(w_present)

# Using list comprehension
# newlist = [expression for item in iterable if condition == True]
names = ["Michael", "Ayodele", "Oluwaseun", "Aroworade", "Vascrown"]
w_present = [name for name in names if 'w' in name]

print(w_present)
print()

# range list comprehension
newlist = [x for x in range(10)]
print(newlist)
newlist_less_than_5 = [x for x in range(10) if x < 5]
print(newlist_less_than_5)