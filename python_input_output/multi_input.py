# Using split
day, month, year = input("Enter birthday: ").split()
print("Day = {}, Month = {}, Year = {}".format(day, month, year))
print()


# List comprehension
day, month, year = [int(i) for i in input("Enter today's date: ").split()]
print("Day = {}, Month = {}, Year = {}".format(day, month, year))
print()

# print() with end and sep
print('22', '01', '2024', sep='/', end="\n")
