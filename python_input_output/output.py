# They are several ways to format output using string method
"""
Using string modulo operator (%)
Using format method
"""
# Modulo operator
print("Day: %2d, Month: %4d, Year: %6d" % (22, 1, 2024))  # spaces + character
print("Height: %4.2f, Weight: %6.3f" % (5.8, 78.98))
# Print octal value
print("%7.3o" % 25)   # print octal value
# Print Exponential value
print("%10.3E" % 356.08977)
print()

# Using format method
day = 22
month = 1
year = 2024
print("Day = {}, Month = {}, Year = {}".format(day, month, year))
print("I love {} and {} programming languages".format('Python', 'C'))
print("I love {0} and {1} programming languages".format('Python', 'C'))
print("I love {1} and {0} programming languages".format('Python', 'C'))

skill1 = "Software Engineer"
skill2 = "DevOps/Cloud Engineer"
print(f"I am a {skill1} and a {skill2}.")