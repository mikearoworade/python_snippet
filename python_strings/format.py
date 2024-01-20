# We cannot combine strings and number. Hence, format.
"""
age = 27
intro = "My name is Michael, I am " + 27
print(intro)

intro = "My name is Michael, I am " + 27
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str
"""

# Using format()
age = 27
intro = "My name is Michael, I am {}"
print(intro.format(age))
years = 4
print("I'm a Software Engineer with {} years experience".format(years))
print()

# format() takes unlimited number of arguments
days = 29
month = "February"
year = 2024
verdict = "There are {} days in the month of {}, {}."
print(verdict.format(days, month, year))

# correct placeholder, use index.
verdict = "There are {2} days in the month of {0}, {1}."
print(verdict.format(month, year, days))
print()
