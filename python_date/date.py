# Date in python is not a data type of its own, but we can import a module called "datetime"
# to work with dates as date object
import datetime

# The date below contains year, month, day, hour, minute, second and microsecond
now = datetime.datetime.now()
print(now)  # 2024-01-22 02:47:29.601568

# Return year and weekday
print(now.year)  # 2024
print(now.strftime("%A"))  # Monday

# Create a date object
past = datetime.datetime(1996, 3, 26)
print(past)  # 1996-03-26 00:00:00

# strftime() - it is a method for formatting date object into readable strings.
# Display day of the month
print(past.strftime("%B"))  # March
print(past.strftime("%b"))  # Mar
print(past.strftime("%a"))  # Tue
print(past.strftime("%w"))  # 2. i.e Monday is 1, sunday is 0, saturday is 6
print(past.strftime("%Y"))  # 1996
print(past.strftime("%y"))  # 96
print(past.strftime("%H"))  # 00
print(past.strftime("%M"))  # 00
print(past.strftime("%S"))  # 00
