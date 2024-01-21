# Python conditions and if statements
# "if" statement
a = 27
b = 29
if b > a:
    print("b is greater than a", end="\n\n")

# elif
a = 27
b = 27
if b > a:
    print("b is greater than a", end="\n\n")
elif a == b:
    print("a and b are equal.", end="\n\n")

# else
a = 30
b = 29
if b > a:
    print("b is greater than a", end="\n\n")
elif a == b:
    print("a and b are equal", end="\n\n")
else:
    print("a is greater than b", end="\n\n")


# Ternary operators
print("A") if a > b else print("B")
print()

# logical operators: and
a = 29
b = 27
c = 24
if a > b and a > c:
    print("Both conditions are true")
print()

# logical operators: or
a = 29
b = 27
c = 24
if a > b or a > c:
    print("At least one of the conditions is True.", end="\n\n")

# logical operator: not
a = 27
b = 29
if not a > b:
    print("a is not greater than b", end="\n\n")

# Nested if
age = 27
if age > 19:
    print("No longer a teenager")
    if age > 25:
        print("Man, welcome to the age of total accountability.")

# pass - "if" statement cannot be empty. Hence, "pass" can be used when there is no content.
age = 27
if age > 20:
    pass
