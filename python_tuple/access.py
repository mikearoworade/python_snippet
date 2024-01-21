# Access tuple items
names = ("Aroworade", "Michael", "Ayodele", "Oluwaseun", "Vastcrown")
print(names[1])
print()

# Print last item of the tuple
print(names[-1])
print()

# Return third, fourth, and fifth
print(names[2:5])

# Return from beginning to but not included, vastcrown
print(names[:4])

# Return the items from "Michael" to end
print(names[1:])

# Return range of negative index
print(names[-4:-1])
print()

# Check if item exist
if "Oluwaseun" in names:
    print("Yes, Oluwaseun is in the name tuple")
