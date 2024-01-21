# Python has two primitive loop commands: while and for loop
# while loop
i = 1
while i < 6:
    print(i)
    i += 1
print()

# Break statement - break can stop the loop even if the while condition is true.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print()

# Continue statement - continue can stop the current iteration, and continue with next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print()

# Python for
names = ["Michael", "Ayodele", "Aroworade"]
for name in names:
    print(name)
print()

# Looping through a string
name = "Ayo"
for i in name:
    print(i)
print()

# Break statement
names = ["Michael", "Oluwaseun", "Aroworade"]
for name in names:
    if name == "Oluwaseun":
        break
    print(name)
print()

# Continue statement
for name in names:
    if name == "Oluwaseun":
        continue
    print(name)
print()

# Range function
for i in range(4):
    print(i)
print()

# range: Using start parameter
for i in range(1, 4):
    print(i)
print()

# else in for loop
for i in range(1, 4):
    print(i)
else:
    print("Finished..")
print()

# Nested loop
stats = ["Smart", "Fine"]
names = ["Michael", "Ayodele", "Aroworade"]

for x in stats:
    for y in names:
        print(x, y)
print()

